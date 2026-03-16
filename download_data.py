import os
from huggingface_hub import hf_hub_download

# 保存先ディレクトリ
TARGET_DIR = "data"
os.makedirs(TARGET_DIR, exist_ok=True)

# IMPACT dataset
REPO_ID = "AI4Patents/IMPACT"

# 年
START_YEAR = 2007
END_YEAR = 2022

for year in range(START_YEAR, END_YEAR + 1):
    for ext in ["csv", "zip"]:
        filename = f"{year}.{ext}"
        print(f"Downloading {filename} ...")

        path = hf_hub_download(
            repo_id=REPO_ID,
            filename=filename,
            repo_type="dataset"
        )

        destination = os.path.join(TARGET_DIR, filename)

        # 既存ファイルがあれば削除
        if os.path.exists(destination):
            os.remove(destination)

        os.rename(path, destination)

print("Download finished.")