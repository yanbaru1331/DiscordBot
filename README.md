# GDF Discord BOT
ソシャゲマルチ募集用discord bot
## 環境
```
Ubuntu 20.04
python 3.11
```

## 使い方
```bash
docker build -t 任意のイメージ名 .
docker compose build --no-cache
docker compose up -d
docker container ps
docker exec -it 控えたCONTAIENR ID bash
```

```bash
cd ./scr
python3.11 main.py
```

## コマンド一覧
```
/マルチ募集
マルチ募集コマンド　クエスト、日時を入力
参加者は参加属性のリアクションを押す

/spbh
クエスト入力省略版
参加者側の使用方法は上記と同一

/spbh_date
放置狩りスケジュール調整コマンド　日付を入力
入力された日付から1週間のカレンダーを出力
参加者は参加する曜日のスタンプを押す
```
