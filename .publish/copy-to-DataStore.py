import os
import shutil
import glob

# Destination path where the repository content will be copied
dest_path = r"\\DKCPH1-STOR.DHI.DK\Projects\11561006\WaterBench\WaterBench-MIKE3HD-Oresund-published"

# Copy all files except .zip files to the destination path, preserving the directory structure

def copy_to_datastore():
    for fn in glob.glob("**/*", recursive=True):
        if os.path.isfile(fn) and not fn.endswith(".zip"):
            dest_fn = os.path.join(dest_path, fn)
            os.makedirs(os.path.dirname(dest_fn), exist_ok=True)
            shutil.copy2(fn, dest_fn)
            print(f"Copied: {fn}")
    print(f"Done. Files copied to: {dest_path}")


if __name__ == "__main__":
    copy_to_datastore()
