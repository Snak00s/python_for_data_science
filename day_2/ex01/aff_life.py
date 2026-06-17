import matplotlib.pyplot as plt
from load_csv import load


def main():
    df = load("life_expectancy_years.csv")
    if (type(df) is type(None)):
        exit(1)
    idx = df.index[df['country'] == "France"].to_list()
    if (len(idx) != 1):
        print("Error : Multiple occurence or not found")
        exit(1)
        return
    idx = idx[0]
    france = df.loc[idx][1:].astype(float)
    france.plot(x="country", xlabel="Year",
                ylabel="Life expectancy",
                title="France Life expectancy Projection")
    plt.show()
    return


if __name__ == "__main__":
    main()
