import numpy as np


class Game:

    WIDTH, HEIGHT = 8, 8

    def __init__(self):
        self.array = np.zeros((Game.HEIGHT, Game.WIDTH), dtype=int)
        self.ones_positions = self.generate_20_ones()
        self.blind_array = np.full((Game.HEIGHT, Game.WIDTH), '_')
        self.used_positions = []
        self.num_of_ones = 0
        self.guesses = 0

    @staticmethod
    def generate_20_ones():
        ones = []
        while len(ones) <= 20:
            elem = (np.random.randint(0, Game.WIDTH), np.random.randint(0, Game.HEIGHT))
            if elem not in ones:
                ones.append(elem)
        return ones

    def print_board(self):
        print(self.blind_array)

    def print_attempts(self, attempts):
        print(f'{attempts} attempts')

    def check_win(self):
        return self.num_of_ones == 20

    def check_input(self, user_input):
        return 1 <= user_input <= 8

    def get_user_input(self, prompt):
        while True:
            try:
                user_input = input(prompt)
                if user_input == '0':
                    return 0
                user_input = int(user_input)
                if self.check_input(user_input):
                    return user_input
                print('Invalid input. Please enter a valid number between 1 and 8.')
            except ValueError:
                print('Invalid input. Please enter a valid number between 1 and 8.')

    def play(self, attempts):
        try:
            for x, y in self.ones_positions:
                self.array[x, y] = 1

            while attempts > 0:
                self.print_board()
                self.print_attempts(attempts)
                print("---------------------------------------")
                x = self.get_user_input('To exit, enter 0. Enter a row (1 to 8): ')
                if x == 0:
                    break
                y = self.get_user_input('To exit, enter 0. Enter a column (1 to 8): ')
                if y == 0:
                    break
                if (x, y) not in self.used_positions:
                    self.used_positions.append((x, y))
                    if self.array[x - 1, y - 1] == 1:
                        self.blind_array[x - 1, y - 1] = 1
                        self.num_of_ones += 1
                        self.guesses += 1
                        if self.guesses == 2:
                            self.guesses = 0
                            attempts += 1
                    else:
                        self.blind_array[x - 1, y - 1] = 0
                        self.guesses = 0
                        attempts -= 1
                else:
                    print('Try again. You have already chosen this position')
                if self.check_win():
                    print('Congrats, you have won. You are the genius')
                    break

            self.print_attempts(attempts)
            print('Not your day buddy, you lost')

        except Exception:
            print('Game failed - Invalid input. Please enter a valid row and column.')


class MainGame:
    @staticmethod
    def description():
        print("""
        ##################################################################################
        Vladislav Zabrovsky, K-23 - Where is the 1 hidden?.
        Array with shape (8,8) generated randomly and filled with 1 or 0.
        The number of generated 1 is 20. You win if you manage to guess every 1 in a stack.
        GG;)
        ##################################################################################
        """)

    @staticmethod
    def print_options(options):
        print('Options:')
        for key, value in options.items():
            print(f"{key} - {value} attempts")
        print('To leave the game, enter 0')

    def main(self):
        difficulty_level = {'easy': 40, 'medium': 30, 'hard': 20, 'insane': 8}

        while True:
            self.description()
            self.print_options(difficulty_level)

            choosing_dif = input('Please choose a difficulty: ').strip().lower()

            if choosing_dif in difficulty_level:
                attempts = difficulty_level[choosing_dif]
                game_instance = Game()
                game_instance.play(attempts)
            elif choosing_dif == '0':
                break
            else:
                print('Invalid option, try again')

        print('Goodbye my dear friend')


if __name__ == "__main__":
    main_game = MainGame()
    main_game.main()




