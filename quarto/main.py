# Free for personal or classroom use; see 'LICENSE.md' for details.
# https://github.com/squillero/computational-intelligence

import logging
import argparse
import random
import quarto
import copy

class RandomPlayer(quarto.Player):
    """Random player"""

    def __init__(self, quarto: quarto.Quarto):
        super().__init__(quarto)

    def choose_piece(self):
        return random.randint(0, 15)

    def place_piece(self):
        return random.randint(0, 3), random.randint(0, 3) #column, row

    
class RiskyPlayer(quarto.Player):
    """Risky player"""
    
    def __init__(self, quarto: quarto.Quarto):
        super().__init__(quarto)

    def choose_piece(self):
        """Evito di dare un pezzo che fa vincere l'avversario"""
        quarto = self.get_game()
        for piece in range(quarto.BOARD_SIDE*quarto.BOARD_SIDE):
            if quarto.marked_pieces[piece]==0:
                winning_move = 0
                for i in range(quarto.BOARD_SIDE): #col
                    for j in range(quarto.BOARD_SIDE): #row
                        if winning_move == 0:
                            if quarto.board[j,i] == -1:
                                quarto.place(i, j)
                                if quarto.check_winning_move():
                                    winning_move = 1
                                quarto.unplace(i, j)
                                if winning_move == 0:
                                    quarto.marked_pieces[piece] = 1
                                    return piece
        "Altrimenti do un pezzo random"
        return random.randint(0, 15)

    def place_piece(self):
        """Controllo se è possibile fare una mossa vincente"""
        winning_move = 0
        line_of_like = 0
        piece_ok = False
        quarto = self.get_game()
        for i in range(quarto.BOARD_SIDE): #col
            for j in range(quarto.BOARD_SIDE): #row
                piece_ok = quarto.place(i, j)
                if piece_ok == True:
                    if quarto.check_winning_move():
                        winning_move = 1
                        quarto.unplace(i, j)
                        return i, j;
                    quarto.unplace(i, j)
        """Altrimenti faccio una mossa lines of like se possibile"""
        """lines of like = controllo se ci sono pezzi che hanno almeno una caratteristica in comune"""    
        piece_ok = False    
        if winning_move == 0:
            quarto = self.get_game()
            for i in range(quarto.BOARD_SIDE): #col
                for j in range(quarto.BOARD_SIDE): #row
                    piece_ok = quarto.place(i, j)
                    if piece_ok == True:
                        if quarto.check_line_of_like():
                            line_of_like = 1
                            quarto.unplace(i, j)
                            return i, j;
                        quarto.unplace(i, j)
        """Altrimenti faccio una mossa random""" 
        piece_ok = False
        quarto = self.get_game()
        if line_of_like == 0:
            while not piece_ok:
                x, y = random.randint(0, 3), random.randint(0, 3)
                if quarto.board[y,x] == -1:
                    piece_ok = True
                    return x, y 
       
        
        
def main():
    num_matches = 100
    win = 0
    game = quarto.Quarto()
    for i in range(num_matches):
        game.set_players((RandomPlayer(game), RiskyPlayer(game))) #player 0 = random = avversario, player 1 = risky = io
        winner = game.run()
        if winner == 1:
            win = win + 1
        game.clear()
    win_rate = win / num_matches
    print(f"win rate = {win_rate}")
    #logging.warning(f"main: Winner: player {winner}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='count', default=0, help='increase log verbosity')
    parser.add_argument('-d',
                        '--debug',
                        action='store_const',
                        dest='verbose',
                        const=2,
                        help='log debug messages (same as -vv)')
    args = parser.parse_args()

    if args.verbose == 0:
        logging.getLogger().setLevel(level=logging.WARNING)
    elif args.verbose == 1:
        logging.getLogger().setLevel(level=logging.INFO)
    elif args.verbose == 2:
        logging.getLogger().setLevel(level=logging.DEBUG)

    main()