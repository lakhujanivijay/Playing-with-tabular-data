import pandas as pd


file_name = "clean-ramen.csv"

df = pd.read_csv(file_name, sep=",")

brand_product_usa= df[(df["Country"]=="USA") | (df["Country"]=="United States")]

Brandgroup = brand_product_usa.groupby('Brand')

df2 = Brandgroup.apply(lambda x: x['Variety'].unique())

df2 =df2.to_frame().reset_index()

df2.columns = ["Brand", "Unique"]


df2['list_len'] = df2["Unique"].str.len()

print(df2)
# brand_product = brand_product_usa[['Brand','Variety']].value_counts()

# brand_product = brand_product.to_frame().reset_index()
# # print(brand_product.info)
# brand_product.to_csv("out2.xls", sep="\t",index = False)