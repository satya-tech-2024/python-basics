import pandas as p
import pandas as pd

data_set = {
    "Family": ["Satya", "Subha", "Siddharth", "Shourya"],
    "Age": [45, 37, 13, 9],
    "Education": ["MSc", "MSc", "Year 9", "Year 5"]
}
df = p.DataFrame(data_set)
print(df)

df_indexes = pd.DataFrame(data_set, index=["r1", "r2", "r3", "r4"])

print(df_indexes.loc["r1", "Family"])
# Access rows by indexing
print(df_indexes.iloc[[1,2]])
print(df.dtypes)
print("\n", df.shape)
print(df_indexes.index)
print(df_indexes.T)
print(df_indexes.head(3))
print(df_indexes.tail(3))

open()


# for col in df:
#     print(col)
