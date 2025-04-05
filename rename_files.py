import os
import re

def rename_files():
    build_dir = "build"
    if not os.path.exists(build_dir):
        print("Build directory not found")
        return

    # Regular expressions for matching file names
    # Match format: YouTube-Music-RVX-8.13.51-.arm64-v8a.zip
    music_dot_pattern = re.compile(r'YouTube-Music-RVX-(\d+\.\d+\.\d+)\.([^.]+)\.zip')
    music_dot_apk_pattern = re.compile(r'YouTube-Music-RVX-(\d+\.\d+\.\d+)\.([^.]+)\.apk')

    for filename in os.listdir(build_dir):
        filepath = os.path.join(build_dir, filename)
        if not os.path.isfile(filepath):
            continue

        # Handle YouTube Music APK files with dot before architecture
        music_dot_apk_match = music_dot_apk_pattern.match(filename)
        if music_dot_apk_match:
            version, arch = music_dot_apk_match.groups()
            new_name = f"YouTube-Music-RVX-{version}-({arch}).apk"
            new_path = os.path.join(build_dir, new_name)
            
            try:
                os.rename(filepath, new_path)
                print(f"Renamed: {filename} -> {new_name}")
            except Exception as e:
                print(f"Error renaming {filename}: {e}")
        
        # Handle YouTube Music module files with dot before architecture
        music_dot_match = music_dot_pattern.match(filename)
        if music_dot_match:
            version, arch = music_dot_match.groups()
            new_name = f"YouTube-Music-RVX-{version}-({arch}).zip"
            new_path = os.path.join(build_dir, new_name)
            
            try:
                os.rename(filepath, new_path)
                print(f"Renamed: {filename} -> {new_name}")
            except Exception as e:
                print(f"Error renaming {filename}: {e}")

if __name__ == "__main__":
    rename_files() 