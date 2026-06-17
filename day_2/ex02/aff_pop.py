import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def convert_unit(cell: pd.Series) -> pd.Series:
    """
    Convert string pd.Series into int pd.Series for string formated as x.xK :
    'x' as digit and 'K' as metric unit like M for millions, k for thoushand
    """
    ret = []
    for country_pop in cell:
        last_idx = 0
        for char in country_pop:
            if (char.isnumeric() is True) or (char == "."):
                last_idx += 1
            else:
                break
        var = float(country_pop[0:last_idx])

        if country_pop[last_idx] == "M":
            var *= 1e6

        if country_pop[last_idx] == "k":
            var *= 1e3

        ret.append(int(var))

    return pd.Series(ret, index=cell.index)


def main():

    df = load("population_total.csv")
    if (type(df) is type(None)):
        exit(1)
    fr_idx = df.index[df['country'] == "France"].to_list()
    if (len(fr_idx) != 1):
        print("Error : Multiple occurence or not found")
        exit(1)
        return
    bg_idx = df.index[df['country'] == "Belgium"].to_list()
    if (len(bg_idx) != 1):
        print("Error : Multiple occurence or not found")
        exit(1)
        return

    pop = df.loc[[fr_idx[0], bg_idx[0]]]
    pop = pop.set_index('country').transpose()
    pop = pop[pop.index.astype(int) <= 2050]
    pop = pop.apply(convert_unit, axis=1)
    pop.plot(ylabel="Population", xlabel="Year",
             title="Population Projections")
    plt.show()
    return


if __name__ == "__main__":
    main()
