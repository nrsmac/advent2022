import argparse

x_beats_y = {
    'rock': 'scissors',
    'scissors' :'paper',
    'paper':'rock'
}

shape_scores = {
    'rock':1,
    'paper':2,
    'scissors':3
}

policies = { 
    'X': -1, # Lose 
    'Y': 0, # Draw
    'Z': 1 # Win
}

opponent_shapes = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}

def play_round(opponent_shape, policy):
    '''
    Plays a round given shapes
    returns:
        * score: my score given outcome'''

    #print(f"opponent_shape: {opponent_shape}")
    #print(f"policy: {policy}")

    if policy == -1:
        # Lose
        my_shape = x_beats_y[opponent_shape]
    elif policy == 1:
        # Win
        my_shape = x_beats_y[x_beats_y[opponent_shape]]
    else:
        # Draw
        my_shape = opponent_shape

    score = shape_scores[my_shape]
    if policy == 0: score+=3
    if policy == 1: score+=6

    return score


def play_rounds(plays:list):
    '''
    Play a round given a list of player symbols in format:
        [[opponent_play, my_play],[],...]
    '''
    scores = []
    for opponent_shape, policy in plays:
        score = play_round(opponent_shape , policy)
        scores.append(score) 
    return scores

def get_input_plays(input_file):
    '''Reads the input file and returns a list of plays'''
    with open(input_file, 'r') as f:
        # Get pairs of symbols cleaned up
        symbols = [line.strip().split(' ') for line in f.readlines()]

        # Get shapes and policy given symbol
        plays = [[opponent_shapes[symbol[0]], policies[symbol[1]]] for symbol in symbols]
        
    return plays

def main(input_str:str):
    plays = get_input_plays(input_str)
    scores = play_rounds(plays)
    print(f"Total score after second elf encounter: {sum(scores)}")
#    print(play_round('scissors', 1))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str)
    args = parser.parse_args()
    main(args.input)
