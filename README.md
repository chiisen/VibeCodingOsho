# VibeCodingOsho

基於 Flask 的「奧修禪卡線上占卜」示範專案。

![Osho01](./images/Osho01.jpg)

## 本地執行

1. 建議使用虛擬環境（venv 或 Conda）。
2. 安裝依賴：

```bash
pip install -r requirements.txt
```

3. 啟動開發伺服器：

```bash
python app.py
```

4. 瀏覽 `http://127.0.0.1:5000`。

## 結構

- `app.py`：Flask 應用與路由
- `templates/`：Jinja 模板（`base.html`、`index.html`、`result.html`、`history.html`）
- `static/css/styles.css`：基本樣式
- `data/cards.json`：卡牌資料

## 設定

- 以 `FLASK_SECRET_KEY` 覆蓋預設金鑰於生產環境。

