import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def main():
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    if (type(income) is type(None)):
        exit(1)

    expectancy = load("life_expectancy_years.csv")
    if (type(expectancy) is type(None)):
        exit(1)

    inc = pd.DataFrame([income["country"], income["1900"]]).transpose()
    inc = inc.rename(columns={"1900": "income"})
    exp = pd.DataFrame([expectancy["country"], expectancy["1900"]]).transpose()
    exp = exp.rename(columns={"1900": "expectancy"})
    proj = pd.merge(inc, exp, on='country')
    proj.plot(x='income', xlim=((300, 10000)),
              xlabel='Gross domestic product', logx=True,
              y='expectancy', ylabel='Life Expectancy',
              title='1900', kind='scatter')
    plt.show()
    return


if __name__ == "__main__":
    main()
