from Methods import bisection_method, golden_ratio, fibonacci, search_minimal_segment
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calc_number, result = fibonacci(-2, 20,  10E-5, "fibonacci.txt")
    search_minimal_segment(7, 10E-1, "search_minimum.txt")
    print(calc_number, result)

