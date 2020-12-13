import csv


class Leaderboard:
    def __init__(self):
        self.create_if_not_exist()

    def create_if_not_exist(self):
        try:
            with open('score.csv', 'r'):
                pass
        except FileNotFoundError:
            with open('score.csv', 'w', newline=None) as f:
                csv.writer(f).writerow(('Username', 'Score'))

    def add_score(self, username, gold):
        with open('score.csv', 'a', newline=None) as f:
            csv.writer(f).writerow((username, gold))
        self.show_rank((username, gold))

    def get_scores(self):
        scores = []
        with open('score.csv', 'r') as f:
            for line in csv.reader(f):
                if line[1] == 'Score':
                    next
                else:
                    scores.append((line[0], int(line[1])))
        scores.sort(reverse=True, key=self.idx_one)
        return scores

    def show_rank(self, row):
        scores = self.get_scores()
        print(
            f'It is currently number {scores.index(row) + 1}'
            ' on the leaderboard')

    def print_top_x(self, x):
        scores = self.get_scores()
        if x > len(scores):
            x = len(scores)
        elif len(scores) == 0:
            print('There are no highscores yet')
            return

        for i in range(x):
            score = [scores[i][0], str(scores[i][1])]
            row = ', '.join(score)
            print(f'{i + 1} {row}')

    def idx_one(self, item):
        return item[1]
