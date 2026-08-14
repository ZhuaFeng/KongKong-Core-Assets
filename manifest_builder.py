# manifest_builder.py
import os
import hashlib
import json

# ==========================================
# ★ 設定區 (發布前請確認網址正確)
# ==========================================
# 你的 GitHub 儲存庫中，core_engine 資料夾的「Raw」根目錄網址
GITHUB_RAW_BASE_URL = "https://raw.githubusercontent.com/ZhuaFeng/KongKong-Core-Assets/main/core_engine"
TARGET_DIR = "core_engine"
OUTPUT_FILE = "manifest.json"
APP_VERSION = "0.0.0.01" # 這次更新的版本號

def calculate_md5(file_path):
    """計算檔案的 MD5 Hash"""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        print(f"計算 {file_path} Hash 失敗: {e}")
        return None

def build_manifest():
    if not os.path.exists(TARGET_DIR):
        print(f"錯誤：找不到資料夾 '{TARGET_DIR}'。")
        return

    manifest = {
        "version": APP_VERSION,
        "files": {}
    }

    print(f"開始掃描資料夾 '{TARGET_DIR}'...")
    
    # 遞迴掃描資料夾內所有檔案
    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            # 計算相對路徑 (例如：tessdata/eng.traineddata)
            relative_path = os.path.relpath(file_path, TARGET_DIR).replace('\\', '/')
            
            file_hash = calculate_md5(file_path)
            file_size = os.path.getsize(file_path)
            
            if file_hash:
                manifest["files"][relative_path] = {
                    "hash": file_hash,
                    "size": file_size,
                    "url": f"{GITHUB_RAW_BASE_URL}/{relative_path}"
                }
                print(f"已加入: {relative_path} (大小: {file_size} bytes)")

    # 寫入 JSON 檔案
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=4, ensure_ascii=False)
        
    print(f"\n✅ 成功建立 {OUTPUT_FILE}！")
    print("請將此檔案上傳至 GitHub。")

if __name__ == "__main__":
    build_manifest()
