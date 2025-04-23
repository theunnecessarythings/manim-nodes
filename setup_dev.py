#!/usr/bin/env python3
import os
import sys
import site
import argparse
from pathlib import Path
import shutil

def setup_dev_environment(blender_addons_path=None):
    """Set up a development environment for the Manim Node Editor addon"""
    # Get the current directory (where this script is run from)
    current_dir = Path.cwd()
    addon_dir = current_dir / "manim_node_editor"
    
    if not addon_dir.exists():
        print(f"Error: Could not find the addon directory at {addon_dir}")
        return False
    
    # Determine Blender's addon directory if not provided
    if not blender_addons_path:
        # Try to find Blender's addon path
        if sys.platform == "win32":
            appdata = os.getenv("APPDATA")
            if appdata:
                blender_versions = Path(appdata) / "Blender Foundation" / "Blender"
        elif sys.platform == "darwin":
            blender_versions = Path.home() / "Library" / "Application Support" / "Blender"
        else:  # Linux and others
            blender_versions = Path.home() / ".config" / "blender"
        
        # Find the latest version
        latest_version = None
        latest_version_num = 0
        
        if blender_versions.exists():
            for version_dir in blender_versions.iterdir():
                if version_dir.is_dir() and version_dir.name[0].isdigit():
                    try:
                        version_num = float(version_dir.name.split('.')[0])
                        if version_num > latest_version_num:
                            latest_version_num = version_num
                            latest_version = version_dir
                    except:
                        pass
        
        if latest_version:
            blender_addons_path = latest_version / "scripts" / "addons"
    
    # If we still don't have a path, ask the user
    if not blender_addons_path or not Path(blender_addons_path).exists():
        print("Could not determine Blender addons directory automatically.")
        blender_addons_path = input("Please enter the full path to your Blender addons directory: ")
        blender_addons_path = Path(blender_addons_path)
    
    # Create the symlink or junction (Windows)
    target_link = blender_addons_path / "manim_node_editor"
    
    # Remove existing link or directory if it exists
    if target_link.exists():
        if target_link.is_symlink() or (sys.platform == "win32" and os.path.isdir(target_link)):
            if sys.platform == "win32":
                # On Windows, we need to handle junctions differently
                if os.path.isdir(target_link) and not os.path.islink(target_link):
                    shutil.rmtree(target_link)
                else:
                    os.unlink(target_link)
            else:
                os.unlink(target_link)
        else:
            print(f"Warning: {target_link} exists and is not a symlink. Please remove it manually.")
            return False
    
    # Create the link
    try:
        if sys.platform == "win32":
            # Windows needs special handling for directory junctions
            import subprocess
            subprocess.check_call(f'mklink /J "{target_link}" "{addon_dir}"', shell=True)
        else:
            # Unix-like systems can use a standard symlink
            os.symlink(addon_dir, target_link, target_is_directory=True)
        
        print(f"Successfully created development link from {addon_dir} to {target_link}")
        return True
    except Exception as e:
        print(f"Error creating symbolic link: {e}")
        print("You may need to run this script with administrator privileges.")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Set up a development environment for the Manim Node Editor Blender addon")
    parser.add_argument("--blender-addons", type=str, help="Path to Blender addons directory")
    args = parser.parse_args()
    
    setup_dev_environment(args.blender_addons) 