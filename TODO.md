# TODO - 優化任務追蹤

##  Completed

### 高優先級
- [x] 修復 debug=True 寫死問題 - 改為環境變數控制
- [x] 強化 Secret Key 配置 - 移除預設金鑰、改用強隨機
- [x] 加入檔案讀取錯誤處理 - get_cards() 加入 try-except
- [x] 加入 CSRF 保護 - 使用 Flask-WTF
- [x] 新增 CSRF token 到 result.html 表單

### 中優先級
- [x] 建立自訂錯誤頁面 - 404/500 錯誤處理
- [x] 加入速率限制 - Flask-Limiter 限制抽卡頻率
- [x] 配置日誌記錄 - 統一 log 格式與輸出
- [x] 加入 ARIA 屬性到 result.html
- [x] 加入 ARIA 屬性到 history.html

### 低優先級
- [x] 建立測試目錄 - pytest 單元測試
- [x] 建立 Dockerfile - 容器化部署
- [x] 優化前端無障礙 - 加入 ARIA 屬性
- [x] 優化前端響應式 - CSS 行動裝置優化
- [x] 加入 SEO meta 標籤到 base.html
- [x] 建立 robots.txt

## Pending

- (none)
