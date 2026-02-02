import streamlit as st
from common.base import stylePage

# ---------------------- UI WIDTH AND MAPI KEY ----------------------
defaultMAPI = "eyJ1ciI6InN1bWl0QG1pZGFzaXQuY29tIiwicGciOiJjaXZpbCIsImNuIjoia2xDdlBJV0FRZyJ9.a4416151529e131327528db57e28ab6c1b055e69ad7a3dde6bf0c05ab4dd74f2"
stylePage(300,defaultMAPI)  # APP WIDTH -> 300px , mapiKey is set to defaultMAPI for testing

# ---------------------- CIVIL NX CONNECTION ----------------------
from midas_civil import *
MAPI_KEY(st.session_state.mapiKey)
MAPI_BASEURL.autoURL()

# ---------------------- FUNCTIONS ----------------------
def createNode():
    Node.delete()
    for i in range(st.session_state.numNode):
        Node(i,0,0)
    Node.create()

# ---------------------- UI OF PLUGIN ----------------------
st.header('NODE CREATOR')
st.number_input('Number of Nodes',min_value=1,max_value=20,value=10,key='numNode')
st.button("CREATE NODE",icon=':material/add_circle_outline:',type='primary',on_click=createNode)