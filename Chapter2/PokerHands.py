import sys

BLACK, WHITE, TIE = 0, 1, 2

"""
High Card. Hands which do not fit any higher category are ranked by the value of their highest card.
If the highest cards have the same value, the hands are ranked by the next highest, and so on. 1

Pair. 2 of the 5 cards in the hand have the same value. Hands which both contain a pair are ranked
by the value of the cards forming the pair. If these values are the same, the hands are ranked by
the values of the cards not forming the pair, in decreasing order. 2

Two Pairs. The hand contains 2 different pairs. Hands which both contain 2 pairs are ranked by the
value of their highest pair. Hands with the same highest pair are ranked by the value of their
other pair. If these values are the same the hands are ranked by the value of the remaining card. 3

Three of a Kind. Three of the cards in the hand have the same value. Hands which both contain
three of a kind are ranked by the value of the 3 cards. 4

Straight. Hand contains 5 cards with consecutive values. Hands which both contain a straight are
ranked by their highest card.

Flush. Hand contains 5 cards of the same suit. Hands which are both flushes are ranked using the
rules for High Card. 5

Full House. 3 cards of the same value, with the remaining 2 cards forming a pair. Ranked by the
value of the 3 cards. 6

Four of a kind. 4 cards with the same value. Ranked by the value of the 4 cards. 7

Straight flush. 5 cards of the same suit with consecutive values. Ranked by the highest card in the
hand. 8

"""

card_sequence = [None] * 29
values = [ [0]*5, [0]*5 ] 
suit = [ [0]*5, [0]*5 ] 

sorted_white = [0] * 5 
sorted_black = [0] * 5 

card_count = [ [0]*15, [0]*15 ] 

white_score_array = [0] * 3
black_score_array = [0] * 3

def print_winner(player):

    if (player == BLACK):
        print("Black wins.")
    elif (player == WHITE):
        print("White wins.")
    else:
        print("Tie.")

    return

def count_cards():
    


    for player in range(0,2):
        
        for i in range(0,5):
            card_count [player] [ values[player] [i] ] += 1

    

    return


def high_card():
    
    # Devuelve 0 si el ganador es BLACK o 1 si el ganador es WHITE, 2 si es EMPATE
    
    i = 4
    while (sorted_white[i] == sorted_black[i] and i >= 0): 
        i -= 1
    

    if (i == -1 and sorted_white[0] == sorted_black[0]):
        return TIE

    return 0 if sorted_black[i] > sorted_white[i] else 1
   

def pair_cards(player):

    pairs = -1
    for i in range(2,15):

        if (card_count [player] [i] == 2):
            pairs = i
            break
    

    if (pairs != -1):
        return pairs + pairs
    else:
        return -1
    


def two_pair(player):

    idx = 0
    # Valor de la pareja, valor de la pareja, valor restante
    pairs = [-1,-1,-1]
    n_pairs = 0
    for i in range(2,15):

        if (card_count [player] [i] == 2):
            pairs[idx] = i
            idx += 1
            n_pairs += 1
        

        if (card_count [player] [i] == 1):
            pairs[2] = i

    if n_pairs == 2:
        if (player == WHITE):
            white_score_array [0] = pairs [0]
            white_score_array [1] = pairs [1]
            white_score_array [2] = pairs [2]
        
        else:
            black_score_array [0] = pairs [0]
            black_score_array [1] = pairs [1]
            black_score_array [2] = pairs [2]
    
    else:
        if (player == WHITE):
            white_score_array [0] = -1
            white_score_array [1] = -1
            white_score_array [2] = -1
        else:
            black_score_array [0] = -1
            black_score_array [1] = -1
            black_score_array [2] = -1

    return

def three_of_a_kind(player):

    for i in range(2,15):

        if (card_count [player] [i] == 3): 
            return i * 3
        
        
    
    return -1


def straight(player):

    if player == WHITE:

        for i in range(0,4):

            if (sorted_white [i + 1] - sorted_white [i] != 1) :
                return -1
    else:
        for i in range(0,4):

            if (sorted_black [i + 1] - sorted_black [i] != 1) :
                return -1
    
    
    if (player == WHITE):
        return sorted_white [4]
    else:
        return sorted_black [4]
    

def flush (player):
    suit_type = suit[player] [0]
    for i in range(0,4):

        if (suit[player] [i + 1] != suit_type):
            return -1
    

    return max(values[player])

def full_house (player):

    three,two,value = 0,0,0

    for i in range(2,15):

        if (card_count [player] [i] == 3 ):
            three += 1
            value = i
        
            
        if (card_count [player] [i] == 2):
            two += 1
        
    

    if (three == 1 and two == 1):
        return value * 3

    return -1


def four_of_a_kind(player):


    for i in range(2,15):

        if (card_count [player] [i] == 4): 
            return i * 4
    

    return -1


def straight_flush(player):

    suit_type = suit[player] [0]

    if player == WHITE:

        for i in range(0,4):

            if (sorted_white [i + 1] - sorted_white [i] != 1) :
                return -1

            if (suit[player] [i + 1] != suit_type):
                return -1
    else:
        for i in range(0,4):

            if (sorted_black [i + 1] - sorted_black [i] != 1) :
                return -1

            if (suit[player] [i + 1] != suit_type):
                return -1
        
        
    
    if (player == WHITE):
        return sorted_white [4]
    else:
        return sorted_black [4]


def main():
    lel = ["2H 2S 3C 3D AC 3S 3H 5H 4H AS\n"]

    global card_count
    global sorted_white
    global sorted_black
    #for line in sys.stdin:
    for line in sys.stdin:
        card_sequence = line[:-1]
        card_count = [ [0]*15, [0]*15 ] 
        sorted_white = [0] * 5 
        sorted_black = [0] * 5 
        idx = 0
        for i in range(0,15,3):
            if card_sequence[i] == 'T':
                values [BLACK][idx] =  10
                suit [BLACK][idx] = card_sequence [i + 1]
                sorted_black[idx] = values [BLACK][idx]                
                idx += 1
                continue

            if card_sequence[i] == 'J':
                values [BLACK][idx] =  11
                suit [BLACK][idx] = card_sequence [i + 1]
                sorted_black[idx] = values [BLACK][idx]
                idx += 1
                continue

            if card_sequence[i] == 'Q':
                values [BLACK][idx] =  12
                suit [BLACK][idx] = card_sequence [i + 1]
                sorted_black[idx] = values [BLACK][idx]
                idx += 1
                continue

            if card_sequence[i] == 'K':
                values [BLACK][idx] =  13
                suit [BLACK][idx] = card_sequence [i + 1]
                sorted_black[idx] = values [BLACK][idx]                
                idx += 1
                continue

            if card_sequence[i] == 'A':
                values [BLACK][idx] =  14
                suit [BLACK][idx] = card_sequence [i + 1]
                sorted_black[idx] = values [BLACK][idx]
                idx += 1
                continue

    
            values [BLACK][idx] =  int(card_sequence[i])
            
            suit [BLACK][idx] = card_sequence [i + 1]
            sorted_black[idx] = values [BLACK][idx]
            idx += 1
        
        idx = 0
        for i in range(15,29,3):

                
                        
            if card_sequence[i] == 'T':
                values [WHITE][idx] =  10
                suit [WHITE][idx] = card_sequence [i + 1]
                sorted_white[idx] = values [WHITE][idx]                    
                idx += 1
                continue

            if card_sequence[i] == 'J':
                values [WHITE][idx] =  11
                suit [WHITE][idx] = card_sequence [i + 1]
                sorted_white[idx] = values [WHITE][idx]                    
                idx += 1
                continue

            if card_sequence[i] == 'Q':
                values [WHITE][idx] =  12
                suit [WHITE][idx] = card_sequence [i + 1]
                sorted_white[idx] = values [WHITE][idx]                    
                idx += 1
                continue

            if card_sequence[i] == 'K':
                values [WHITE][idx] =  13
                suit [WHITE][idx] = card_sequence [i + 1]
                sorted_white[idx] = values [WHITE][idx]                    
                idx += 1
                continue

            if card_sequence[i] == 'A':
                values [WHITE][idx] =  14
                suit [WHITE][idx] = card_sequence [i + 1]
                sorted_white[idx] = values [WHITE][idx]                
                idx += 1
                continue

            values [WHITE][idx] =  int(card_sequence[i])

            
            suit [WHITE][idx] = card_sequence [i + 1]
            sorted_white[idx] = values [WHITE][idx]
            idx += 1
        
        sorted_white = sorted(sorted_white)
        sorted_black = sorted(sorted_black)
        count_cards()


        black_score = straight_flush(BLACK) 
        white_score = straight_flush(WHITE)

        if (black_score != -1 or white_score != -1):

            if (black_score != -1 and white_score != -1):

                if black_score == white_score:
                    print_winner(TIE)
                    continue

                print_winner(BLACK) if black_score > white_score else print_winner(WHITE)
                continue
            

            if (black_score != -1):
                print_winner(BLACK)
            else:
                print_winner(WHITE)
            
            continue
        
        black_score = four_of_a_kind(BLACK)
        white_score = four_of_a_kind(WHITE)
        if (black_score != -1 or white_score != -1):

            if (black_score != -1 and white_score != -1):

                if black_score == white_score:
                    print_winner(TIE)
                    continue

                print_winner(BLACK) if black_score > white_score else print_winner(WHITE)
                continue
            

            if (black_score != -1):
                print_winner(BLACK)
            else:
                print_winner(WHITE)
            
            continue
        

        

        black_score = full_house(BLACK)
        white_score = full_house(WHITE)

        if (black_score != -1 or white_score != -1):

            if (black_score != -1 and white_score != -1):

                if black_score == white_score:
                    print_winner(TIE)
                    continue

                print_winner(BLACK) if black_score > white_score else print_winner(WHITE)
                continue

            if (black_score != -1):
                print_winner(BLACK)
            else:
                print_winner(WHITE)
            continue

        black_score = flush(BLACK)
        white_score = flush(WHITE)

        if (black_score != -1 or white_score != -1):

            if (black_score != -1 and white_score != -1):
                aux = high_card()
                if aux == 2:
                    print_winner(TIE)
                    continue
                print_winner(BLACK) if aux == 0 else print_winner(WHITE)
                continue
            

            if (black_score != -1):
                print_winner(BLACK)
            else:
                print_winner(WHITE)
            continue
        

        black_score = straight(BLACK)
        white_score = straight(WHITE)

        if (black_score != -1 or white_score != -1):

            if (black_score != -1 and white_score != -1):

                if black_score == white_score:
                    print_winner(TIE)
                    continue

                print_winner(BLACK) if black_score > white_score else print_winner(WHITE)
                continue

            if (black_score != -1):
                print_winner(BLACK)
            else:
                print_winner(WHITE)
            continue
        

        black_score = three_of_a_kind(BLACK) 
        white_score = three_of_a_kind(WHITE)

        if (black_score != -1 or white_score != -1):

            if (black_score != -1 and white_score != -1):

                if black_score == white_score:
                    print_winner(TIE)
                    continue

                print_winner(BLACK) if black_score > white_score else print_winner(WHITE)
                continue

            if (black_score != -1):
                print_winner(BLACK)
            else:
                print_winner(WHITE)
            continue
        

        two_pair(BLACK)
        two_pair(WHITE)

        if (black_score_array[0] != -1 or white_score_array[0] != -1):

            if (black_score_array[0] != -1 and white_score_array[0] != -1):
                
                idx = 1
                while (black_score_array [idx] == white_score_array [idx] and idx >= 0):
                    idx -= 1
                
                if (idx == -1):

                    if (black_score_array[2] == white_score_array [2]):
                        print_winner(TIE)
                        continue
                    
    
                    print_winner(BLACK) if black_score_array [2]> white_score_array [2] else print_winner(WHITE)
                    continue

                
                print_winner(BLACK) if black_score_array [idx] > white_score_array [idx] else print_winner(WHITE)
                continue

            if (black_score_array[0] != -1):
                print_winner(BLACK)
                continue

            if white_score_array[0] != -1:
                print_winner(WHITE)
                continue

        

        black_score = pair_cards(BLACK)
        white_score = pair_cards(WHITE)

        if (black_score != -1 or white_score != -1):

            if (black_score != -1 and white_score != -1):

                

                if (black_score == white_score):

                    half = black_score // 2

                    sorted_black = [elem for elem in sorted_black if elem != half]
                    sorted_white = [elem for elem in sorted_white if elem != half]

                    idx = 2
                    while( (sorted_black[idx] == sorted_white[idx])  and idx >= 0):
                        idx -= 1

                    if (idx == -1 and sorted_white[0] == sorted_black[0]):
                        print_winner(TIE)
                        continue
                    
                    print_winner(BLACK) if sorted_black[idx] > sorted_white[idx] else print_winner(WHITE)
                    continue

                print_winner(BLACK) if black_score > white_score else print_winner(WHITE)
                continue
                
            

            if (black_score != -1):
                print_winner(BLACK)
            else:
                print_winner(WHITE)
            
            continue

        
        aux = high_card()

        if (aux == 2):
            print_winner(TIE)
            continue
        
            


        print_winner(BLACK) if aux == 0 else print_winner(WHITE)

        
if __name__ == "__main__":
    main()
    


