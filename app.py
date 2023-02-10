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


"""
Console readability matters
When the menu or stats display to the console, it should display in a nice readable format. Use extra spaces or line breaks ('\n') to break up lines if needed. For example, '\nThis will start on a newline.'

Displaying the stats
When displaying the selected teams' stats to the screen you will want to include:

Team's name as a string
Total players on that team as an integer
The player names as strings separated by commas
NOTE: When displaying the player names it should not just display the List representation object. It should display them as if they are one large comma separated string so the user cannot see any hints at what data type players are held inside.
"""

def main():
    (panthers, bandits, warriors) = balance_teams()


if __name__ == "__main__":
    main()
