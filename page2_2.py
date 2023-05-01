import os
import json
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import mysql.connector
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Totalss",layout="wide")

mydb = mysql.connector.connect(
    host='localhost',
    port='3306',
    user="root",
    password="achuthan@13", database="phonepe_pulse_db")
cursor = mydb.cursor()

#defining the coordinates of INDIA
i_s=json.load(open("C:/Users/Lenovo/Desktop/Phonepe_pluse/states_india.geojson",'r'))
state_id_map={}
for feature in i_s["features"]:
    feature["id"]=feature['properties']['state_code']
    state_id_map[feature['properties']['st_nm']]=feature["id"]

#changing the names of the state ,as same as in database
def change_dict_key(d, old_key, new_key, default_value=None):
    d[new_key] = d.pop(old_key, default_value)

change_dict_key(state_id_map, 'Telangana', 'telangana')
change_dict_key(state_id_map, 'Andaman & Nicobar Island', 'andaman-&-nicobar-islands')
change_dict_key(state_id_map, 'Andhra Pradesh', 'andhra-pradesh')
change_dict_key(state_id_map, 'Arunanchal Pradesh', 'arunachal-pradesh')
change_dict_key(state_id_map, 'Assam', 'assam')
change_dict_key(state_id_map, 'Bihar', 'bihar')
change_dict_key(state_id_map, 'Chhattisgarh', 'chhattisgarh')
change_dict_key(state_id_map, 'Daman & Diu', 'telangana')
change_dict_key(state_id_map, 'Goa', 'goa')
change_dict_key(state_id_map, 'Gujarat', 'gujarat')
change_dict_key(state_id_map, 'Haryana', 'haryana')
change_dict_key(state_id_map, 'Himachal Pradesh', 'himachal-pradesh')
change_dict_key(state_id_map, 'Jammu & Kashmir', 'jammu-&-kashmir')
change_dict_key(state_id_map, 'Jharkhand', 'jharkhand')
change_dict_key(state_id_map, 'Karnataka', 'karnataka')
change_dict_key(state_id_map, 'Kerala', 'kerala')
change_dict_key(state_id_map, 'Lakshadweep', 'lakshadweep')
change_dict_key(state_id_map, 'Madhya Pradesh', 'madhya-pradesh')
change_dict_key(state_id_map, 'Maharashtra', 'maharashtra')
change_dict_key(state_id_map, 'Manipur', 'manipur')
change_dict_key(state_id_map, 'Chandigarh', 'chandigarh')
change_dict_key(state_id_map, 'Puducherry', 'puducherry')
change_dict_key(state_id_map, 'Punjab', 'punjab')
change_dict_key(state_id_map, 'Rajasthan', 'rajasthan')
change_dict_key(state_id_map, 'Sikkim', 'sikkim')
change_dict_key(state_id_map, 'Tamil Nadu', 'tamil-nadu')
change_dict_key(state_id_map, 'Tripura', 'tripura')
change_dict_key(state_id_map, 'Uttar Pradesh', 'uttar-pradesh')
change_dict_key(state_id_map, 'Uttarakhand', 'uttarakhand')
change_dict_key(state_id_map, 'West Bengal', 'west-bengal')
change_dict_key(state_id_map, 'Odisha', 'odisha')
change_dict_key(state_id_map, 'Dadara & Nagar Havelli', 'telangana')
change_dict_key(state_id_map, 'Meghalaya', 'meghalaya')
change_dict_key(state_id_map, 'Mizoram', 'mizoram')
change_dict_key(state_id_map, 'Nagaland', 'nagaland')
change_dict_key(state_id_map, 'NCT of Delhi', 'delhi')
change_dict_key(state_id_map, 'Daman & Diu', 'dadra-&-nagar-haveli-&-daman-&-diu')
state_id_map['dadra-&-nagar-haveli-&-daman-&-diu']=31
state_id_map['ladakh']=12
state_id_map['telangana']=0

#fetching data from MYSQL dataframe

query1 = "Select * from df_aggregated_transaction"
cursor.execute(query1)
q1=cursor.fetchall()
df_aggregated_transaction=pd.DataFrame(q1,columns=cursor.column_names)

query2 = "Select * from df_aggregated_user"
cursor.execute(query2)
q2=cursor.fetchall()
df_aggregated_user=pd.DataFrame(q2,columns=cursor.column_names)

query3 = "Select * from df_map_transaction"
cursor.execute(query3)
q3=cursor.fetchall()
df_map_transaction=pd.DataFrame(q3,columns=cursor.column_names)

query4 = "Select * from df_map_user"
cursor.execute(query4)
q4=cursor.fetchall()
df_map_user=pd.DataFrame(q4,columns=cursor.column_names)

query5 = "Select * from df_top_transaction"
cursor.execute(query5)
q5=cursor.fetchall()
df_top_transaction=pd.DataFrame(q5,columns=cursor.column_names)

query6 = "Select * from df_top_user"
cursor.execute(query6)
q6=cursor.fetchall()
df_top_user=pd.DataFrame(q6,columns=cursor.column_names)

with st.sidebar:
    view1 = st.selectbox("Explore", ["Home", "Insight","About"])


if view1=="Home":
    col1, col2, = st.columns(2)
    col1.image(Image.open("images/phonepe.png"), width=500)
    with col1:
        st.subheader(
            "PhonePe  is an Indian digital payments and financial technology company headquartered in Bengaluru, Karnataka, India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer. The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016. It is owned by Flipkart, a subsidiary of Walmart.")
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
    with col2:
        st.video("images/upi.mp4")

elif view1=="About":
    name = "Achuthan G"
    mail = (f'{"Mail :"}  {"achuthanvbachu12@gmail.com"}')
    description = "An Aspiring DATA-SCIENTIST..!"
    social_media = {
        "GITHUB": "https://github.com/Achuthanvb/Phonepe_guvi_pro/upload/main",
        "LINKEDIN": "https://www.linkedin.com/feed/",
        "INSTAGRAM": "https://www.instagram.com/goal__scorer_/",
    }
    col1, col2, col3 = st.columns(3)
    # col2.image(Image.open("images/my.png"), width=350)
    with col3:
        st.title(name)
        st.write(description)
        st.write("---")
        st.subheader(mail)
    st.write("#")
    cols = st.columns(len(social_media))
    for index, (platform, link) in enumerate(social_media.items()):
        cols[index].write(f"[{platform}]({link})")




elif view1=="Insight":

    c1,c2=st.columns(2)

    with st.sidebar:
        view = st.selectbox("Explore", ["Total Transcations", "Types","Search By"])


    if view=="Total Transcations":

        c11,c22,c33=st.columns([2,9,2])
        with c22:
            st.header(":red[Total Transcations]")
            st.subheader("No. of Counts and Sum of Amount")
        c1, c2 = st.columns(2)
        with c1:
            st.subheader(":green[Insights on Totals of transactions]")
            sortby=st.radio("Sort BY:",["Transaction_count","Transaction_amount","Avrg"],horizontal=True)
        with c2:
            choose_year = st.selectbox("Year:",
                                       options=["2018-2022", 2018, 2019, 2020, 2021, 2022])
            choose_qtr = st.selectbox("Quater", ["All","Q1", "Q2", "Q3", "Q4"])
            if choose_qtr == "Q1":
                qua = 1
            elif choose_qtr == "Q2":
                qua = 2
            elif choose_qtr == "Q3":
                qua = 3
            elif choose_qtr == "Q4":
                qua = 4


        #Sor = (sorted_ty[['State', "Transaction_count", "Transaction_amount", 'Avrg']])

        if choose_year=="2018-2022" and choose_qtr=="All":
            total_tot = df_top_transaction.drop(["Year", 'Quater'], axis='columns')
            total_tot = total_tot.groupby(['State'], as_index=False).sum(
                ['Transaction_amount'])
            total_tot["Avrg"] = total_tot['Transaction_amount'] / total_tot['Transaction_count']
            sorted_ty = (total_tot.sort_values(by=[sortby], ascending=False))
            Sor = (sorted_ty[['State', "Transaction_count", "Transaction_amount", 'Avrg']])
            Sor['st_id'] = Sor['State'].map(state_id_map)

        elif choose_year!="2018-2022" and choose_qtr=="All":
            total_tot = df_top_transaction.groupby(['State', 'Year'], as_index=False).sum(
                ['Transaction_amount'])
            total_tot = total_tot[total_tot["Year"] == choose_year]
            total_tot["Avrg"] = total_tot['Transaction_amount'] / total_tot['Transaction_count']
            sorted_ty = (total_tot.sort_values(by=[sortby], ascending=False))
            Sor = (sorted_ty[['State', "Transaction_count", "Transaction_amount", 'Avrg']])
            Sor['st_id'] = Sor['State'].map(state_id_map)

        elif choose_year!="2018-2022" and choose_qtr!="All":


            total_tot = df_top_transaction.groupby(['State', "Year",'Quater'], as_index=False).sum(
                ['Transaction_amount'])
            total_tot_y=total_tot[(total_tot["Year"]==choose_year) & (total_tot["Quater"]==qua)]
            total_tot_y["Avrg"] = total_tot_y['Transaction_amount'] / total_tot_y['Transaction_count']
            sorted_ty = (total_tot_y.sort_values(by=[sortby], ascending=False))
            Sor = (sorted_ty[['State', "Transaction_count", "Transaction_amount", 'Avrg']])
            Sor['st_id'] = Sor['State'].map(state_id_map)


        elif choose_year=="2018-2022" and choose_qtr!="All":
            total_tot = df_top_transaction.groupby(['State', 'Quater'], as_index=False).sum(
                ['Transaction_amount'])
            total_tot = total_tot[total_tot["Quater"] == qua]
            total_tot["Avrg"] = total_tot['Transaction_amount'] / total_tot['Transaction_count']
            sorted_ty = (total_tot.sort_values(by=[sortby], ascending=False))
            Sor = (sorted_ty[['State', "Transaction_count", "Transaction_amount", 'Avrg']])
            Sor['st_id'] = Sor['State'].map(state_id_map)


        fig1 = px.bar(Sor, x='State', y=sortby, text=sortby, color_discrete_sequence=['#38254D'],
                     title=str(sortby), width=1000,height=500,)
        fig1.update_layout(margin=dict(t=70, b=0, l=70, r=40),
                                hovermode="x unified",
                                xaxis_tickangle=45,
                                xaxis_title=' ', yaxis_title="States",
                                plot_bgcolor='#FFFFFF', paper_bgcolor='#2C1942',
                                title_font=dict(size=25, color='#a5a7ab', family="Lato, sans-serif"),
                                font=dict(color='#FFFFFF'),)


        fig2 = px.choropleth(Sor,
                                         locations='st_id',
                                         geojson=i_s,
                                         color=sortby,
                                         hover_name='State',
                                         width=900,
                                         height=600,
                                         hover_data=[sortby],
                                         color_continuous_scale='purples')
        fig2.update_geos(fitbounds="locations", visible=False)




        c1,c2=st.columns([5,3])
        with c1:
            st.plotly_chart(fig2,use_container_width=True)
            st.plotly_chart(fig1,use_container_width=True)

        with c2:
            st.table(Sor[['State', "Transaction_count", "Transaction_amount", 'Avrg']].set_index(Sor.columns[0]))

        com=df_top_transaction.groupby(['State', 'Year','Quater'], as_index=False).sum(
                ['Transaction_amount'])
    elif view=="Types":

        st.subheader(":green[Insights on types of transactions]")
        c1,c2=st.columns(2)
        with c1:
            choose_type = st.selectbox("Type:",
                                       options=["Recharge & bill payments", "Peer-to-peer payments", "Merchant payments",
                                                "Financial servive", "Others"])
            #co_am = st.radio('Transaction:', ("Amount", 'Count'))
            #if co_am == "Amount":
             #   color1 = 'Transaction_amount'
            #elif co_am == "Count":
            #    color1 = 'Transaction_count'
            sortby = st.radio("Sort BY:", ["Transaction_count", "Transaction_amount", "Avrg"], horizontal=True)
        with c2:
            choose_year = st.selectbox("Year:",
                                       options=["2018-2022", 2018, 2019, 2020, 2021, 2022])
            choose_qtr = st.selectbox("Quater", ["All", "Q1", "Q2", "Q3", "Q4"])
            if choose_qtr == "Q1":
                qua = 1
            elif choose_qtr == "Q2":
                qua = 2
            elif choose_qtr == "Q3":
                qua = 3
            elif choose_qtr == "Q4":
                qua = 4

        if choose_year == "2018-2022" and choose_qtr == "All":
            ty_trans = df_aggregated_transaction.groupby(['State', 'Transaction_type'], as_index=False).sum(
                ['Transaction_amount'])
            ty_trans_Y = ty_trans[ty_trans['Transaction_type'] == choose_type]
            ty_trans_Y['st_id'] = ty_trans_Y['State'].map(state_id_map)
            ty_trans_Y["Avrg"] = ty_trans_Y['Transaction_amount'] / ty_trans_Y['Transaction_count']
            sorted_ty = (ty_trans_Y.sort_values(by=[sortby], ascending=False))
            Sor = (sorted_ty[['State', "Transaction_count", "Transaction_amount", 'Avrg']])
            Sor['st_id'] = Sor['State'].map(state_id_map)
            # Sor = (sorted_ty[['State', "Transaction_count", "Transaction_amount", 'Avrg']])

            # st.table(Sor[['State', "Transaction_count","Transaction_amount",'Avrg']].set_index(Sor.columns[0]))
        elif choose_year != "2018-2022" and choose_qtr == "All":
            ty_trans = df_aggregated_transaction.groupby(['State', 'Transaction_type', 'Year'], as_index=False).sum(
                ['Transaction_amount'])
            ty_trans_Y = ty_trans[ty_trans['Transaction_type'] == choose_type]
            ty_trans_Y = ty_trans_Y[ty_trans_Y["Year"] == choose_year]
            ty_trans_Y['st_id'] = ty_trans_Y['State'].map(state_id_map)
            ty_trans_Y["Avrg"] = ty_trans_Y['Transaction_amount'] / ty_trans_Y['Transaction_count']
            Sor = (ty_trans_Y[["State", "Transaction_count", "Transaction_amount", 'Avrg']].sort_values(by=[sortby],
                                                                                                        ascending=False)
                   )
            Sor['st_id'] = Sor['State'].map(state_id_map)
            # st.table(Sor[['State', "Transaction_count","Transaction_amount",'Avrg']].set_index(Sor.columns[0]))

        elif choose_year != "2018-2022" and choose_qtr != "All":

            ty_trans = df_aggregated_transaction.groupby(['State', 'Transaction_type', 'Year', 'Quater'],
                                                         as_index=False).sum(
                ['Transaction_amount'])
            ty_trans_Y = ty_trans[ty_trans['Transaction_type'] == choose_type]
            ty_trans_Y = ty_trans_Y[ty_trans_Y["Year"] == choose_year]
            ty_trans_Y = ty_trans_Y[ty_trans_Y["Quater"] == qua]
            # ty_trans_Y['st_id'] = ty_trans_Y['State'].map(state_id_map)
            ty_trans_Y["Avrg"] = ty_trans_Y['Transaction_amount'] / ty_trans_Y['Transaction_count']
            Sor = (ty_trans_Y[["State", "Transaction_count", "Transaction_amount", 'Avrg']].sort_values(
                by=[sortby], ascending=False))
            Sor['st_id'] = Sor['State'].map(state_id_map)
            # st.table(Sor[['State', "Transaction_count","Transaction_amount",'Avrg']].set_index(Sor.columns[0]))
        elif choose_year == "2018-2022" and choose_qtr != "All":
            ty_trans = df_aggregated_transaction.groupby(['State', 'Transaction_type', 'Quater'], as_index=False).sum(
                ['Transaction_amount'])
            ty_trans_Y = ty_trans[ty_trans['Transaction_type'] == choose_type]
            ty_trans_Y = ty_trans_Y[ty_trans_Y["Quater"] == qua]
            # ty_trans_Y['st_id'] = ty_trans_Y['State'].map(state_id_map)
            ty_trans_Y["Avrg"] = ty_trans_Y['Transaction_amount'] / ty_trans_Y['Transaction_count']
            Sor = (ty_trans_Y[
                ["State", "Transaction_count", "Quater", "Transaction_amount", 'Avrg']].sort_values(
                by=[sortby], ascending=False))
            Sor['st_id'] = Sor['State'].map(state_id_map)


        fix4 = px.choropleth(Sor,
                             locations='st_id',
                             geojson=i_s,
                             color=sortby,
                             hover_name='State',
                             width=900,
                             height=600,
                             hover_data=[sortby],
                             color_continuous_scale='purples')
        fix4.update_geos(fitbounds="locations", visible=False)
        fig = px.bar(Sor, x='State', y=sortby, text=sortby, color_discrete_sequence=['#38254D'],
                     title=str(choose_type), width=1000, height=500)
        fig.update_layout(margin=dict(t=70, b=0, l=70, r=40),
                          hovermode="x unified",
                          xaxis_tickangle=45,
                          xaxis_title=' ', yaxis_title=" ",
                          plot_bgcolor='#FFFFFF', paper_bgcolor='#2C1942',
                          title_font=dict(size=25, color='#a5a7ab', family="Lato, sans-serif"),
                          font=dict(color='#FFFFFF'), )

        c1, c2 = st.columns([5, 3])
        with c1:
            st.plotly_chart(fix4,use_container_width=True)
            st.plotly_chart(fig,use_container_width=True)
        with c2:
            st.table(Sor[['State', "Transaction_count", "Transaction_amount", 'Avrg']].set_index(Sor.columns[0]))

    elif view=="Search By":
        st.subheader(":green[Explore  by Searching]")
        c1, c2 = st.columns(2)

        with st.sidebar :
            search = st.selectbox("Search By", ["District", "Pincode"])
        if search == "District":
            with c1:
                s = (df_map_user["State"].unique())
                s.sort()
                state = st.selectbox("Select State:", s)
                dd = (df_map_user[df_map_user["State"] == state])
                dd1 = (dd["District"].unique())
                dd1.sort()
                dis = st.selectbox('Search Disrtict', dd1)
            with c1:
                # state=st.selectbox()
                # dist = st.selectbox("Search Disrtict", d)
                # Filter the dataframe using masks
                # m1 = df_map_user["District"].str.contains(text_search)

                st.write(dis)

                sortby = st.radio("Sort BY:", ["Count", "amount", ], horizontal=True)

            with c2:
                choose_col = st.radio("Year/Quater:",
                                      options=['Year', 'Quater'], horizontal=True)

                if choose_col == 'Year':

                    state_df = df_map_transaction[df_map_transaction["State"] == state]
                    state_df1 = state_df[state_df["District"] == dis]

                    years = [2018, 2019, 2020, 2021, 2022]
                    q1 = state_df1[state_df1["Quater"] == 1][sortby]
                    q2 = state_df1[state_df1["Quater"] == 2][sortby]
                    q3 = state_df1[state_df1["Quater"] == 3][sortby]
                    q4 = state_df1[state_df1["Quater"] == 4][sortby]
                    trace1 = go.Bar(
                        x=years,
                        y=q1,
                        name='Q1'
                    )
                    trace2 = go.Bar(
                        x=years,
                        y=q2,
                        name='Q2')
                    trace3 = go.Bar(
                        x=years,
                        y=q3,
                        name='Q3')
                    trace4 = go.Bar(
                        x=years,
                        y=q4,
                        name='Q4')

                    data = [trace1, trace2, trace3, trace4]
                    layout = go.Layout(barmode='group')
                    fig = go.Figure(data=data, layout=layout)

                elif choose_col == 'Quater':
                    state_df = df_map_transaction[df_map_transaction["State"] == state]
                    state_df1 = state_df[state_df["District"] == dis]

                    Quater = [1, 2, 3, 4]
                    y18 = state_df1[state_df1["Year"] == 2018][sortby]
                    y19 = state_df1[state_df1["Year"] == 2019][sortby]
                    y20 = state_df1[state_df1["Year"] == 2020][sortby]
                    y21 = state_df1[state_df1["Year"] == 2021][sortby]
                    y22 = state_df1[state_df1["Year"] == 2022][sortby]
                    trace1 = go.Bar(
                        x=Quater,
                        y=y18,
                        name='2018'
                    )
                    trace2 = go.Bar(
                        x=Quater,
                        y=y19,
                        name='2019')
                    trace3 = go.Bar(
                        x=Quater,
                        y=y20,
                        name='2020')
                    trace4 = go.Bar(
                        x=Quater,
                        y=y21,
                        name='2021')
                    trace5 = go.Bar(
                        x=Quater,
                        y=y22,
                        name='2022')

                    data = [trace1, trace2, trace3, trace4, trace5]
                    layout = go.Layout(barmode='group')
                    fig = go.Figure(data=data, layout=layout)

            with c1:
                st.plotly_chart(fig,use_container_width=True)
            with c2:
                orderby = st.radio("Order By:", ['', 'Year', 'Quater', 'Count', 'amount'])
                if orderby == "":
                    st.table(state_df1.set_index(state_df1.columns[0]))
                else:
                    order_place = (state_df1.sort_values(by=[orderby], ascending=False))
                    st.table(order_place.set_index(order_place.columns[0]))

        elif search == "Pincode":


            with c1:
                s = (df_top_transaction["State"].unique())
                s.sort()
                state = st.selectbox("Select State:", s)
                state_sel = df_top_transaction[df_top_transaction["State"] == state]
                pin_select = (state_sel["District"].unique())
                # pincode.sort()
                pincode = st.selectbox("Select State:", pin_select)
                pin_df = df_top_transaction[df_top_transaction["District"] == pincode]




                sortby = st.radio("Sort BY:", ["Transaction_count", "Transaction_amount", ], horizontal=True)

            with c2:
                choose_col = st.radio("Year/Quater:",
                                      options=['Year', 'Quater'], horizontal=True)

                if choose_col == 'Year':

                    pin_df = df_top_transaction[df_top_transaction["District"] == pincode]

                    years = [2018, 2019, 2020, 2021, 2022]
                    q1 = pin_df[pin_df["Quater"] == 1][sortby]
                    q2 = pin_df[pin_df["Quater"] == 2][sortby]
                    q3 = pin_df[pin_df["Quater"] == 3][sortby]
                    q4 = pin_df[pin_df["Quater"] == 4][sortby]

                    trace1 = go.Bar(
                        x=years,
                        y=q1,
                        name='Q1'
                    )
                    trace2 = go.Bar(
                        x=years,
                        y=q2,
                        name='Q2')
                    trace3 = go.Bar(
                        x=years,
                        y=q3,
                        name='Q3')
                    trace4 = go.Bar(
                        x=years,
                        y=q4,
                        name='Q4')

                    data = [trace1, trace2, trace3, trace4]
                    layout = go.Layout(barmode='group')
                    fig = go.Figure(data=data, layout=layout)

                elif choose_col == 'Quater':
                    pin_df = df_top_transaction[df_top_transaction["District"] == pincode]

                    Quater = [1, 2, 3, 4]
                    y18 = pin_df[pin_df["Year"] == 2018][sortby]
                    y19 = pin_df[pin_df["Year"] == 2019][sortby]
                    y20 = pin_df[pin_df["Year"] == 2020][sortby]
                    y21 = pin_df[pin_df["Year"] == 2021][sortby]
                    y22 = pin_df[pin_df["Year"] == 2022][sortby]
                    trace1 = go.Bar(
                        x=Quater,
                        y=y18,
                        name='2018'
                    )
                    trace2 = go.Bar(
                        x=Quater,
                        y=y19,
                        name='2019')
                    trace3 = go.Bar(
                        x=Quater,
                        y=y20,
                        name='2020')
                    trace4 = go.Bar(
                        x=Quater,
                        y=y21,
                        name='2021')
                    trace5 = go.Bar(
                        x=Quater,
                        y=y22,
                        name='2022')

                    data = [trace1, trace2, trace3, trace4, trace5]
                    layout = go.Layout(barmode='group')
                    fig = go.Figure(data=data, layout=layout)

            with c1:
                st.plotly_chart(fig,use_container_width=True)
            with c2:
                orderby = st.radio("Order By:", ['', 'Year', 'Quater', 'Transaction_count', 'Transaction_amount'])
                if orderby == "":
                    st.table(pin_df.set_index(pin_df.columns[0]))
                else:
                    order_place = (pin_df.sort_values(by=[orderby], ascending=False))
                    st.table(order_place.set_index(order_place.columns[0]))

