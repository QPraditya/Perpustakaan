import streamlit as st
import base64
import plotly.express as px
from streamlit_option_menu import option_menu
import home  # import file home.py
import form_pinjam  # import file form_pinjam.py
import form_pengembalian  # import file form_pengembalian.py

# Set up the Streamlit app configuration
st.set_page_config(page_title="Perpustakaan Ahok", page_icon="📚" , layout="centered")

# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
EXAMPLE_NO = 1  

df = px.data.iris()

@st.cache_data()
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def streamlit_menu(example=1):
    if example == 1:
        # 1. sebagai menu sidebar
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Beranda", "Formulir Peminjaman", "Pengembalian"],  # required
                icons=["house", "book", "reply"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
                styles={
                    "container": {"background-color": "#B"},
                    "icon": {"color": "orange", "font-size": "25px"},
                    "nav-link": {
                        "font-size": "20px",
                        "text-align": "left",
                        "margin": "0px",
                        "--hover-color": "#DE9151",
                    },
                    "nav-link-selected": {"background-color": "#000"},
                }
            )
        return selected

    if example == 2:
        # 2. horizontal menu w/o custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Beranda", "Formulir Peminjaman", "Pengembalian"],  # required
            icons=["house", "book", "reply"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected

    if example == 3:
        # 3. horizontal menu custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Beranda", "Formulir Peminjaman", "Pengembalian"],  # required
            icons=["house", "book", "reply"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )
        return selected

# Custom CSS background dan sidebar color
st.markdown("""
    <style>
    .main {
        background-color: #DBBA7;  /* Background color for the main content */
    }
    .css-1d391kg {
        background-color: #2E2E3A;  /* Background color for the sidebar */
    }
    </style>
    """, unsafe_allow_html=True)

selected = streamlit_menu(example=EXAMPLE_NO)

if selected == "Beranda":
    home.run()  # Jalankan fungsi () Run home.py
if selected == "Formulir Peminjaman":
    form_pinjam.run_form_pinjam()  # Jalankan fungsi () Run form_pinjam.py
if selected == "Pengembalian":
    form_pengembalian.run_form_pengembalian()  # Jalankan fungsi () Run form_pengembalian.py

