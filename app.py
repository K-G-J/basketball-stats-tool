from constants import TEAMS, PLAYERS
import copy
import random

print("\n 🏀 BASKETBALL TEAM STATS TOOL 🏀")

"""
Extra Credit
To get an "exceeds" rating, complete all of the steps below:

1.  Cleaning guardian field
    When cleaning the data, clean the guardian field as well before adding it into your newly created collection, split up the guardian string into a List.

    NOTE: There can be more than one guardian, indicated by the " and " between their names.

2.  Additional balancing to the team
    Additionally, balance the teams so that each team has the same number of experienced vs. inexperienced players.

    If this is done correctly each team stats should display the same number count for experienced total and inexperienced total as well as the same total number of players on the team.

3.  Include additional stats for a given displayed team:
    number of inexperienced players on that team
    number of experienced players on that team
    the average height of the team
    the guardians of all the players on that team (as a comma-separated string)
    HINT: You can calculate the average height for a given team by keeping a running sum total of each players height on the team and dividing that total by the total number of players on that team.

4.  Quit Menu Option
    The user should be re-prompted with the main menu until they decide to "Quit the program".
"""


def show_menu():
    while True:
        try:
            print(
                "\n ---- MENU ---- \n Here are your choices: \n 1) Display Team Stats\n 2) Quit\n")
            choice = int(input("Please enter an option:  "))
        except ValueError as err:
            # Handle invalid input
            print(
                f"\n❗️ Please select either 1 or 2 from the options\n({err})\n")
            continue
        if choice != 1 and choice != 2:
            # Handle invalid input
            print(
                f"\n❗️ Please select either 1 or 2 from the options\n")
        return choice


def clean_data(data):
    cleaned_data = []
    # Read player data and deep copy to not change the original
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
    # Randomize the players distributed to each team
    random.shuffle(cleaned_data)

    # Balance the players across the three teams: Panthers, Bandits and Warriors
    num_players_team = int(len(PLAYERS) / len(TEAMS))
    panthers = cleaned_data[:num_players_team]
    bandits = cleaned_data[num_players_team: num_players_team * 2]
    warriors = cleaned_data[num_players_team * 2:]

    # Make sure the teams have the same number of total players on them when function has finished
    if len(panthers) != len(bandits) != len(warriors):
        print(f"""
            Oops 😕 ... the teams are not balanced
            Panthers: {len(panthers)} players
            Bandits: {len(bandits)} players
            Warriors: {len(warriors)} players
            """)
        return
    # Make sure the teams are unique
    assert [i for i in panthers if i not in bandits if i not in warriors] != [
    ], "Oops 😕 ... The teams have overlapping players"

    return panthers, bandits, warriors


def pick_team():
    while (team_choice := int(input(
            "\n Please enter a team option:\n 1) Panthers\n 2) Bandits\n 3) Warriors\n"))) != 1 and team_choice != 2 and team_choice != 3:
        # Handle invalid input
        print('\n❗️ Please enter a team option of 1, 2, or 3')
    return team_choice


def display_stats(team_name, team):
    # Display team name
    heading = f"🏀 Team: {team_name} Stats 🏀"
    print(f"\n{heading}\n{'-' * (len(heading) + 2)}\n")

    # Get variables to calculate stats
    total_heights = 0
    experienced_players = []
    player_names = []
    gaurdian_names = []
    for player in team:
        if player['experience'] == True:
            experienced_players.append(player)
        total_heights += player['height']
        player_names.append(player['name'])
        gaurdian_names.append(player['guardians'])

    # Format and display stats
    print(f"""
        Total Players: {len(team)}
        Total Experienced: {len(experienced_players)}
        Total Inexperienced: {len(team) - len(experienced_players)}
        Average Height: {round(total_heights / len(team), 2)}
        
        Players on Team: 
        {', '.join(player_names)}
        
        Gaurdians:
        {', '.join(gaurdian_names)}
        
        """)


def main():
    try:
        (panthers, bandits, warriors) = balance_teams()
    except AssertionError as err:
        print(f"\n{err}\n")
    except:
        print("\n Ooops 😕 ... something went wrong, please try again")

    while (choice := show_menu()) != 2:
        # Handle display stats
        if choice == 1:
            team = pick_team()
            # 1 = Panthers      2 = Bandits     3 = Warriors
            if team == 1:
                display_stats("Panthers", panthers)
            elif team == 2:
                display_stats("Bandits", bandits)
            else:
                display_stats("Warriors", warriors)

            while input("Press ENTER to continue...") != "":
                continue
    else:
        # Handle quit
        print("\nThank you for using the basketball stats tool! 👋\n")
        return


if __name__ == "__main__":
    main()
