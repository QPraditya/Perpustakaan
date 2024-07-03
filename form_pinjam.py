import streamlit as st
import datetime
import data  # Assuming data.py is in the same directory or added to PYTHONPATH

def run_form_pinjam():
    # Initialize session state variables if they don't exist
    if 'arynama' not in st.session_state:
        st.session_state.arynama = []
    if 'aryjudul' not in st.session_state:
        st.session_state.aryjudul = []
    if 'arytglpinjam' not in st.session_state:
        st.session_state.arytglpinjam = []
    if 'arytglkembali' not in st.session_state:
        st.session_state.arytglkembali = []

    st.title("Form Peminjaman Buku")

    # Create form for borrowing books
    with st.form(key="borrow_form", clear_on_submit=True):
        nama = st.text_input("Nama Lengkap:")

        # Select category and book title
        kategori = st.selectbox('Pilih Kategori Buku', ['', 'Filsafat', 'Psychology', 'Sejarah'], key='selected_category')

        if kategori:
            judul_list = data.categories.get(kategori, [])
        else:
            judul_list = []
        
        judul = st.selectbox('Pilih Judul Buku', judul_list, key='selected_title')

        # Select borrowing and returning dates
        cols = st.columns(2)
        tglpinjam = cols[0].date_input("Tanggal Peminjaman:", datetime.date.today())
        tglkembali = cols[1].date_input("Tanggal Kembali:", datetime.date.today() + datetime.timedelta(days=7))

        submitted = st.form_submit_button(label="Submit")

        if submitted:
            if not nama or not judul:
                st.error("Nama dan judul buku harus diisi.")
            else:
                # Update session state
                st.session_state.arynama.append(nama)
                st.session_state.aryjudul.append(judul)
                st.session_state.arytglpinjam.append(tglpinjam)
                st.session_state.arytglkembali.append(tglkembali)

                # Display success message and borrowing receipt
                st.success("Terima kasih sudah meminjam buku di perpustakaan! 😄 Jangan lupa simpan struk peminjaman ya")

                receipt = f'''
************************  PERPUS MINIMALISM  ************************
************ Sistem Peminjaman Buku Perpustakaan Digital ************
************************ Struk Bukti Pinjam *************************
Tanggal : {tglpinjam}
Nama Peminjam Buku : {nama}
Judul Buku : {judul}
Tanggal Peminjaman : {tglpinjam}
Tanggal Kembali : {tglkembali}
---Terima Kasih Telah Meminjam Buku Ditempat Kami---
---Struk Harap Dibawa pada saat pengembalian Buku---
'''
                st.text(receipt)

# Run the form
run_form_pinjam()
