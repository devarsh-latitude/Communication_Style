import streamlit as st
import json

#Inputs : 1,2,3,4,5,6,7,8,9,10,11
try:
    with open("/home/devarsh/Devarsh/date_28_02/input_matching.json","r") as fs:
        data = json.load(fs)

    for i in data.keys():
        data[i]=list(map(int,data[i].split('-')))

    u_input = st.text_input('Enter Numbers Comma Separated: ', '1,2,8,9')
    user_input = list(map(int,u_input.split(",")))

    count_res={1:0,2:0,3:0,4:0}
    for i in user_input:
        for count,val in enumerate(data.values(),1):
            if i in val:
                count_res[count]+=1

    st.write("Your communication style is of : Style "+ str(max(zip(count_res.values(), count_res.keys()))[1]))
except:
    st.write("Please Enter Values Systematically only.")