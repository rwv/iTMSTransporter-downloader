import urllib.request
import json
import zipfile
import tarfile
import tempfile
import os
import shutil
import glob

ARTIFACTS_API = "https://api.github.com/repos/rwv/iTMSTransporter-downloader/actions/artifacts"
ARTIFACT_DOWNLOAD_API = "https://nightly.link/rwv/iTMSTransporter-downloader/actions/artifacts/{artifact_id}.zip"
CACHE_FOLDER_NAME = "com.apple.amp.itmstransporter"
CACHE_FOLDER_ROOT = os.path.expanduser("~/Library/Caches")
CACHE_FOLDER_PATH = os.path.join(CACHE_FOLDER_ROOT, CACHE_FOLDER_NAME)
ARTIFACT_FILENAME = "com.apple.amp.itmstransporter.tar.gz"
ARTIFACT_FILENAME_ZIP = ARTIFACT_FILENAME + ".zip"
BINARY_PREFIX = "./"
ARTIFACT_ZIP_PATH = os.path.join(BINARY_PREFIX, ARTIFACT_FILENAME_ZIP)
GITHUB_RUNNDER_HOME = "/Users/runner"

def download_latest_artifact(filename):
    # need third party service to download the artifact
    # see https://github.com/actions/upload-artifact/issues/51
    response = urllib.request.urlopen(ARTIFACTS_API)
    artifacts = json.loads(response.read())
    for artifact in artifacts["artifacts"]:
        if artifact["name"] == ARTIFACT_FILENAME:
            artifact_url = ARTIFACT_DOWNLOAD_API.format(artifact_id=artifact["id"])
            print("Downloading artifact from: " + artifact_url)
            urllib.request.urlretrieve(artifact_url, filename=filename)

def unzip_untar_file(filename, output_dir):
    print(f"Unzip and untar {filename} to {output_dir}")
    temp_folder = tempfile.TemporaryDirectory()
    with zipfile.ZipFile(filename) as zf:
        zf.extract(member=ARTIFACT_FILENAME, path=temp_folder.name)
    with tarfile.open(os.path.join(temp_folder.name, ARTIFACT_FILENAME), mode="r:gz") as tf:
        tf.extractall(output_dir)

def change_owner(path, owner):
    print(f"Change file owner to local user {owner}")
    os.system(f"chown -R {owner} {path}")

def modify_repository_xml(path):
    print(f"Modify {path}")
    local_home = os.path.expanduser("~")
    with open(path) as f:
        data = f.read()
    with open(path, "w") as f:
        f.write(data.replace(GITHUB_RUNNDER_HOME, local_home))

if __name__ == "__main__":
    if os.path.exists(ARTIFACT_ZIP_PATH):
        print("Artifact already exists, skipping download")
    else:
        download_latest_artifact(ARTIFACT_ZIP_PATH)

    temp_folder = tempfile.TemporaryDirectory()
    unzip_untar_file(ARTIFACT_ZIP_PATH, output_dir=temp_folder.name)
    change_owner(temp_folder.name, owner=os.getuid())

    temp_cache_path = os.path.join(temp_folder.name, CACHE_FOLDER_NAME)

    xml_paths = glob.glob(os.path.join(temp_cache_path, "obr", "*", "repository.xml"))
    for xml_path in xml_paths:
        modify_repository_xml(xml_path)

    print(f"replace {CACHE_FOLDER_PATH}")
    shutil.rmtree(CACHE_FOLDER_PATH, ignore_errors=True)
    shutil.move(temp_cache_path, CACHE_FOLDER_PATH)
