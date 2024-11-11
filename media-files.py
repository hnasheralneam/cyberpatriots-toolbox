import subprocess
import glob


media_types = ['*.jpg', '*.png', '*.mp3', '*.jpeg']
print(f"Supported file extensions: {media_types}")
extra_exts = input("Add more extensions separated by spaces (optional): ")
media_types.extend(extra_exts.split())
for ext in media_types:
    for filename in glob.iglob(f'/home/**/*{ext}', recursive=True):
        if input(f"Remove file {filename}? (Y/n): ").lower() in ['y', '']:
            subprocess.call(['rm', '-rf', filename])
