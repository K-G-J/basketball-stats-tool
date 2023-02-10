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


def main():
    clean_data(PLAYERS)


if __name__ == "__main__":
    main()
