# このファイルを使用してテストを行うこと
# 今回はpythonでお願いします
import csv


class Teams:

    def __init__(self, path):
        self.path = path

    def read_csv(self):
        """一覧取得"""
        row_list = []
        with open(self.path, encoding='utf8', newline='') as f:
            csvreader = csv.reader(f)
            row_list = [row for row in csvreader]

        return row_list

    def teams_calc(self):
        """各チーム毎の総得点、総失点、勝率を計算"""
        pass

    def a_league_only(self):
        """試合日が2024-01-05〜2024-03-05かつリーグがAリーグのみの一覧データと合計数"""
        pass

    def winning_percentage_comparison(self):
        """各チームの「ホーム」と「アウェイ」での勝率を比較した一覧と勝率が最も高いチーム"""
        pass


if __name__ == "__main__":
    teams = Teams('./test.csv')
    # for i in teams.read_csv():
    #     print(i)
    teams.teams_calc()
