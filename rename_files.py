import os
import re

def rename_files():
    build_dir = "build"
    if not os.path.exists(build_dir):
        print("Build directory not found")
        return

    # Regular expressions for matching file names
    music_pattern = re.compile(r'YouTube-Music-RVX-(\d+\.\d+\.\d+)\.([^.]+)\.([^.]+)')

    for filename in os.listdir(build_dir):
        filepath = os.path.join(build_dir, filename)
        if not os.path.isfile(filepath):
            continue

        # Handle YouTube Music files
        music_match = music_pattern.match(filename)
        if music_match:
            version, arch, ext = music_match.groups()
            new_name = f"YouTube-Music-RVX-{version}-({arch}).{ext}"
            new_path = os.path.join(build_dir, new_name)
            
            try:
                os.rename(filepath, new_path)
                print(f"Renamed: {filename} -> {new_name}")
            except Exception as e:
                print(f"Error renaming {filename}: {e}")

if __name__ == "__main__":
    rename_files() 