import pandas as pd
import random

def find_teams(guess, df):
    teams = []
    for i in range(1, max(guess) + 1):
        indexes_team = [index for index, value in enumerate(guess) if value == i]
        team = df.loc[indexes_team].copy()
        teams.append(team)
    
    avgs = [team["rating"].mean() for team in teams]
    max_diff = max(avgs) - min(avgs)
    return teams, max_diff

def print_teams(teams, max_diff):
    for i, team in enumerate(teams, start=1):
        team["aux"] = team["player"] + " (" + team["rating"].astype(str) + ")"
        print(f"Team {i}: {team['aux'].values}")
        print(f"Average team {i}: {team['rating'].mean():.2f}")
    
    print(f"Diff best vs worst team: {max_diff:.2f}")

def is_valid_team(team):
    num_captains = team['is_captain'].sum()
    num_goalkeepers = team['is_goalkeeper'].sum()
    return num_captains <= 2 and num_goalkeepers >= 2

def main():
    # Read CSV and filter players
    df = pd.read_csv('PlayersRatings.csv')
    df = df.loc[df['is_going'] == 1].copy()

    # Shuffle groups of players by rating, then sort
    groups = [group.copy() for _, group in df.groupby('rating')]
    random.shuffle(groups)
    df = pd.concat(groups).reset_index(drop=True)
    df = df.sort_values(by='rating', ascending=False).reset_index(drop=True)

    num_players = len(df)
    num_teams = (num_players + 4) // 5  # Ensure each team has exactly 5 members
    initial_guess = [i % num_teams + 1 for i in range(num_players)]
    team1, max_diff = find_teams(initial_guess, df)

    print("Initial Solution:\n")
    print_teams(team1, max_diff)

    new_guess = initial_guess.copy()
    best_guess = initial_guess.copy()
    max_diff_best = max_diff
    max_diff_list = [max_diff]
    max_trials = 10000
    count = 0

    while count < max_trials and max_diff_best > 0:
        random.shuffle(new_guess)
        teams, new_max_diff = find_teams(new_guess, df)
        if all(is_valid_team(team) for team in teams):
            max_diff_list.append(new_max_diff)
            if new_max_diff < max_diff_best:
                max_diff_best = new_max_diff
                best_guess = new_guess.copy()
        count += 1

    # Optional: Uncomment the following lines to plot a histogram of max_diff values
    # import matplotlib.pyplot as plt
    # pd.DataFrame({"data": max_diff_list}).plot(kind='hist')
    # plt.show()

    print("\nOptimized Solution:\n")
    teams_best, max_diff_best = find_teams(best_guess, df)
    print_teams(teams_best, max_diff_best)

if __name__ == "__main__":
    main()