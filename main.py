print("Demon's Souls: 1\n"
      "Dark Souls I: 2\n"
      "Dark Souls II: 3\n"
      "Dark Souls III: 4\n"
      "Bloodborne: 5\n"
      "Sekiro: Shadows Die Twice: 6\n"
      "Elden Ring: 7\n")
game = int(input("Enter the number corresponding to the souls game calculator you'd like to use: "))

while 1 > game > 7:  # While loop to make sure the game number entered is valid
    print("ERROR: The value inputted is not a valid number, please try again.")
    print("Demon's Souls: 1\n"
          "Dark Souls I: 2\n"
          "Dark Souls II: 3\n"
          "Dark Souls III: 4\n"
          "Bloodborne: 5\n"
          "Sekiro: Shadows Die Twice: 6\n"
          "Elden Ring: 7\n")
    game = int(input("Enter the number corresponding to the souls game calculator you'd like to use: "))

start_level = int(input("start level: "))
end_level = int(input("level you want to be: "))


# Function for the games that use the same calculations (Demon's souls, DS1, DS3, Bloodborne, Elden Ring)
def souls_calc(start, end, maximum):
    low_level_list = [673, 690, 707, 724, 741, 758, 775, 793, 811, 829]
    souls = 0
    if start < 11 and end < 11:
        for i in range(end - start):
            souls = low_level_list[i] + souls
        souls_needed = round(souls)
    elif start < 11:
        for i in range(11 - start):
            souls = low_level_list[i + start - 1] + souls
        for i in range(end - 11):
            souls = souls + int((0.02 * (i + 12) ** 3) + (3.06 * (i + 12) ** 2) + (105.6 * (i + 12)) - 895)
        souls_needed = souls
    elif start <= maximum and end <= maximum:
        for i in range(end - start):
            souls = souls + int((0.02 * (i + start + 1) ** 3) + (3.06 * (i + start + 1) ** 2) + (
                    105.6 * (i + start + 1)) - 895)
        souls_needed = souls
    else:
        souls_needed = "ERROR: The end level is greater than the max level of {0}".format(maximum)

    return souls_needed


def game_calc(start, end):  # Calculation of souls needed based on the game
    if end > start > 0 and end > 0:
        if game == 1:  # Demon's Souls
            max_level = 712
            souls_needed = souls_calc(start_level, end_level, max_level)

        elif game == 2:  # Dark Souls 1
            print("What is your starting class?\n"  # DS1 max level values based on starting class
                  "Warrior: 1\n"
                  "Knight: 2\n"
                  "Wanderer: 3\n"
                  "Thief: 4\n"
                  "Bandit: 5\n"
                  "Hunter: 6\n"
                  "Sorcerer: 7\n"
                  "Pyromancer: 8\n"
                  "Cleric: 9\n"
                  "Deprived: 10\n")
            class_ds1 = int(input("Enter the corresponding number: "))

            while 1 > class_ds1 > 10:
                print("ERROR: The number entered for the class is not valid, please try again")
                print("What is your starting class?\n"
                      "Warrior: 1\n"
                      "Knight: 2\n"
                      "Wanderer: 3\n"
                      "Thief: 4\n"
                      "Bandit: 5\n"
                      "Hunter: 6\n"
                      "Sorcerer: 7\n"
                      "Pyromancer: 8\n"
                      "Cleric: 9\n"
                      "Deprived: 10\n")
                class_ds1 = int(input("Enter the corresponding number: "))

            if class_ds1 == 7:
                max_level = 713
            elif class_ds1 == 2 or class_ds1 == 4:
                max_level = 711
            elif class_ds1 == 3 or class_ds1 == 8:
                max_level = 709
            else:
                max_level = 710

            souls_needed = souls_calc(start_level, end_level, max_level)

        elif game == 3:  # Dark Souls 2
            # No specific formula used for DS2 souls, text file of values used
            ds2_input = open('DS2_Soul_Values.txt', 'r')
            ds2_soul_list = ds2_input.readlines()
            ds2_input.close()

            for i in range(len(ds2_soul_list)):
                ds2_soul_list[i] = int(ds2_soul_list[i])

            if end <= 838:
                souls = 0
                for i in range(end - start):
                    souls = ds2_soul_list[i + start - 1] + souls
                souls_needed = souls
            else:
                souls_needed = "ERROR: The end level is greater than the max level of 838"

        elif game == 4:  # Dark Souls 3
            max_level = 802
            souls_needed = souls_calc(start_level, end_level, max_level)

        elif game == 5:  # Bloodborne
            max_level = 544
            souls_needed = souls_calc(start_level, end_level, max_level)

        elif game == 6:  # Sekiro: Shadows Die Twice
            # Note: This game has no max level
            low_level_list = [500, 514, 528, 542, 557, 572, 587, 602, 618, 634, 650, 666, 682, 698, 715, 732,
                              749, 766, 784, 802, 820, 838, 856, 874, 893]
            xp = 0
            if start < 25 and end < 25:
                for i in range(end - start):
                    xp = low_level_list[i] + xp
                souls_needed = xp
            elif start < 25:
                for i in range(24 - start):
                    xp = low_level_list[i + start - 1] + xp
                for i in range(end - 24):
                    xp = xp + int((0.02 * (i + 25) ** 3) + (2.4204 * (i + 25) ** 2) + (44.741 * (i + 25)) - 1851.8)
                souls_needed = xp
            else:
                for i in range(end - start):
                    xp = xp + int((0.02 * (i + start + 1) ** 3) + (2.4204 * (i + start + 1) ** 2) + (44.741 * (
                            i + start + 1)) - 1851.8)
                souls_needed = xp

        else:  # Elden Ring
            max_level = 713
            souls_needed = souls_calc(start_level, end_level, max_level)

    else:
        souls_needed = "ERROR: The start and/or end level inputted is invalid"

    return souls_needed


souls_required = game_calc(start_level, end_level)

print("Souls required to go from level {0} to {1} is: {2}".format(start_level, end_level, souls_required))
