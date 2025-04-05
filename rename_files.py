import os
import re
import glob

def rename_files():
    build_dir = "build"
    if not os.path.exists(build_dir):
        print("Build directory not found")
        return

    # Regular expressions for matching file names
    # Match format: YouTube-Music-RVX-8.13.51-(arm64-v8a).zip
    music_pattern = re.compile(r'YouTube-Music-RVX-(\d+\.\d+\.\d+)-\(([^)]+)\)\.(apk|zip)')
    # Match format: YouTube-OG-Monet-RVX-20.13.37.apk
    monet_pattern = re.compile(r'YouTube-OG-Monet-RVX-(\d+\.\d+\.\d+)\.(apk|zip)')

    print("Checking files in build directory...")
    files_found = False
    
    for filename in os.listdir(build_dir):
        filepath = os.path.join(build_dir, filename)
        if not os.path.isfile(filepath):
            continue
            
        files_found = True
        print(f"Checking file: {filename}")
        
        # Handle YouTube Music files
        music_match = music_pattern.match(filename)
        if music_match:
            version, arch, ext = music_match.groups()
            new_name = f"YouTube-Music-RVX-{version}-({arch}).{ext}"
            new_path = os.path.join(build_dir, new_name)
            
            try:
                if filepath != new_path:
                    os.rename(filepath, new_path)
                    print(f"Renamed: {filename} -> {new_name}")
                else:
                    print(f"File already has correct name: {filename}")
            except Exception as e:
                print(f"Error renaming {filename}: {e}")
            continue
            
        # Handle YouTube Monet files
        monet_match = monet_pattern.match(filename)
        if monet_match:
            version, ext = monet_match.groups()
            new_name = f"YouTube-OG-Monet-RVX-{version}.{ext}"
            new_path = os.path.join(build_dir, new_name)
            
            try:
                if filepath != new_path:
                    os.rename(filepath, new_path)
                    print(f"Renamed: {filename} -> {new_name}")
                else:
                    print(f"File already has correct name: {filename}")
            except Exception as e:
                print(f"Error renaming {filename}: {e}")
            continue
            
        print(f"No match for pattern: {filename}")
    
    if not files_found:
        print("No files found in build directory")
    
    # List all files in build directory after renaming
    print("\nFiles in build directory after renaming:")
    for file in os.listdir(build_dir):
        print(f"- {file}")

if __name__ == "__main__":
    rename_files() 