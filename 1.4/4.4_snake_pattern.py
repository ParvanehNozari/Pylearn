def draw_snake_pattern():
    while True:
        try:
            n = int(input("Enter the length of the snake: "))
            if n < 0:
                print("Please enter a non-negative integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    pattern = ""
    for i in range(n):
        if i % 2 == 0:
            pattern += "*"
        else:
            pattern += "#"

    print(pattern)

draw_snake_pattern()
