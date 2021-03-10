from methods import bisection_method, golden_ratio, fibonacci, search_minimal_segment
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calc_number, result = fibonacci(-2, 20, 10E-2, "fibonacci_report.txt")
    calc_number1, result1 = golden_ratio(-2, 20, 10E-2, "golden_ratio_report.txt")
    search_minimal_segment(6, 10E-3, "search_minimum_report.txt")
    print(calc_number, result)

