from Methods import bisection_method, golden_ratio
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calc_number, result = bisection_method(-2, 20, 0.01, "bisection.txt")
    print(calc_number, result)

