import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('marketing_r.csv', sep=",")


def conversion_rate(dataframe, columns_name):
    column_conv = dataframe[dataframe['converted'] == True].groupby(columns_name)['user_id'].nunique()
    column_total = dataframe.groupby(columns_name)['user_id'].nunique()

    conversion_rate = column_conv / column_total
    conversion_rate = conversion_rate.fillna(0)  # NaN wypełniamy zerami

    return conversion_rate


def plotting_conv(dataframe):
    for column in dataframe:
        plt.plot(dataframe.index, dataframe[column])

        plt.title("Data w zależności od kanału")
        plt.xlabel("Data")
        plt.ylabel("Użytkownicy")
        plt.xticks(rotation=45)

        plt.show()
        plt.clf()  # czyści wykres


if __name__ == '__main__':
    age_group_conv = conversion_rate(df, ['date_served', 'age_group'])
    print(age_group_conv)
    # date_served  age_group
    # 1/1/18       0-18 years     0.155172
    #              19-24 years    0.196721
    #              24-30 years    0.105263
    #              30-36 years    0.040816
    #              36-45 years    0.042553

    age_group_conv_df = pd.DataFrame(age_group_conv.unstack(level=1))
    print(age_group_conv_df.head(3))
    plotting_conv(age_group_conv_df)
