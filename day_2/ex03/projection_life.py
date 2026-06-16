import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load

def main():
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    if (type(income) == type(None)):
        exit(1)
    
    expectancy = load("life_expectancy_years.csv")
    if (type(expectancy) == type(None)):
        exit(1)

    print(income)
    return


if __name__ == "__main__":
    main()