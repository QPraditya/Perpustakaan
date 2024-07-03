# filsafat_page.py
import streamlit as st
from PIL import Image
from data import image_paths

def filsafat_page():
    st.title("Buku-buku Filsafat")
    st.write("Berikut ini adalah buku-buku yang tersedia dalam kategori Filsafat:")

    images = [Image.open(img_path) for img_path in image_paths]

    cols = st.columns((1,1,1,1))
    cols1 = st.columns((1,1,1,1))
    cols2 = st.columns((1,1,1,1))
    cols3 = st.columns((1,1,1,1))

    cols[0].image(images[0], width=150)
    cols[0].write("Tersedia 3 Buku")
    cols[1].image(images[1], width=150)
    cols[1].write("Tersedia 2 Buku")
    cols[2].image(images[2], width=150)
    cols[2].write("Tersedia 4 Buku")
    cols[3].image(images[3], width=150)
    cols[3].write("Tersedia 1 Buku")

    cols1[0].image(images[4], width=150)
    cols1[0].write("Tersedia 2 Buku")
    cols1[1].image(images[5], width=150)
    cols1[1].write("Tersedia 2 Buku")
    cols1[2].image(images[6], width=150)
    cols1[2].write("Tersedia 4 Buku")
    cols1[3].image(images[7], width=150)
    cols1[3].write("Tersedia 0 Buku")

    cols2[0].image(images[8], width=150)
    cols2[0].write("Tersedia 2 Buku")
    cols2[1].image(images[9], width=150)
    cols2[1].write("Tersedia 0 Buku")
    cols2[2].image(images[0], width=150)
    cols2[2].write("Tersedia 3 Buku")
    cols2[3].image(images[1], width=150)
    cols2[3].write("Tersedia 2 Buku")

    cols3[0].image(images[2], width=150)
    cols3[0].write("Tersedia 4 Buku")
    cols3[1].image(images[3], width=150)
    cols3[1].write("Tersedia 1 Buku")
    cols3[2].image(images[4], width=150)
    cols3[2].write("Tersedia 2 Buku")
    cols3[3].image(images[5], width=150)
    cols3[3].write("Tersedia 2 Buku")
