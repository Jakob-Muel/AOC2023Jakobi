def findMatch(entries, winners):
    winners_as_int = []
    entries_as_int = []
    entries_cleaned = entries.replace("\n", "").split(" ")
    winners_cleaned = winners.split(" ")
    for entries in entries_cleaned:
        if entries.isdigit():
            entries_as_int.append(int(entries))
    for winnies in winners_cleaned:
        if winnies.isdigit():
            winners_as_int.append(int(winnies))
    samesies = list(set(entries_as_int).intersection(winners_as_int))
    return samesies.__len__()


def calculate_sums(sorted_card):
    sum_of_points = 0
    for ma_card in sorted_card:
        points_per_card = 1
        matches = findMatch(ma_card[0], ma_card[1][1])
        if matches > 0:
            if matches > 1:
                for i in range(matches - 1):
                    points_per_card = points_per_card * 2

                sum_of_points = sum_of_points + points_per_card

            else:
                sum_of_points = sum_of_points + points_per_card
        else:
            pass
    print(sum_of_points)

def find_NumberOfCards(sorted_card):
    sorted_card_copy = sorted_card
    for my_card in enumerate(sorted_card):
        print(sorted_card.__len__(), "sorted card length")
        matches = findMatch(my_card[1][0], my_card[1][1][1])
        print(matches)
        if matches > 0:
            print("kommt hier an")
            for i in range(matches - 1):
                print(my_card[0]+i+1, "indec")
                print(sorted_card[my_card[0]+1+i], "alsdaf")
                sorted_card.insert(my_card[0]+i+1, sorted_card[my_card[0]+1])


if __name__ == '__main__':
    card_pile = []
    sorted_card = []

    with open('CardPile.txt') as f:
        [card_pile.append(line) for line in f.readlines()]

    for card in card_pile:
        card.split("|")
        sorted_card.append(card.split("|"))

    sorted_card = list(map(lambda x: [x[1], x[0].split(":")], sorted_card))
    calculate_sums(sorted_card)
    find_NumberOfCards(sorted_card)
