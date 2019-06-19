import pandas as pd

file = pd.read_csv(r'c:\Users\F15059\PycharmProjects\work\EON_Hack\SV2_ARENA_Trends_15min_AsIs_BWB_MBS1_20190420_011025.csv', sep=',')

df = pd.DataFrame(file)
size = df.shape


for row in range(size[0]):
    for column in range(size[1]):
        # print(row, column)

        # get value
        entry = df.iloc[row, column]
        is_numberic(entry)
