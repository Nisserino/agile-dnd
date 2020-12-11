import csv
from csv import writer


class Leader_board:

    # Append/add player and set highscore to 0.
    def apnd_player(self):

        createnewplayer = input("Type your new name: ")

        def name_score_add(self):

            with open('score.csv', mode='a') as score_write:
                csv_writer = writer(score_write)
                csv_writer.writerow([createnewplayer, 0])
                score_write.close()
        name_score_add()

    # Create header username & highscore add player and 0 highscore

    def create_header_username_highscore(self):

        with open('score.csv', mode='a') as score_write:
            fieldnames = ['username', 'highscore']
            writer = csv.DictWriter(score_write, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'username': "kevin", 'highscore': 0})
    create_header_username_highscore()

    # To get the score of all players
    def get_score(self):

        with open('score.csv', 'r') as read_score:
            # reader = csv.reader(read_score)
            # next(reader)
            reader = csv.DictReader(read_score)
            rankone_highscore = [row['highscore'].split(",")[0] for row in reader]
            print(rankone_highscore)

    # Get the highest score of all the players

    def highest_score(self):

        with open('score.csv', 'r') as read_score:
            reader = csv.DictReader(read_score)
            rankone_highscore = [row['highscore'].split(",")[0:1] for row in reader]
            rankone = max(rankone_highscore)
            print(f"the highest score in this game is {rankone}")

    def sortsecond(val):
        return val[-1]
    with open('score.csv', 'r') as my_score:
        reader = csv.reader(my_score)
        for f in reader:
            data = list(reader)
            data.sort(reverse=True, key=sortsecond)
        print(data[0])
        print(f"the player with the highest score in this game is:{data[0]}")
