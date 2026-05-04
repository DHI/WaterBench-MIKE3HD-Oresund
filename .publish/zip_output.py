import zipfile

# This is the case name of the WaterBench case, e.g. "MIKE21HD-Oresund"
case_name = ""

# This is the path where the output files are located, e.g. "./output".
# The folder should contain the actual data and a README.md specifying how to cite the WaterBench case.
path_output = "./output"

# This is the path where the zip file will be created, e.g. ".publish/MIKE21HD-Oresund-output.zip"
# before uploading to github the .zip file should be removed. It will only be uploaded to Zenodo.
zip_fn = f".publish/{case_name}-output.zip"


def zip_repo():
    with zipfile.ZipFile(zip_fn, "w") as z:
        z.write(path_output + "/Area.dfsu", arcname="Area.dfsu")
        z.write(path_output + "/Points.dfs0", arcname="Points.dfs0")
        z.write(path_output + "/README.md", arcname="README.md")
    print(f"Zip file created: {zip_fn}")


if __name__ == "__main__":
    zip_repo()
