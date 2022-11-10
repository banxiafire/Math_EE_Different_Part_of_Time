def scipycalculation(country):

    import pandas as pd
    df1 = pd.read_csv(country + '_Weekly_average_data_Cases.csv')
    df2 = pd.read_csv(country + '_Weekly_average_data_Mobility.csv')

    resultapp = []

    for nu in range(1, 103):
        from scipy import stats
        res1 = stats.pearsonr(df1.average_cases_7[nu: nu + 9], df2.average_mobility_7[nu:nu + 9])

        print(res1)

        resultapp.append(res1)

    print(resultapp)




scipycalculation('Sing')