bl_info = {
    "name": "Addon Watcher",
    "author": "Developer",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "Preferences > Add-ons",
    "description": "Auto-reload addons when their files change",
    "warning": "",
    "wiki_url": "",
    "category": "Development",
}

import bpy
import os
import sys
import importlib
import time
import threading
from datetime import datetime
from pathlib import Path

# Dictionary to store monitored addons and their file modification times
monitored_addons = {}
file_mtimes = {}
watcher_thread = None
should_stop = False

class AddonWatcherPanel(bpy.types.Panel):
    bl_label = "Addon Watcher"
    bl_idname = "OBJECT_PT_addon_watcher"
    bl_space_type = 'PREFERENCES'
    bl_region_type = 'WINDOW'
    bl_context = "addons"
    
    def draw(self, context):
        layout = self.layout
        
        # Add a button to watch the current addon
        if hasattr(context, "preferences") and hasattr(context.preferences, "active_section"):
            if context.preferences.active_section == 'ADDONS':
                addon = context.window_manager.addon_watcher
                
                if watcher_thread and watcher_thread.is_alive():
                    layout.operator("preferences.stop_watching_addons", icon='CANCEL')
                    
                    # Show monitored addons
                    box = layout.box()
                    box.label(text="Currently Monitoring:")
                    for addon_name in monitored_addons:
                        row = box.row()
                        row.label(text=addon_name)
                else:
                    row = layout.row()
                    row.prop(addon, "target_addon")
                    row = layout.row()
                    row.prop(addon, "monitor_interval")
                    row = layout.row()
                    row.operator("preferences.start_watching_addon", icon='PLAY')

def reload_addon(addon_name):
    """Reload all modules for a specific addon"""
    print(f"Reloading addon: {addon_name}")
    
    # Disable the addon first
    try:
        bpy.ops.preferences.addon_disable(module=addon_name)
    except:
        print(f"Could not disable addon {addon_name}")
    
    # Find all modules belonging to this addon
    addon_modules = [
        module_name for module_name in list(sys.modules.keys())
        if module_name == addon_name or module_name.startswith(addon_name + ".")
    ]
    
    # Reload each module
    for module_name in addon_modules:
        if module_name in sys.modules:
            # Store the module object
            module = sys.modules[module_name]
            # Reload it
            try:
                importlib.reload(module)
                print(f"Reloaded module: {module_name}")
            except:
                print(f"Failed to reload module: {module_name}")
    
    # Re-enable the addon
    try:
        bpy.ops.preferences.addon_enable(module=addon_name)
        print(f"Re-enabled addon: {addon_name}")
    except:
        print(f"Could not re-enable addon {addon_name}")
    
    # Update UI
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            area.tag_redraw()

def get_addon_directory(addon_name):
    """Get the directory of an addon from its name"""
    # Find the addon module
    if addon_name in sys.modules:
        module = sys.modules[addon_name]
        # Get the module file path
        if hasattr(module, "__file__"):
            path = Path(module.__file__)
            return path.parent
    return None

def get_addon_files(directory):
    """Get all Python files in an addon directory"""
    if not directory or not directory.exists():
        return []
    
    python_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files

def check_for_changes():
    """Check if any of the monitored addon files have changed"""
    changed_addons = []
    
    for addon_name, directory in monitored_addons.items():
        files = get_addon_files(directory)
        
        for file_path in files:
            # Get current modification time
            try:
                current_mtime = os.path.getmtime(file_path)
                
                # If this is the first time seeing this file, record the mtime
                if file_path not in file_mtimes:
                    file_mtimes[file_path] = current_mtime
                    continue
                
                # Check if file has been modified
                if current_mtime > file_mtimes[file_path]:
                    print(f"File changed: {file_path}")
                    file_mtimes[file_path] = current_mtime
                    if addon_name not in changed_addons:
                        changed_addons.append(addon_name)
            except:
                pass
    
    return changed_addons

def watcher_function():
    """Thread function to watch for file changes"""
    global should_stop
    
    print("Addon watcher started")
    
    while not should_stop:
        # Check for changes
        changed_addons = check_for_changes()
        
        # Reload any changed addons
        if changed_addons:
            print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Changes detected")
            for addon_name in changed_addons:
                # Queue the reload to run in the main thread on next window redraw
                bpy.app.timers.register(
                    lambda addon=addon_name: reload_addon(addon)
                )
        
        # Sleep for the specified interval
        time.sleep(bpy.context.window_manager.addon_watcher.monitor_interval)

class PREFERENCES_OT_start_watching_addon(bpy.types.Operator):
    """Start watching an addon for changes"""
    bl_idname = "preferences.start_watching_addon"
    bl_label = "Start Watching Addon"
    
    def execute(self, context):
        global monitored_addons, watcher_thread, should_stop
        
        addon_name = context.window_manager.addon_watcher.target_addon
        
        # Check if addon exists
        if addon_name not in bpy.context.preferences.addons:
            self.report({'ERROR'}, f"Addon {addon_name} is not enabled")
            return {'CANCELLED'}
        
        # Get addon directory
        directory = get_addon_directory(addon_name)
        if not directory:
            self.report({'ERROR'}, f"Could not find directory for addon {addon_name}")
            return {'CANCELLED'}
        
        # Add to monitored addons
        monitored_addons[addon_name] = directory
        print(f"Monitoring addon: {addon_name} at {directory}")
        
        # Start the watcher thread if not already running
        if not watcher_thread or not watcher_thread.is_alive():
            should_stop = False
            watcher_thread = threading.Thread(target=watcher_function)
            watcher_thread.daemon = True
            watcher_thread.start()
        
        return {'FINISHED'}

class PREFERENCES_OT_stop_watching_addons(bpy.types.Operator):
    """Stop watching addons for changes"""
    bl_idname = "preferences.stop_watching_addons"
    bl_label = "Stop Watching Addons"
    
    def execute(self, context):
        global monitored_addons, watcher_thread, should_stop
        
        # Stop the watcher thread
        should_stop = True
        if watcher_thread and watcher_thread.is_alive():
            # Let the thread exit gracefully
            watcher_thread.join(2.0)
        
        # Clear monitored addons
        monitored_addons = {}
        file_mtimes.clear()
        
        print("Stopped watching addons")
        return {'FINISHED'}

class AddonWatcherSettings(bpy.types.PropertyGroup):
    target_addon: bpy.props.StringProperty(
        name="Addon Name",
        description="Name of the addon to watch for changes",
        default="manim_node_editor"
    )
    
    monitor_interval: bpy.props.FloatProperty(
        name="Check Interval",
        description="How often to check for changes (in seconds)",
        default=1.0,
        min=0.5,
        max=10.0
    )

classes = (
    AddonWatcherSettings,
    AddonWatcherPanel,
    PREFERENCES_OT_start_watching_addon,
    PREFERENCES_OT_stop_watching_addons,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.WindowManager.addon_watcher = bpy.props.PointerProperty(type=AddonWatcherSettings)

def unregister():
    global should_stop, watcher_thread
    
    # Stop the watcher thread
    should_stop = True
    if watcher_thread and watcher_thread.is_alive():
        watcher_thread.join(2.0)
    
    # Unregister classes
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    
    del bpy.types.WindowManager.addon_watcher

if __name__ == "__main__":
    register() 