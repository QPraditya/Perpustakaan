import streamlit as st
from streamlit_option_menu import option_menu

# Import pages dari file lain
from home_page import home_page
from psychology_page import psychology_page
from sejarah_page import sejarah_page
from filsafat_page import filsafat_page

def footer():
    st.markdown("""
    <style>
    .footer {
        padding: 10px;
        text-align: center;
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
    }
    </style>
    <div class="footer">
        <p>© 2024 Perpustakaan Kami. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)

def run():
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)

    # Menambahkan Navbar menggunakan streamlit_option_menu
    selected = option_menu(
        menu_title=None,  # required
        options=["Home", "Filsafat", "Psychology", "Sejarah"],  # required
        icons=["house", "book", "book", "book"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "border-radius": "10px", "overflow": "hidden"},
            "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px", "--hover-color": "#45474B", "border-radius": "10px"},
            "nav-link-selected": {"background-color": "#000", "border-radius": "10px"},
        }
    )

    # Display content based on selected option
    if selected == "Home":
        home_page()
    elif selected == "Filsafat":
        filsafat_page()
    elif selected == "Psychology":
        psychology_page()
    elif selected == "Sejarah":
        sejarah_page()

    # Add some spacing to ensure the footer doesn't overlap the content
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)

    # Add the footer at the bottom
    footer()

if __name__ == "__main__":
    run()
