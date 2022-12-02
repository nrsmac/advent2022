import argparse

shape_scores = {
    'rock':1,
    'paper':2,
    'scissors':3
}

my_shapes = { 
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

opponent_shapes = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}

def play_round(opponent_shape, my_shape):
    '''
    Plays a round given shapes
    returns:
        * score: my score given outcome'''

    #print(f"Opponent: {opponent_shape}, Me: {my_shape}")
    if opponent_shape == my_shape:  # Tie
        did_I_win = 0  #1 if I win, -1 if opponent wins, 0 if tie
    elif opponent_shape == 'rock':
        if my_shape == 'scissors': did_I_win = -1
        else: did_I_win = 1
    elif opponent_shape == 'paper':
        if my_shape == 'rock': did_I_win = -1
        else: did_I_win = 1
    elif opponent_shape == 'scissors':
        if my_shape == 'paper': did_I_win = -1
        else: did_I_win = 1

    score = shape_scores[my_shape]
    if did_I_win == 0: score+=3
    if did_I_win == 1: score+=6

    return score


def play_rounds(plays:list):
    '''
    Play a round given a list of player symbols in format:
        [[opponent_play, my_play],[],...]
    '''
    scores = []
    for opponent_shape, my_shape in plays:
        score = play_round(opponent_shape , my_shape)
        scores.append(score) 
    return scores

def get_input_plays(input_file):
    '''Reads the input file and returns a list of plays'''
    with open(input_file, 'r') as f:
        # Get pairs of symbols cleaned up
        symbols = [line.strip().split(' ') for line in f.readlines()]
        #print(symbols)

        # Get shapes given strategy symbol
        plays = [[opponent_shapes[symbol[0]], my_shapes[symbol[1]]] for symbol in symbols]
        
    return plays

def main(input_str:str):
    plays = get_input_plays(input_str)
    scores = play_rounds(plays)
    print(f"Total score after first elf encounter: {sum(scores)}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str)
    args = parser.parse_args()
    main(args.input)
