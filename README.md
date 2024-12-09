## プログラミング能力テスト

### 課題
- csvファイルを読み込み、指定条件の内容を抽出すること

### 以下の条件を抽出　※答も掲載済み
- 条件1：全ての試合一覧データ
```bash
python ability_test.py

試合日 チーム名 対戦チーム名 勝利 点数 試合場所 リーグ
2024-01-01 Team A Team D 1 4-0 Home Bリーグ
2024-01-04 Team B Team D 1 5-0 Home Aリーグ
2024-01-08 Team C Team A 1 3-0 Away Aリーグ
2024-01-10 Team D Team A 0 0-1 Away Aリーグ
2024-01-15 Team E Team B 1 4-0 Home Aリーグ
2024-01-17 Team A Team D 1 3-2 Away Aリーグ
2024-01-18 Team B Team E 1 5-1 Home Bリーグ
2024-01-20 Team C Team A 0 4-5 Away Bリーグ
2024-01-21 Team D Team C 0 0-4 Away Bリーグ
2024-01-22 Team E Team D 0 1-2 Away Bリーグ
2024-01-25 Team A Team B 1 1-0 Home Aリーグ
2024-01-28 Team B Team D 1 1-0 Away Bリーグ
2024-01-30 Team C Team A 0 0-5 Home Aリーグ
2024-02-03 Team D Team C 0 1-3 Home Bリーグ
2024-02-05 Team E Team C 0 2-5 Home Bリーグ
2024-02-08 Team A Team D 0 0-1 Away Bリーグ
2024-02-10 Team B Team C 0 0-0 Away Bリーグ
2024-02-14 Team C Team A 0 3-5 Home Aリーグ
2024-02-19 Team D Team B 1 3-0 Away Aリーグ
2024-02-22 Team E Team B 1 5-2 Away Aリーグ
2024-02-25 Team A Team C 0 2-5 Away Bリーグ
2024-02-28 Team B Team A 0 2-2 Home Bリーグ
2024-03-06 Team C Team D 1 2-1 Away Aリーグ
2024-03-10 Team D Team A 0 1-4 Home Aリーグ
2024-03-12 Team E Team D 0 1-1 Away Aリーグ
2024-03-16 Team A Team D 0 1-5 Home Bリーグ
2024-03-18 Team B Team D 1 5-3 Home Bリーグ
2024-03-20 Team C Team E 0 3-4 Home Bリーグ
2024-03-22 Team D Team B 1 5-4 Home Aリーグ
2024-03-24 Team E Team A 0 0-0 Home Bリーグ
2024-03-25 Team A Team D 0 4-4 Away Aリーグ
2024-03-27 Team B Team A 0 3-3 Away Bリーグ
2024-03-29 Team C Team E 1 3-2 Away Aリーグ
2024-03-30 Team D Team E 0 4-4 Away Bリーグ
2024-03-31 Team E Team D 1 4-2 Away Aリーグ
2024-04-08 Team A Team E 0 2-5 Away Bリーグ
2024-04-10 Team B Team E 0 0-1 Home Bリーグ
2024-04-12 Team C Team B 0 3-3 Home Aリーグ
2024-04-13 Team D Team E 0 0-1 Away Bリーグ
2024-04-15 Team E Team D 0 2-5 Away Bリーグ
2024-04-16 Team A Team E 0 3-5 Home Bリーグ
2024-04-19 Team B Team C 1 4-1 Away Bリーグ
2024-04-20 Team C Team D 0 1-5 Away Aリーグ
2024-04-21 Team D Team A 0 1-4 Home Aリーグ
2024-04-24 Team E Team A 1 3-1 Away Aリーグ
2024-04-26 Team A Team E 0 3-3 Away Aリーグ
2024-04-28 Team B Team C 0 4-5 Away Aリーグ
2024-04-30 Team C Team D 0 2-2 Home Bリーグ
```
- 条件2：各チーム毎の総得点、総失点、勝率を計算
```bash
python ability_test.py

Team B 総得点: 29 総失点: 16 勝率: 0.50
Team E 総得点: 22 総失点: 18 勝率: 0.44
Team C 総得点: 24 総失点: 32 勝率: 0.30
Team A 総得点: 23 総失点: 30 勝率: 0.30
Team D 総得点: 15 総失点: 25 勝率: 0.22
```
- 条件3：試合日が2024-01-05〜2024-03-05かつリーグがAリーグのみの一覧データと合計数
```bash
python ability_test.py

試合日 チーム名 対戦チーム名 勝利 点数 試合場所 リーグ
2024-01-08 Team C Team A 1 3-0 Away Aリーグ
2024-01-10 Team D Team A 0 0-1 Away Aリーグ
2024-01-15 Team E Team B 1 4-0 Home Aリーグ
2024-01-17 Team A Team D 1 3-2 Away Aリーグ
2024-01-25 Team A Team B 1 1-0 Home Aリーグ
2024-01-30 Team C Team A 0 0-5 Home Aリーグ
2024-02-14 Team C Team A 0 3-5 Home Aリーグ
2024-02-19 Team D Team B 1 3-0 Away Aリーグ
2024-02-22 Team E Team B 1 5-2 Away Aリーグ
```
- 条件4：各チームの「ホーム」と「アウェイ」での勝率を比較した一覧と勝率が最も高いチーム
```bash
python ability_test.py

Homeの勝率一覧     |  Awayの勝率一覧
------------------------------------------
Team A, 勝率: 0.50 | Team A, 勝率: 0.17
Team B, 勝率: 0.60 | Team B, 勝率: 0.40
Team C, 勝率: 0.00 | Team C, 勝率: 0.60
Team D, 勝率: 0.25 | Team D, 勝率: 0.20
Team E, 勝率: 0.33 | Team E, 勝率: 0.50

HomeとAwayの中で最も勝率の高いチーム
------------------------------------------
Team B, 勝率: 0.60 | Team C, 勝率: 0.60
```