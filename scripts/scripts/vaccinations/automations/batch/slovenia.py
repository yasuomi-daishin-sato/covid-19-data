import pandas as pd

def main():

    df = pd.read_csv(
        "https://raw.githubusercontent.com/sledilnik/data/master/csv/vaccination.csv",
        usecols=["date", "vaccination.administered.todate"]
    )

    df = df.rename(columns={"vaccination.administered.todate": "total_vaccinations"})
    df = df[-df["total_vaccinations"].isna()]

    df.loc[:, "location"] = "Slovenia"
    df.loc[:, "source_url"] = "https://covid-19.sledilnik.org/en/stats"
    df.loc[:, "vaccine"] = "Pfizer/BioNTech"

    df.to_csv("automations/output/Slovenia.csv", index=False)

if __name__ == "__main__":
    main()
