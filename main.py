import card_deck

deck = card_deck.Deck()

print("Welcome to Blackjack!")

while True:
    menu = """
[1] Play
[2] Show Deck
[3] Shuffle Deck
[q] Quit\n"""

    print(menu)
    user_input = input("Select an option:")
    print()

    if user_input == '1':
        print("You selected PLAY!")
    if user_input == '2':
        deck.show_deck()
    if user_input == '3':
        deck.shuffle_deck()
        print("Deck shuffled!")
    if user_input == 'q':
        print("Thanks for playing\ngoodbye!")
        break
