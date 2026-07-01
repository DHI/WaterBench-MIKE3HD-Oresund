# create a zip file of this repo, excluding all dirs starting with a . or __ in the name; exclude also "output"

import os
import zipfile
import glob

# This is the case name of the WaterBench case, e.g. "MIKE3HD-Oresund"
case_name = "MIKE3HD-Oresund"

# This is the path where the zip file will be created, e.g. ".publish/MIKE3HD-Oresund-repo.zip"
# before uploading to github the .zip file should be removed. It will only be uploaded to Zenodo.
zip_fn = f".publish/{case_name}.zip"


def zip_repo():
    with zipfile.ZipFile(zip_fn, "w") as z:
        for fn in glob.glob("**/*", recursive=True):
            if (
                not any([fn.startswith(x) for x in [".", "__", "output" + os.sep]])
                and "__" not in fn
                and "." in fn
            ):
                z.write(fn)
            else:
                print(f"Excluded: {fn}")

    print(f"Zip file created: {zip_fn}")


if __name__ == "__main__":
    zip_repo()
