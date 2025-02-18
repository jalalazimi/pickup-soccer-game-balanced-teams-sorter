# Pickup Soccer Game Balanced Teams Sorter

This project aims to create balanced teams for a pickup soccer game based on player ratings. The script reads player data from a CSV file, sorts players into teams, and optimizes the team composition to minimize the difference in average ratings between the best and worst teams.

## Files

- `pickup_soccer_team_sorter.py`: The main script that sorts and optimizes the teams.
- `PlayersRatings.csv`: The CSV file containing player information and ratings.

## Usage

1. Ensure you have Python and the required libraries installed:
    ```sh
    pip install pandas
    ```

2. Place your player data in the `PlayersRatings.csv` file. The file should have the following columns:
    - `player`: The name of the player.
    - `rating`: The rating of the player.
    - `is_going`: Whether the player is attending the game (1 for yes, 0 for no).
    - `is_captain`: Whether the player is a captain (1 for yes, 0 for no).
    - `is_goalkeeper`: Whether the player is a goalkeeper (1 for yes, 0 for no).

3. Run the script:
    ```sh
    python pickup_soccer_team_sorter.py
    ```

4. The script will print the initial and optimized team compositions along with their average ratings and the difference between the best and worst teams.

## Example

An example `PlayersRatings.csv` file is provided with the project. You can modify it to include your own player data.

## License

This project is licensed under the MIT License.