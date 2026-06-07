#!/usr/bin/env python3
"""
Stellar Blade Mod Manager – Auto installer for skin and texture mods.
Open source – no game memory modification.
"""

import os
import sys
import shutil
from pathlib import Path

STEAM_PATHS = [
    r"C:\Program Files (x86)\Steam\steamapps\common\StellarBlade",
    r"C:\Program Files\Steam\steamapps\common\StellarBlade",
]

def find_game_path():
    for path in STEAM_PATHS:
        if os.path.exists(path):
            return path
    return None

def install_mods(archive_path, mods_path):
    if not os.path.exists(mods_path):
        os.makedirs(mods_path, exist_ok=True)
    
    mod_files = [f for f in os.listdir(archive_path) if f.endswith('.pak')]
    for mod_file in mod_files:
        src = os.path.join(archive_path, mod_file)
        dst = os.path.join(mods_path, mod_file)
        shutil.copy2(src, dst)
        print(f"✅ Installed: {mod_file}")
    print("Installation complete. Launch the game.")

def main():
    game_path = find_game_path()
    if not game_path:
        print("❌ Stellar Blade not found. Install the game first.")
        return
    
    paks_path = os.path.join(game_path, "SB", "Content", "Paks")
    mods_path = os.path.join(paks_path, "~mods")
    
    if not os.path.exists(paks_path):
        print(f"❌ Game folder is valid but Paks folder not found: {paks_path}")
        return
    
    # Simulate installation of mods from the extracted archive
    archive_path = os.path.dirname(sys.argv[0]) if hasattr(sys, 'frozen') else os.getcwd()
    install_mods(archive_path, mods_path)
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()