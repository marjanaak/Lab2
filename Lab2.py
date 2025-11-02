def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()  

    calc_average(num_list)
    calc_min_max(num_list)


def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    print("get_user_input")
    numberinput = input()
    numberlist = numberinput.split(",")
    floatlist = [float(i) for i in numberlist]
    return floatlist


def calc_average(num_list):
    print("calc_average")
    average = sum(num_list) / len(num_list)
    print("Average: " + str(average))


def calc_min_max(num_list):
    print("calc_min_max")
    minimum = min(num_list)
    maximum = max(num_list)
    print("Min: " + str(minimum))
    print("Max: " + str(maximum))


if __name__ == "__main__":
    main()