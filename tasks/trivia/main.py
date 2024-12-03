from QuestionBank import QuestionBank
from Player import Player
from Game import Game
from questions import question_list

def start_game():
    """ Start the game by creating a new game object and adding players
    Returns:
        game: The game object
    """
    # Create a new question bank object
    questionBank = QuestionBank()

    # Get some user inputs for settings
    player_count = int(input("How many players are playing today? "))
    round_count = int(input("How many rounds would you like to play? "))

    # Add the questions to the question bank and randomize them
    for question in question_list:
        questionBank.add_question(question)
        questionBank.randomize_questions()

    # Create a new game object
    print("Welcome to the game!")
    game = Game(questionBank, round_count)
    
    # Add all players to the game
    for i in range(player_count):
        newPlayer = Player(i, str(input(f"Enter player {i+1} name: ")))
        game.add_player(newPlayer)

    return game


def finish_game(game):
    """ Finish the game and print the final scores
    Parameters:
        game (Game): The game object
    """
    print("==================================================")
    print("Game over!")
    print("Final scores:")
    game.get_state()


def play_round(game, player):
    """ Play a round of the game
    Parameters:
        game (Game): The game object
        player (Player): The player object
    Returns:
        bool: True if the game is still running
    """ 
    # Get a new question 
    question = game._questionBank.get_new_question()

    # Check if there are still questions available
    if question is None:
        print("No more questions available!")
        return False

    # Print the question and options
    print(question.get_question())
    for i, option in enumerate(question.get_options()):
        print(f"{i+1}. {option}")
    print("--------------------------------------------------")

    # Get the players answer
    answer = input("Enter the number of your answer: ")

    # Check if the answer is correct
    correct_answer, correct_option = question.check_answer(answer)

    # Print the result and add a point to the player's score if the answer is correct
    if correct_answer:
        print("- CORRECT! -")
        player.add_score()
    else:
        print("- INCORRECT -, sorry! The correct answer was: " + correct_option)
    game.next_round()

    return True


def main():
    game = start_game()

    # Play the game for the specified number of rounds
    for _ in range(game.get_round_count()):
        for player in game.get_players():
            try:
                game.get_state()
                print("--------------------------------------------------")
                ok = play_round(game, player)
                if not ok:
                    finish_game(game)
                    break

            # Exit the game if the user presses Ctrl+C
            except KeyboardInterrupt:
                finish_game(game)
                break

    # After all rounds were played, finish the game
    finish_game(game)


if __name__ == "__main__":
    main()
