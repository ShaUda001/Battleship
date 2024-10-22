import random

def main():
    game_board = [['~' for _ in range(8)] for _ in range(8)]
    print()
    ship_x = get_pos_x()
    ship_y = get_pos_y()
    ship_pos = get_ship_pos(ship_x, ship_y)
    used_coordinates = set()
    counter = 15
    hit_counter = 0
    
    while counter != 0:
        display_results(game_board, counter)
        x_value, y_value = get_coordinates()
        if (x_value, y_value) in used_coordinates:
            print("You already used those coordinates")
            continue
        used_coordinates.add((x_value, y_value))
        compare = get_compare(ship_pos, x_value, y_value, game_board)
        hit_counter += compare
        if hit_counter == 4:
            display_results(game_board, counter)
            print("YOU WON!!")
            return
        counter -= 1

    print("\n---------------------------------------------------------")
    print("Game Over!")
    print("You failed to find the ship. This was the ship's location.")
    print("\ns = ship\n")
    print("  1  2  3  4  5  6  7  8")
    for i, row in enumerate(ship_pos):
        print(f"{i + 1}|" + "  ".join(row))

def get_compare(ship_pos, x_value, y_value, game_board):
    hit_counter = 0
    if ship_pos[y_value - 1][x_value - 1] == "s":
        game_board[y_value - 1][x_value - 1] = "x"
        hit_counter += 1
    else:
        game_board[y_value - 1][x_value - 1] = "o"
    return hit_counter

def get_pos_x():
    return random.randint(0, 7)

def get_pos_y():
    return random.randint(0, 7)

def get_ship_pos(ship_x, ship_y):
    ship_pos = [['~' for _ in range(8)] for _ in range(8)]
    vert_or_horiz = random.randint(0, 1)  # 1 = vertical, 0 = horizontal

    if vert_or_horiz == 1:  # vertical ship
        if ship_x >= 4:
            for i in range(4):
                ship_pos[ship_x - i][ship_y] = "s"
        else:
            for i in range(4):
                ship_pos[ship_x + i][ship_y] = "s"
    else:  # horizontal ship
        if ship_y >= 4:
            for i in range(4):
                ship_pos[ship_x][ship_y - i] = "s"
        else:
            for i in range(4):
                ship_pos[ship_x][ship_y + i] = "s"
    return ship_pos

def display_results(game_board, counter):
    print("----------------------------")
    print("~ = Ocean")
    print("o = Miss")
    print("x = Hit\n")
    print("  1  2  3  4  5  6  7  8")
    for i, row in enumerate(game_board):
        print(f"{i + 1}|" + "  ".join(row))
    print(f"\nYou have {counter} turn(s) left\n")

def get_coordinates():
    while True:
        try:
            x = int(input("Input X value (1-8) then press Enter: "))
            y = int(input("Input Y value (1-8) then press Enter: "))
            if 1 <= x <= 8 and 1 <= y <= 8:
                return x, y
            else:
                print("Value out of bound, please try again")
        except ValueError:
            print("Invalid input, please enter a number between 1 and 8")

if __name__ == "__main__":
    main()
