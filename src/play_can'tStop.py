from game import Game
from players.glenn_player import Glenn_Player
from players.random_player import RandomPlayer
import copy
import json
import pickle
from players.Couto_Player import Couto_Player
def main(count):
    game = Game(n_players = 2, dice_number = 4, dice_value = 6, column_range = [2,12],
            offset = 2, initial_height = 3)

    is_over = False
    who_won = None
    
    p1 = Glenn_Player()
    p2 = Couto_Player()
    
      
    state_action_pairs = {}
    state_action_pairs[1] = []
    state_action_pairs[2] = []
    state_action_pairs_current_round = []

    current_player = game.player_turn
    while not is_over:
        moves = game.available_moves()
        # if len(moves) >4:
        #     print(len(moves))
        #     print(moves)
        #     print(game.current_roll)

        #     print("HERE")
        #     # input()
        # print(game.current_roll)
        # print(moves)
        # input()
        if game.is_player_busted(moves):
            state_action_pairs_current_round = []
            
            if current_player == 1:
                current_player = 2
            else:
                # print('Your Turn to Play')
                current_player = 1
            continue
        else:
            if current_player != game.player_turn:
                print('deu merda')
                exit()
            if game.player_turn == 1:
                # print(game.current_roll)
                moves = game.available_moves()
                print("Available actions: \t", moves)


                # print(dir(game))
                # print(game.board_game.board)
                # print(game.current_roll)
                # print(game.neutral_positions)
                # print("positions")
                # input()
                # print(dir(game))
                # print(game.n_neutral_markers)
                # print(game.neutral_positions)
                # print(game.current_roll)
                # print(moves)
                # input()
                # print(moves)
                
                # print('Choose one of the available options: ')
                # input()
                # print("\n")
                
                if moves[0] =='y' or moves[0]=='n':
                    # print("Yes/NO")
                    # # chosen_play = str(input())
                    
                    # chosen_play = p2.get_action(game)
                    # print("Please choose yes/no! (y for yes and n for No)")
                    # chosen_index = str(input())
                    # while chosen_index != 'y' and chosen_index != 'n':
                    #     print("Please choose either y or n!")
                    #     chosen_index = str(input())
                
                    # assert game.n_neutral_markers <=3
                    # print(chosen_play)
                    chosen_play = p2.get_action(game)

                    
                else:
                    # print("Column decision")
                    # print("Please choose the index of the action you want to choose (from 1 to %s)"%(len(moves)))
                    # chosen_index = int(input())
                    # while chosen_index > len(moves) or chosen_index<=0:
                    #     print("Please enter a value from 1 to ",len(moves))
                    #     chosen_index = int(input())
                    chosen_play = p2.get_action(game)
                    # chosen_play = moves[chosen_index-1]
                    # print("CHOSE", chosen_play)
                    
            else:
                
                # moves = game.available_moves()
                chosen_play = p2.get_action(game)
                # print(chosen_play)
            
            pair = (copy.deepcopy(game), chosen_play)
            state_action_pairs_current_round.append(pair)
                        
            if chosen_play == 'n':
                state_action_pairs[current_player].append(state_action_pairs_current_round)
                state_action_pairs_current_round = []
                
                if current_player == 1:                        
                    current_player = 2
                else:                
                    current_player = 1
            game.play(chosen_play)
            game.print_board()
            

        who_won, is_over = game.is_finished()

        # print('who won = ', who_won)
        if is_over:
            if who_won==1:
                count +=1
            # with open('random_match_3.pkl', 'wb') as file_match:
            #     print('state_action_pairs')
            #     print(state_action_pairs)
            #     pickle.dump(state_action_pairs, file_match)
            return count
            
if __name__ == "__main__":
    count = 0
    for i in range(100):
        count = main(count)
    print(count)
    #'''
    # match1 = None
    # match2 = None
    # match3 = None
    
    # with open('random_match_1.pkl', 'rb') as human_data_file:
    #     match1 = pickle.load(human_data_file)

    # with open('random_match_2.pkl', 'rb') as human_data_file:
    #     match2 = pickle.load(human_data_file)

    # with open('random_match_3.pkl', 'rb') as human_data_file:
    #     match3 = pickle.load(human_data_file)

    # collection_matches = [match1, match2, match3]
    # print('collection_matches')
    # print(collection_matches)
    # with open('random_matches.pkl', 'wb') as file_match:
    #     pickle.dump(collection_matches, file_match)
    #'''

    
    
    