def findMax(cubes, kind_of_cubes):
    red_cubes = []
    for x in cubes:
        if kind_of_cubes in x:
            red_cubes.append(int(x.replace(kind_of_cubes, "").replace(" ", "")))
        else:
            pass

    return max(red_cubes)













if __name__ == '__main__':
    newList = []
    sum_of_games = 0
    game_index = 1

    power_Mania = 0
    with open('game.txt') as f:
        gamesAndResultsInitial = [line.replace('\n', '') for line in f.readlines()]

    #print(gamesAndResultsInitial)

    gamesAndResultsInitial = list(map(lambda x: x.split(":"), gamesAndResultsInitial))
    gamesAndResultsInitial = list(map(lambda x: [x[0], x[1].replace(";", ",").split(",")], gamesAndResultsInitial))
    for elements in gamesAndResultsInitial:
        red_Cubes = findMax(elements[1], "red")
        green_Cubes = findMax(elements[1], "green")
        blue_Cubes = findMax(elements[1], "blue")

        power_Mania = power_Mania + (red_Cubes * green_Cubes * blue_Cubes)
        if red_Cubes <= 12 and blue_Cubes <= 14 and green_Cubes <= 13:
            sum_of_games = sum_of_games + game_index
        game_index = game_index + 1
    print("sum_of_games " + sum_of_games.__str__())
    print("power_Mania " + power_Mania.__str__())



