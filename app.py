from constants import TEAMS, PLAYERS
import copy
import random
import keyboard


# Assign team name constants
TEAM_1 = TEAMS[0].title()
TEAM_2 = TEAMS[1].title()
TEAM_3 = TEAMS[2].title()


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
    # Get experienced and inexperienced list to balance teams
    experienced_list = []
    inexperienced_list = []
    # Read player data and deep copy to not change the original
    # A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.
    for player in copy.deepcopy(data):
        (height,) = tuple(player['height'].split()[:-1])
        # Save height as an integer
        player['height'] = int(height)

        # Save experience as a boolean value
        if player['experience'] == 'YES':
            player['experience'] = True
            experienced_list.append(player)
        else:
            player['experience'] = False
            inexperienced_list.append(player)
        """
        TODO: Cleaning guardian field
        When cleaning the data, clean the guardian field as well before adding it into your newly created collection, split up the guardian string into a List.

        NOTE: There can be more than one guardian, indicated by the " and " between their names.
        """

        # Save cleaned player data to a new collection
        cleaned_data.append(player)

    # Return new collection of cleaned player data
    return cleaned_data, experienced_list, inexperienced_list


def balance_teams():
    (cleaned_data, experienced_list, inexperienced_list) = clean_data(PLAYERS)
    # Check equality
    if len(experienced_list) + len(inexperienced_list) != len(cleaned_data):
        raise ValueError("❗️ The teams cannot be balanced\n")
    # Randomize the players distributed to each team
    random.shuffle(experienced_list)
    random.shuffle(inexperienced_list)

    # Make sure equal number of experienced and inexperienced players
    num_players_team = int(len(PLAYERS) / len(TEAMS))
    num_experienced_players = int(len(experienced_list) / len(TEAMS))
    num_inexperienced_players = int(len(inexperienced_list) / len(TEAMS))
    if num_experienced_players != num_inexperienced_players:
        print(f"""
            Oops 😕 ... there are unequal experienced and inexperienced players
            {num_experienced_players} experienced players
            {num_inexperienced_players} inexperienced players
            """)
        return

    # Balance the players across the three teams
    # Each team has the same number of experienced and inexperienced players.
    team_1 = experienced_list[:num_experienced_players] + \
        inexperienced_list[:num_inexperienced_players]
    team_2 = experienced_list[num_experienced_players: num_experienced_players * 2] + \
        inexperienced_list[num_inexperienced_players: num_inexperienced_players * 2]
    team_3 = experienced_list[num_experienced_players * 2:] + \
        inexperienced_list[num_inexperienced_players * 2:]

    # Make sure the teams have the same number of total players on them when function has finished
    if not len(team_1) == len(team_2) == len(team_3) == num_players_team:
        print(f"""
            Oops 😕 ... the teams are not balanced
            {TEAM_1}: {len(team_1)} players
            {TEAM_2}: {len(team_2)} players
            {TEAM_3}: {len(team_3)} players
            """)
        return

    # Make sure the teams are unique
    assert [i for i in team_1 if i not in team_2 if i not in team_3] != [
    ], "Oops 😕 ... The teams have overlapping players"

    return team_1, team_2, team_3


def pick_team():
    while (team_choice := int(input(
            f"\n Please enter a team option:\n 1) {TEAM_1}\n 2) {TEAM_2}\n 3) {TEAM_3}\n"))) != 1 and team_choice != 2 and team_choice != 3:
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
    """
    TODO: Include additional stats for a given displayed team:
    number of inexperienced players on that team
    number of experienced players on that team
    the average height of the team
    the guardians of all the players on that team (as a comma-separated string)
    HINT: You can calculate the average height for a given team by keeping a running sum total of each players height on the team and dividing that total by the total number of players on that team.
    """
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

    print("\n 🏀 BASKETBALL TEAM STATS TOOL 🏀")

    try:
        (team_1, team_2, team_3) = balance_teams()
    except AssertionError as err:
        print(f"\n{err}\n")
    except:
        print("\n Ooops 😕 ... something went wrong, please try again")

    """
    TODO: Quit Menu Option
    The user should be re-prompted with the main menu until they decide to "Quit the program".
    """
    while (choice := show_menu()) != 2:
        # Handle display stats
        if choice == 1:
            team = pick_team()
            if team == 1:
                display_stats(TEAM_1, team_1)
            elif team == 2:
                display_stats(TEAM_2, team_2)
            else:
                display_stats(TEAM_3, team_3)

            # TODO: fix to use read_key
            while input("Press ENTER to continue...") != "":
                continue
            # while True:
            #     input("Press ENTER to continue...")
            #     if keyboard.read_key() != "enter":
            #         continue
            #     else:
            #         break
    else:
        # Handle quit
        print("\nThank you for using the basketball stats tool! 👋\n")
        return


if __name__ == "__main__":
    main()
