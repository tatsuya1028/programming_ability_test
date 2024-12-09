# このファイルを使用してテストを行うこと
# 今回はpythonでお願いします
import csv
from datetime import datetime as dt
import datetime


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
        teams_list = []
        data = {}
        rows = self.read_csv()
        # ヘッダーをスキップ
        rows = rows[1:]
        teams_list = list(set([row[1] for row in rows]))
        for teams in teams_list:
            win = 0
            match_number = 0
            data[teams] = {
                'total': 0,
                'loss': 0,
                'win_rate': 0
            }
            for row in rows:
                if teams == row[1]:
                    match_number += 1
                    score = row[4].split('-')
                    data[teams]['total'] += int(score[0])
                    data[teams]['loss'] += int(score[1])
                    if row[3] == '1':
                        win += 1
            data[teams]['win_rate'] = win / match_number

        sorted_data = sorted(data.items(), key=lambda x: x[1]["win_rate"], reverse=True) # noqa

        for team, stats in sorted_data:
            rate = '{:.2f}'.format(stats["win_rate"])
            print(team, f'総得点: {stats["total"]} 総失点: {stats["loss"]} 勝率: {rate}') # noqa

    def a_league_only(self):
        """試合日が2024-01-05〜2024-03-05かつリーグがAリーグのみの一覧データと合計数"""
        rows = self.read_csv()
        # ヘッダーをスキップ
        header = rows[0]
        rows = rows[1:]
        result = [header]
        for row in rows:
            if datetime.datetime(2024, 1, 5) < dt.strptime(row[0], '%Y-%m-%d') < datetime.datetime(2024, 3, 5) and row[6] == "Aリーグ": # noqa
                result.append(row)

        for i in result:
            print(*i)

    def winning_percentage_comparison(self):
        """各チームの「ホーム」と「アウェイ」での勝率を比較した一覧と勝率が最も高いチーム"""
        rows = self.read_csv()[1:]
        teams_list = list(set([row[1] for row in rows]))
        home, max_home = self.win_rate_list(rows, teams_list, "Home")
        away, max_away = self.win_rate_list(rows, teams_list, "Away")

        print("Homeの勝率一覧     |  Awayの勝率一覧")
        print("------------------------------------------")
        for (team_h, stats_h), (team_a, stats_a) in zip(home, away):
            rate_h = '{:.2f}'.format(stats_h["win_rate"])
            rate_a = '{:.2f}'.format(stats_a["win_rate"])
            print(f'{team_h}, 勝率: {rate_h} | {team_a}, 勝率: {rate_a}') # noqa
        max_rate_h = '{:.2f}'.format(max_home[1]["win_rate"])
        away_rate_a = '{:.2f}'.format(max_away[1]["win_rate"])
        print()
        print("HomeとAwayの中で最も勝率の高いチーム")
        print("------------------------------------------")
        print(f'{max_home[0]}, 勝率: {max_rate_h} | {max_away[0]}, 勝率: {away_rate_a}') # noqa

    def win_rate_list(self, rows, teams_list, location):
        """場所での勝率一覧算出"""
        data = {}
        for teams in teams_list:
            win = 0
            match_number = 0
            data[teams] = {
                'win_rate': 0
            }
            for row in rows:
                if teams == row[1] and location == row[5]:
                    match_number += 1
                    if row[3] == '1':
                        win += 1
            data[teams]['win_rate'] = win / match_number

        sorted_data = sorted(data.items(), key=lambda x: x) # noqa
        max_rate = sorted(data.items(), key=lambda x: x[1]["win_rate"], reverse=True) # noqa

        return sorted_data, max_rate[0]


if __name__ == "__main__":
    teams = Teams('./test.csv')
    # for i in teams.read_csv():
    #     print(i)
    # teams.teams_calc()
    teams.winning_percentage_comparison()
