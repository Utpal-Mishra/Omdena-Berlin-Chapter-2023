import home
import one 
import two
import three
import four
import five
import seven
import status

import streamlit as st

st.audio(open('inspire.mp3', 'rb').read(), format='audio/ogg')

PAGES = {
    "Home": home,
    "Data": one,
    "Delay Proportions": two,
    "Delay via Date": three,
    "Delay via Train No.": four,
    "Delay via Railway Operator": five,
    "Map": seven,
    "Train Status": status
}

st.sidebar.title('Navigation Bar')

selection = st.sidebar.selectbox("Go to: \n", list(PAGES.keys()))
page = PAGES[selection]
page.app()