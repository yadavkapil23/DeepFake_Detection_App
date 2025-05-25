import streamlit as st

st.title("Deepfake Detection")
st.write("This is a testing model.")
st.header("THIS IS THE HEADER OF THIS ")
st.subheader("This is subheader")
st.text("This is plain text.")
st.markdown("Bold and _Italic_ with markdown")


import pandas as pd
df = pd.DataFrame({
    "Name" : ["Jack","Kyle","Rahul","Volodymir"],
    "Age" : [19,23,37,29]
})

st.write("This data was written using the streamlit dataframe.")
st.dataframe(df)
st.text("The above df was written using the dataframe")
st.table(df)
st.text("The above table was made using the table.")

st.write("Please Enter the credentials : ")
name = st.text_input("Enter your name : ")
st.write(f"Your name is : {name}!")

age = st.number_input("enter your age : ")
st.write(f"Your age is : {age}")

rating = st.number_input("Please rate our services , Out of 10 :  ",min_value=1,max_value=10)
st.write(f"the rating was : {rating}")

st.button("This is a button")

st.button("Click me to see the magic!")

if st.button("Click"):
    st.write("you clciked me")

agree = st.checkbox("Agree")
if agree:
    st.write("You agreed to terms and conditions")

#radio

Language = st.radio("favourite language : ",["C++","Java","Python","JavaScript"])
st.write("You selected : ",Language)

option = st.selectbox("Select an option:", ["A","B","C"]) 
st.write("You selected : ",option)



#multiselect
Phone = st.multiselect("Options : ",["Apple","Samsung","Vivo","OnePlus","Google"])
st.write("You selected : ",Phone)


#upload file
file = st.file_uploader("Please upload a file")
if file:
    st.write("File uploaded successful.")
    st.write(file.read())

#sidebad
st.sidebar.title("Sidebar")
options = st.sidebar.selectbox("Menu",["Home","About"])

with st.expander("See more"):
    st.write("Hidden content")


#tabs
tab1, tab2 = st.tabs(["Tab One", "Tab Two"])
tab1.write("This is Tab One")
tab2.write("This is Tab Two")


#form
with st.form("form1"):
    user = st.text_input("Username")
    submit = st.form_submit_button("Submit")
    if submit:
        st.write(f"Hello {user}!")