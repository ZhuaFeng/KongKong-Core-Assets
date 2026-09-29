---

## 📂 專案目錄結構 (Directory Structure)

本專案採用「程式邏輯」與「使用者資料」完全分離的架構。主程式可隨意移動，所有核心依賴與玩家資料皆動態生成於使用者的 `Documents` (我的文件) 中。

### 1. 原始碼與開發目錄 (Source / PyInstaller Build)

此區塊為 GitHub 上的原始碼結構，打包時會被封裝進 `.exe` 中：

```text
KongKongAssistant.exe/
├── main.py                  # 程式啟動入口 (含單一實例鎖與防護)
├── app_controller.py        # 系統大腦與資料流總管
├── vision_engine.py         # 多執行緒背景 OCR 與圖形比對引擎
├── hud_window.py            # 四路物理排版 HUD 視窗引擎
├── ui_components.py         # 客製化 UI 元件庫
├── catch_img/               # OpenCV 模板匹配圖資 (EXP/Meso/HP/MP 圖示)
├── buffs/                   # 各職業 BUFF 技能圖示庫
├── sounds/                  # 系統預設警報音效庫 (alert.wav 等)
└── icon.ico                 # 應用程式圖示

```

### 2. 使用者運行目錄 (Runtime Data Directory)

位於 `C:\Users\{使用者}\Documents\KongKongAssistant\`。此資料夾由程式在首次啟動時自動建立，用來存放熱更新引擎、設定檔與快取資料：

```text
KongKongAssistant/
├── settings.json            # 玩家主設定檔 (UI/開關/自訂座標)
├── music_settings.json      # 音樂播放器專屬設定 (EQ/歌單/音量)
├── scale_cache.json         # 盲搜比例快取 (加速影像辨識用)
├── obs_hud.html             # 自動釋放的 OBS 實況主專用 Web 面板
├── obs_config.js            # 動態生成的 WebSocket Port 橋接檔
├── logs/                    
│   └── history.csv          # 玩家歷史戰績存檔
├── sounds/                  # 玩家動態音訊庫
│   ├── user_audio/          # 玩家自訂與裁切的音效檔
│   ├── tts_cache/           # Google 小姐 TTS 背景快取 (定期清理)
│   ├── music_library/       # 本地 YouTube 音樂庫 (受容量控管)
│   └── stream_cache/        # 音樂無縫播放的暫存區
└── core_engine/             # ⚠️ 系統自動從雲端下載的核心引擎
    ├── tessdata/            # Tesseract OCR 語言包
    ├── vlc/                 # VLC 播放器 DLL 依賴
    ├── ffmpeg.exe           # 音訊轉碼器
    ├── deno.exe             # YouTube JS 破解引擎
    └── WgcEngine.dll        # 高幀率無邊框截圖引擎

```

---

## ⌨️ 預設快捷鍵一覽 (Default Hotkeys)

系統支援全域熱鍵 (Global Hotkeys)，在遊戲內也可直接觸發。所有熱鍵皆可在「⚙️設定 -> 快捷鍵」中自訂。

| 快捷鍵 | 功能說明 |
| --- | --- |
| `F9` | **▶️ 開始 / 暫停** 追蹤計算 |
| `F10` | **🔄 重置** 所有當前數據 |
| `F11` | **👁️ 顯示 / 隱藏** HUD 面板 |
| `F12` | **🪟 視窗重置** (依照設定檔 Resize 遊戲視窗) |
| `F7` | **🎵 播放 / 暫停** 音樂 |
| `F6` / `F8` | **⏮ 上一首 / ⏭ 下一首** |
| `PageDown` | **✨ 手動同步** 當前畫面上的 BUFF 狀態 |

---
