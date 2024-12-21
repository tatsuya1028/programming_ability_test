# このファイルを使用してテストを行うこと
# 今回はpythonでお願いします
import csv
from datetime import datetime


class Teams:

    def __init__(self, path):
        self.path = path

    def read_csv(self):
        """一覧取得"""
        with open(self.path, encoding='utf8', newline='') as f:
            csvreader = csv.reader(f)
            row_list = [row for row in csvreader]

        header = row_list[0]
        rows_data = row_list[1:]
        teams_list = list(set([row[1] for row in rows_data]))
        sort_teams = sorted(teams_list)

        return header, rows_data, sort_teams
    

    def teams_calc(self):
        """各チーム毎の総得点、総失点、勝率を計算"""
        data = {}
        _, rows_data, teams_list = self.read_csv()

        for teams in teams_list:
            win = 0
            match_num = 0
            data[teams] = {
                'tatal': 0,
                'loss': 0,
                'win_rate': 0
            }
            for row in rows_data:
                if teams == row[1]:
                    match_num += 1
                    score = row[4].split('-')
                    data[teams]['tatal'] += int(score[0])
                    data[teams]['loss'] += int(score[1])
                    win += int(row[3])
            data[teams]['win_rate'] = win / match_num

        sorted_data = sorted(data.items(), key=lambda x:x[1]['win_rate'], reverse=True)

        for teams, stats in sorted_data:
            rate = '{:.2f}'.format(stats['win_rate'])
            print(teams, f'総得点: {stats["tatal"]} 総失点: {stats["loss"]} 勝率: {rate}')

    def a_league_only(self):
        """試合日が2024-01-05〜2024-03-05かつリーグがAリーグのみの一覧データと合計数"""
        header, rows_data, _ = self.read_csv()
        result = []
        result.append(header)
        for row in rows_data:
            if 'Aリーグ' == row[6] and datetime(2024, 1, 5) < datetime.strptime(row[0], '%Y-%m-%d') < datetime(2024, 3, 5):
                result.append(row)

        for i in result:
            print(*i)

    def winning_percentage_comparison(self):
        """各チームの「ホーム」と「アウェイ」での勝率を比較した一覧と勝率が最も高いチーム"""
        header, rows_data, sort_teams = self.read_csv()
        sorted_data_home, max_rate_home = self.win_rate_list(rows_data, sort_teams, "Home")
        sorted_data_away, max_rate_away = self.win_rate_list(rows_data, sort_teams, "Away")

        for (h_teams, h_stats), (a_teams, a_stats) in zip(sorted_data_home, sorted_data_away):
            print(h_teams, h_stats, a_teams, a_stats)

        m_ht, m_hr = max_rate_home
        mrt, m_rr = max_rate_away

        print("------------------------------------")

        print(m_ht, m_hr, mrt, m_rr)


    def win_rate_list(self, rows, teams_list, location):

        data = {}

        for teams in teams_list:
            win = 0
            match_num = 0
            data[teams] = {
                'win_rate': 0
            }
            for row in rows:
                if teams == row[1] and location == row[5]:
                    match_num += 1
                    win += int(row[3])
            data[teams]['win_rate'] = win / match_num

        sorted_data = sorted(data.items(), key=lambda x:x[0])
        max_rate = sorted(data.items(), key=lambda x:x[1]['win_rate'], reverse=True)
        
        return sorted_data, max_rate[0]


if __name__ == "__main__":
    teams: Teams = Teams('./test.csv')
    # for i in teams.read_csv():
    #     print(i)
    # teams.teams_calc()
    teams.a_league_only()
    teams.winning_percentage_comparison()
