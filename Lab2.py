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
    floatlist = [float(i) for i in numberlist] # for every item i in numberlist, convert i to float
    return floatlist


def calc_average(num_list):
    print("calc_average")
    average = sum(num_list) / len(num_list) # sum() adds all elements in the list, len() gives number of elements
    return average


def find_min_max(num_list):
    print("find_min_max")
    min_temp = min(num_list)
    max_temp = max(num_list)
    return [min_temp, max_temp]


def sort_temperature(num_list):
    print("sort_temperature")
    sorted_list = sorted(num_list) # sorted() or .sort() for ascending order
    return sorted_list


def calc_median_temperature(num_list):
    print("calc_median_temperature")
    sorted_list = sorted(num_list)
    n = len(sorted_list)
    mid = n // 2 # integer division (only / returns float)
    if n % 2 == 0:
        median = (sorted_list[mid - 1] + sorted_list[mid]) / 2 # if even number of elements # is mid - 1 cuz of 0 indexing
    else:
        median = sorted_list[mid] # if odd number of elements
    return median


if __name__ == "__main__":
    main()