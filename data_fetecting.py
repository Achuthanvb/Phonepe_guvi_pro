import os
import json
import pandas as pd
import mysql.connector


#coonnecting local DATABASE
mydb = mysql.connector.connect(
    host='localhost',
    port='3306',
    user="root",
    database='phonepe_pulse_db',
    password="achuthan@13")
cursor = mydb.cursor()



path1 = "C:/Users/Lenovo/Desktop/Phonepe_pluse/pulse/data/aggregated/transaction/country/india/state/"
Agg_state_list = os.listdir(path1)
col1 = {'State': [], 'Year': [], 'Quater': [], 'Transaction_type': [], 'Transaction_count': [],
        'Transaction_amount': []}
for i in Agg_state_list:
    p_i = path1 + i + "/"
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            A = json.load(Data)
            for z in A['data']['transactionData']:
                Name = z['name']
                count = z['paymentInstruments'][0]['count']
                amount = z['paymentInstruments'][0]['amount']
                col1['Transaction_type'].append(Name)
                col1['Transaction_count'].append(count)
                col1['Transaction_amount'].append(amount)
                col1['State'].append(i)
                col1['Year'].append(j)
                col1['Quater'].append(int(k.strip('.json')))
df_aggregated_transaction = pd.DataFrame(col1)
# df_aggregated_transaction


# TO GET THE DATA-FRAME OF AGGREGATED <--> USER
path2 ="C:/Users/Lenovo/Desktop/Phonepe_pluse/pulse/data/aggregated/user/country/india/state/"
user_list = os.listdir(path2)
col2 = {'State': [], 'Year': [], 'Quater': [], 'brands': [], 'Count': [],
        'Percentage': []}
for i in user_list:
    p_i = path2 + i + "/"
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            B = json.load(Data)
            try:
                for w in B["data"]["usersByDevice"]:
                    brand_name = w["brand"]
                    count_ = w["count"]
                    ALL_percentage = w["percentage"]
                    col2["brands"].append(brand_name)
                    col2["Count"].append(count_)
                    col2["Percentage"].append(ALL_percentage)
                    col2["State"].append(i)
                    col2["Year"].append(j)
                    col2["Quater"].append(int(k.strip('.json')))
            except:
                pass
df_aggregated_user = pd.DataFrame(col2)
#df_aggregated_user

path3 = "C:/Users/Lenovo/Desktop/Phonepe_pluse/pulse/data/map/transaction/hover/country/india/state/"
hover_list = os.listdir(path3)
col3 = {'State': [], 'Year': [], 'Quater': [], 'District': [], 'count': [],
        'amount': []}
for i in hover_list:
    p_i = path3 + i + "/"
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            C = json.load(Data)
            for x in C["data"]["hoverDataList"]:
                District = x["name"]
                count = x["metric"][0]["count"]
                amount = x["metric"][0]["amount"]
                col3["District"].append(District)
                col3["count"].append(count)
                col3["amount"].append(amount)
                col3['State'].append(i)
                col3['Year'].append(j)
                col3['Quater'].append(int(k.strip('.json')))
df_map_transaction = pd.DataFrame(col3)
# df_map_transaction

path4 = "C:/Users/Lenovo/Desktop/Phonepe_pluse/pulse/data/map/user/hover/country/india/state/"
map_list = os.listdir(path4)
col4 = {"State": [], "Year": [], "Quater": [], "District": [], "RegisteredUser": []}

for i in map_list:
    p_i = path4 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            D = json.load(Data)

            for u in D["data"]["hoverData"].items():
                district = u[0]
                registereduser = u[1]["registeredUsers"]
                col4["District"].append(district)
                col4["RegisteredUser"].append(registereduser)
                col4['State'].append(i)
                col4['Year'].append(j)
                col4['Quater'].append(int(k.strip('.json')))
df_map_user = pd.DataFrame(col4)
#df_map_user

path5 = "C:/Users/Lenovo/Desktop/Phonepe_pluse/pulse/data/top/transaction/country/india/state/"
TOP_list = os.listdir(path5)
col5 = {'State': [], 'Year': [], 'Quater': [], 'District': [], 'Transaction_count': [],
        'Transaction_amount': []}
for i in TOP_list:
    p_i = path5 + i + "/"
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            E = json.load(Data)
            for z in E['data']['pincodes']:
                Name = z['entityName']
                count = z['metric']['count']
                amount = z['metric']['amount']
                col5['District'].append(Name)
                col5['Transaction_count'].append(count)
                col5['Transaction_amount'].append(amount)
                col5['State'].append(i)
                col5['Year'].append(j)
                col5['Quater'].append(int(k.strip('.json')))
df_top_transaction = pd.DataFrame(col5)
#df_top_transaction

# TO GET THE DATA-FRAME OF TOP <--> USER
path6 = "C:/Users/Lenovo/Desktop/Phonepe_pluse/pulse/data/top/user/country/india/state/"
USER_list = os.listdir(path6)
col6 = {'State': [], 'Year': [], 'Quater': [], 'District': [],
        'RegisteredUser': []}
for i in USER_list:
    p_i = path6 + i + "/"
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            F = json.load(Data)
            for t in F['data']['pincodes']:
                Name = t['name']
                registeredUser = t['registeredUsers']
                col6['District'].append(Name)
                col6['RegisteredUser'].append(registeredUser)
                col6['State'].append(i)
                col6['Year'].append(j)
                col6['Quater'].append(int(k.strip('.json')))
df_top_user = pd.DataFrame(col6)
#df_top_user


#Inserting DATA into MYSQL DATABASE


# table1
cursor.execute("DROP TABLE IF EXISTS df_aggregated_transaction")
# Creating table as per requirement
sql1 = '''CREATE TABLE df_aggregated_transaction(
   State CHAR(35) NOT NULL,
   Year INT,
   Quater INT,
   Transaction_type CHAR(30),
   Transaction_count INT,
   Transaction_amount FLOAT(53)
)'''
cursor.execute(sql1)
insert_stmt1 = """INSERT INTO df_aggregated_transaction(State, Year, Quater, Transaction_type, Transaction_count,Transaction_amount)VALUES (%s, %s, %s, %s, %s,%s)"""

data1 = []
for i in range(len(df_aggregated_transaction)):
    d = (df_aggregated_transaction.iloc[i][0], int(df_aggregated_transaction.iloc[i][1]),
         int(df_aggregated_transaction.iloc[i][2]), df_aggregated_transaction.iloc[i][3],
         int(df_aggregated_transaction.iloc[i][4]), float(df_aggregated_transaction.iloc[i][5]))
    data1.append(d)

for i in data1:
    cursor.execute(insert_stmt1, i)

    # table2

# df_aggregated_user

cursor.execute("DROP TABLE IF EXISTS df_aggregated_user")
# Creating table as per requirement
sql2 = '''CREATE TABLE df_aggregated_user(
      State CHAR(35) NOT NULL,
      Year INT,
      Quater INT,
      brands CHAR(30),
      Count INT,
      Percentage FLOAT(53)
   )'''
cursor.execute(sql2)
insert_stmt2 = """INSERT INTO df_aggregated_user(State, Year, Quater, brands, Count,Percentage)VALUES (%s, %s, %s, %s, %s,%s)"""

data2 = []
for i in range(len(df_aggregated_user)):
    d = (df_aggregated_user.iloc[i][0], df_aggregated_user.iloc[i][1], int(df_aggregated_user.iloc[i][2]),
         df_aggregated_user.iloc[i][3], int(df_aggregated_user.iloc[i][4]), float(df_aggregated_user.iloc[i][5]))
    data2.append(d)

for i in data2:
    cursor.execute(insert_stmt2, i)

# table 3
cursor.execute("DROP TABLE IF EXISTS df_map_transaction")
# Creating table as per requirement
sql3 = '''CREATE TABLE df_map_transaction(
   State CHAR(35) NOT NULL,
   Year INT,
   Quater INT,
   District CHAR(40),
   Count INT,
   amount FLOAT(53)
)'''
cursor.execute(sql3)
insert_stmt3 = """INSERT INTO df_map_transaction(State, Year, Quater, District, Count,amount)VALUES (%s, %s, %s, %s, %s,%s)"""

data3 = []

for i in range(len(df_map_transaction)):
    d = (df_map_transaction.iloc[i][0], df_map_transaction.iloc[i][1], int(df_map_transaction.iloc[i][2]),
         df_map_transaction.iloc[i][3], int(df_map_transaction.iloc[i][4]), float(df_map_transaction.iloc[i][5]))
    data3.append(d)

for i in data3:
    cursor.execute(insert_stmt3, i)

# table4
cursor.execute("DROP TABLE IF EXISTS df_map_user")
# Creating table as per requirement
sql4 = '''CREATE TABLE df_map_user(
   State CHAR(35) NOT NULL,
   Year INT,
   Quater INT,
   District CHAR(40),
   RegisteredUser INT
)'''
cursor.execute(sql4)
insert_stmt4 = """INSERT INTO df_map_user(State, Year, Quater, District, RegisteredUser)VALUES ( %s, %s, %s, %s,%s)"""

data4 = []

for i in range(len(df_map_user)):
    d = (df_map_user.iloc[i][0], df_map_user.iloc[i][1], int(df_map_user.iloc[i][2]), df_map_user.iloc[i][3],
         int(df_map_user.iloc[i][4]))
    data4.append(d)

for i in data4:
    cursor.execute(insert_stmt4, i)

# table5
cursor.execute("DROP TABLE IF EXISTS df_top_transaction")
# Creating table as per requirement
sql5 = '''CREATE TABLE df_top_transaction(
   State CHAR(35) NOT NULL,
   Year INT,
   Quater INT,
   District CHAR(40),
   Transaction_count INT,
   Transaction_amount FLOAT(53)
)'''
cursor.execute(sql5)
insert_stmt5 = """INSERT INTO df_top_transaction(State, Year, Quater, District, Transaction_count,Transaction_amount)VALUES (%s, %s, %s, %s, %s,%s)"""

data5 = []

for i in range(len(df_top_transaction)):
    d = (df_top_transaction.iloc[i][0], int(df_top_transaction.iloc[i][1]), int(df_top_transaction.iloc[i][2]),
         df_top_transaction.iloc[i][3], int(df_top_transaction.iloc[i][4]), float(df_top_transaction.iloc[i][5]))
    data5.append(d)
for i in data5:
    cursor.execute(insert_stmt5, i)

# table6
cursor.execute("DROP TABLE IF EXISTS df_top_user")
# Creating table as per requirement
sql6 = '''CREATE TABLE df_top_user(
   State CHAR(35) NOT NULL,
   Year INT,
   Quater INT,
   District CHAR(13),
   RegisteredUser INT
   )'''
cursor.execute(sql6)
insert_stmt6 = """INSERT INTO df_top_user(State, 
Year, Quater, District, RegisteredUser)VALUES (%s, %s, %s, %s,%s)"""

data6 = []
for i in range(len(df_top_user)):
    d = (df_top_user.iloc[i][0], df_top_user.iloc[i][1], int(df_top_user.iloc[i][2]), df_top_user.iloc[i][3],
         int(df_top_user.iloc[i][4]))
    data6.append(d)

for i in data6:
    cursor.execute(insert_stmt6, i)

print("ALL DONE")