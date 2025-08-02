import json
import logging

logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO)

strategy_dict_x = {}
strategy_dict_o = {}


class History:
    def __init__(self, history=None):
        if history is not None:
            self.history = history
            self.board = self.get_board()
        else:
            self.history = []
            self.board = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
        self.player = self.current_player()

    def current_player(self):
        total_num_moves = len(self.history)
        if total_num_moves < 9:
            if total_num_moves % 2 == 0:
                return 'x'
            else:
                return 'o'
        else:
            return None

    def get_board(self):
        board = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
        for i in range(len(self.history)):
            if i % 2 == 0:
                board[self.history[i]] = 'x'
            else:
                board[self.history[i]] = 'o'
        return board

    def is_win(self):
        board = self.get_board()
        if board[0] == board[1] == board[2] and board[0] != '0':
            if board[0] == 'x':
                return 1
            else:
                return -1
        elif board[3] == board[4] == board[5] and board[3] != '0':
            if board[3] == 'x':
                return 1
            else:
                return -1
        elif board[6] == board[7] == board[8] and board[6] != '0':
            if board[6] == 'x':
                return 1
            else:
                return -1
        elif board[0] == board[3] == board[6] and board[0] != '0':
            if board[0] == 'x':
                return 1
            else:
                return -1
        elif board[1] == board[4] == board[7] and board[1] != '0':
            if board[1] == 'x':
                return 1
            else:
                return -1
        elif board[2] == board[5] == board[8] and board[2] != '0':
            if board[2] == 'x':
                return 1
            else:
                return -1
        elif board[0] == board[4] == board[8] and board[0] != '0':
            if board[0] == 'x':
                return 1
            else:
                return -1
        elif board[2] == board[4] == board[6] and board[2] != '0':
            if board[2] == 'x':
                return 1
            else:
                return -1
        else:
            return 0

    def is_draw(self):
        return len(self.history)==9 and (self.is_win() == 0)

    def get_valid_actions(self):
        actions = []
        board = self.get_board()
        for i in range(len(board)):
            if board[i]=='0':
                actions.append(i)
        return actions

    def is_terminal_history(self):
        return self.is_draw() or (self.is_win()!=0)

    def get_utility_given_terminal_history(self):
        if self.is_terminal_history():
            if self.is_draw():
                return 0
            return self.is_win()
        else:
            return 0

def backward_induction(history_obj):
    global strategy_dict_x, strategy_dict_o

    if history_obj.is_terminal_history():
        return history_obj.get_utility_given_terminal_history()
    history_str = ''
    for i in history_obj.history:
        history_str+=str(i)
    if len(history_obj.history) %2 == 0:
        strategy_dict_x[history_str] = {}
        for i in range(9):
            strategy_dict_x[history_str][i]=-2
    elif len(history_obj.history) < 9:
        strategy_dict_o[history_str] = {}
        for i in range(9):
            strategy_dict_o[history_str][i]=-2
    
    if history_obj.player == 'x':
        best = -2
        for move in history_obj.get_valid_actions():
            newhistory = History(history_obj.history + [move])
            val = backward_induction(newhistory)
            best = max(best,val)
            strategy_dict_x[history_str][move]=val
    else:
        best = 2
        for move in history_obj.get_valid_actions():
            newhistory = History(history_obj.history + [move])
            val = backward_induction(newhistory)
            best = min(best,val)
            strategy_dict_o[history_str][move]=-val
    return best

def solve_tictactoe():
    backward_induction(History())
    with open('./policy_x.json', 'w') as f:
        json.dump(strategy_dict_x, f)
    with open('./policy_o.json', 'w') as f:
        json.dump(strategy_dict_o, f)
    return strategy_dict_x, strategy_dict_o


if __name__ == "__main__":
    logging.info("Start")
    solve_tictactoe()
    logging.info("End")
