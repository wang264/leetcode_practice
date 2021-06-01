import numpy as np
import pandas as pd


def solution(files):
    # files - any of available files, i.e:
    # files = ["./data/framp.csv", "./data/gnyned.csv", "./data/gwoomed.csv",
    #            "./data/hoilled.csv", "./data/plent.csv", "./data/throwsh.csv",
    #            "./data/twerche.csv", "./data/veeme.csv"]

    # write your solution here
    # return list of list, each list contain two dataframes.
    files = ["./bakelai_csv/throwsh.csv", "./bakelai_csv/twerche.csv"]
    rslt = []

    # file = files[0]
    for file in files:
        df_raw = pd.read_csv(file, parse_dates=["date"], index_col=0)
        df_raw["year"] = [idx.year for idx in df_raw.index]
        # find distinct year
        unique_year = sorted(list(set([idx.year for idx in df_raw.index])))

        ls_df_max_vol = []
        for year in unique_year:
            df_year = df_raw[df_raw["year"]==year]
            max_vol = df_year["vol"].max()
            df_year_max_vol = df_year[df_year["vol"]==max_vol]
            ls_df_max_vol.append(df_year_max_vol)

        df_max_vol = pd.concat(ls_df_max_vol)[["vol"]]
        df_max_vol.reset_index(inplace=True)

        ls_df_max_close = []
        for year in unique_year:
            df_year = df_raw[df_raw["year"] == year]
            max_close = df_year["close"].max()
            df_year_max_close = df_year[df_year["close"] == max_close]
            ls_df_max_close.append(df_year_max_close)

        df_max_close = pd.concat(ls_df_max_close)[["close"]]
        df_max_close.reset_index(inplace=True)

        rslt_one_file = [df_max_vol, df_max_close]
        rslt.append(rslt_one_file)
