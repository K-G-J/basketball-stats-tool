from constants import TEAMS, PLAYERS
import copy


def clean_data(data):
    cleaned_data = []
    # Read player data and copy to not change the original
    # A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.
    for player in copy.deepcopy(data):
        (height,) = tuple(player['height'].split()[:-1])
        # Save height as an integer
        player['height'] = int(height)

        # Save experience as a boolean value
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False

        # Save cleaned player data to a new collection
        cleaned_data.append(player)

    # Return new collection of cleaned player data
    return cleaned_data


def balance_teams():
    cleaned_data = clean_data(PLAYERS)
    # Balance the players across the three teams: Panthers, Bandits and Warriors
    num_players_team = int(len(PLAYERS) / len(TEAMS))
    panthers = cleaned_data[:num_players_team]
    bandits = cleaned_data[num_players_team: num_players_team * 2]
    warriors = cleaned_data[num_players_team * 2:]
    # Make sure the teams have the same number of total players on them when function has finished
    if len(panthers) != len(bandits) != len(warriors):
        print(f"""
            Oops...the teams are not balanced
            Panthers: {len(panthers)} players
            Bandits: {len(bandits)} players
            Warriors: {len(warriors)} players
            """)
        return
    # Make sure the teams are unique
    if panthers in bandits in warriors:
        print("Oops...The teams have overlapping players")
        return
    return panthers, bandits, warriors


def main():
    balance_teams()


if __name__ == "__main__":
    main()
