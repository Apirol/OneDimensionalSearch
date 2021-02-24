from Methods import bisection_method, golden_ratio, fibonacci, search_minimal_segment
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calc_number, result = fibonacci(-2, 20,  10E-1, "golden_ratio.txt")
    search_minimal_segment(-1, 10E-10)
    print(calc_number, result)

