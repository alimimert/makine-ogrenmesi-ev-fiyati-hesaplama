import pandas as pd

df_train = pd.read_csv("train.csv")
df_test = pd.read_csv("test.csv")
print(df_train.head(10))

df_train.set_index("Id", inplace=True)
df_test.set_index("Id", inplace=True)
print(df_train.head(10))

print("Train shape: ", df_train.shape)
print("Test shape: ", df_test.shape)
