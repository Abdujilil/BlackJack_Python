import random
import art
import time


def check_result(hands):
    busted, hands["Dealer"] = is_busted(hands["Dealer"])
    print(f"You have {sum(hands["Player"])}, the Dealer has {sum(hands["Dealer"])}.")
    if busted:
        print("Dealer busted! You win!!!")
    else:
        if sum(hands["Dealer"]) > sum(hands["Player"]):
            print("Dealer wins!\n")
        elif sum(hands["Player"]) > sum(hands["Dealer"]):
            print("Player wins!\n")
        else:
            print("It's a draw!\n")


def dealer_hits(dealers_cards, deck):
    dealers_sum = sum(dealers_cards)
    while dealers_sum < 17:
        print("Dealer hits\n")
        dealers_cards = one_more_card(dealers_cards, deck)
        time.sleep(1)
        print(f"Now the dealer has {dealers_cards}\n")
        dealers_sum = sum(dealers_cards)
        if dealers_sum >= 17:
            return dealers_cards


def should_dealer_hit(dealers_cards):
    dealers_cards = replace_ace_value(dealers_cards)
    if sum(dealers_cards) < 17:
        return True


def check_for_blackjack(initial_cards):
    if sum(initial_cards) == 21:
        return True


def deal_cards(deck):
    player_cards = [random.choice(deck), random.choice(deck)]
    dealer_cards = [random.choice(deck), random.choice(deck)]
    hands_in_game = {
        "Player": player_cards,
        "Dealer": dealer_cards,
    }
    return hands_in_game


def one_more_card(current_hand, deck):
    new_card = random.choice(deck)
    current_hand.append(new_card)
    return current_hand


def replace_ace_value(hand):
    if 11 in hand:
        hand[hand.index(11)] = 1
        print(f"The new card value is {hand}")
    return hand


def is_busted(current_hand):
    if 11 in current_hand:
        current_hand[current_hand.index(11)] = 1
        return False, current_hand
    else:
        if sum(current_hand) > 21:
            return True, current_hand
        else:
            return False, current_hand


def game_play():
    play = True
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    while play:
        player_hit = True
        dealer_hit = True
        random.shuffle(cards)
        hands = deal_cards(cards)

        want_to_play = input("Would you like to play a game of Blackjack? Type 'y' or 'n': \n")
        if want_to_play == 'n':
            print("Another time then!\n")
            return

        print("\n" * 20)
        print(art.logo)
        print("\nGood luck player!\n\n")
        print(f"Your cards are: {hands['Player']}\n")
        print(f"Dealer's first card is: {hands['Dealer'][0]}\n")

        if check_for_blackjack(hands['Player']):
            print(f"You have blackjack! {hands['Player']}\n")
            if check_for_blackjack(hands['Dealer']):
                print(f"The Dealer has blackjack too! {hands['Dealer']} It's a Draw!\n")
            else:
                print(f"The Dealer has {hands['Dealer']}. You win!\n")
        else:
            while player_hit or dealer_hit:
                more_cards = input("Would you like another card? Type 'y' or 'n': \n")
                if more_cards == 'n':
                    player_hit = False
                    print("Dealer's turn!\n")
                    print(f"Dealer's cards are {hands['Dealer']}\n")
                    if should_dealer_hit(hands["Dealer"]):
                        hands["Dealer"] = dealer_hits(hands["Dealer"], cards)
                        check_result(hands)
                        dealer_hit = False
                    else:
                        check_result(hands)
                        dealer_hit = False
                else:
                    hands["Player"] = one_more_card(hands["Player"], cards)
                    print(f"Now you have {hands['Player']}")
                    busted, hands["Player"] = is_busted(hands["Player"])
                    if busted:
                        print(f"You have {hands['Player']} busted! You lose!!\n")
                        print(f"The Dealer has {hands['Dealer']}.\n")
                        player_hit = False
                        dealer_hit = False
                    elif sum(hands["Player"]) == 21:
                        player_hit = False
                        print("You have 21!")


game_play()
