# PRISON-RIOT

Continuing the development of the `PRISON RIOT`

1. **Prison Layout Design**: Develop classes or functions to create the prison layout. This includes cells, walls, guard posts, and other infrastructure.

2. **Character Development**: Create character classes for inmates and guards, including attributes like health, behavior, and movement.

3. **Escape Mechanics**: Implement logic for inmates attempting to escape, such as finding paths, avoiding guards, and using tools.

4. **Riot and Emergency Mechanics**: Code for riot scenarios, including AI for non-player characters like guards and inmates, crowd behavior, and responses to player actions.

5. **Combat System**: Design a simple combat system, possibly turn-based or real-time, depending on your game design.

6. **Graphics and Animation**: Use Pygame's capabilities to load and display sprites, animate characters, and render the game environment.

7. **User Interface (UI)**: Develop a UI to display important game information like health bars, score, and instructions.

8. **Game Loop Enhancements**: Refine the main game loop with event handling, updates to game state, and rendering.

9. **Sound Effects and Music**: Integrate background music and sound effects for actions and events.

10. **Testing and Debugging**: Regularly test the game for bugs and performance issues, making necessary adjustments.

## Forbidden Escape - A Prison Riot Game

There are several methods defined that handle different aspects of the gameplay:

*  `__init__()` initializes the game objects.

*  `display_intro()` displays the introductory message to the player.

*  `make_choice()` allows the user to choose between given options by entering their chosen number.

*  `talk_to_aria()` lets the player interact with the AI character Aria. Their level of trust determines how much information Aria shares. This interaction also affects the player’s sanity and strengthens their relationship with Aria.

*  `explore_cell()` allows the player to search their cell and potentially find useful items that can increase their evidence count and possibly aid them in finding the key.

*  `rest()` enables the player to rest, which increases their sanity.

*  `check_status()` shows the current state of the game including the day number, remaining sanity, collected evidence, relationship with Aria, and whether they possess the key.

*  `random_event()` generates a randomly selected event each day, adding more dynamic elements to the gameplay.

*  `solve_puzzle()` presents the player with a puzzle to solve. If they correctly answer it (echo), they unlock a hidden passage and gain additional evidence.

*  `progress_day()` advances the game to the next day, decreases the player’s sanity, triggers another random event, and updates any necessary variables.

Interactive story-driven adventure game with elements of exploration, puzzles, and building relationships, while navigating through the challenges of imprisonment.
