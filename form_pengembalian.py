import streamlit as st
import datetime
import data  # pastikan data.py berada dalam direktori yang sama atau tambahkan ke PYTHONPATH

# Initialize session state if it doesn't exist
if 'arynama' not in st.session_state:
    st.session_state.arynama = []
if 'aryjudul' not in st.session_state:
    st.session_state.aryjudul = []
if 'arytglpinjam' not in st.session_state:
    st.session_state.arytglpinjam = []
if 'arytglkembali' not in st.session_state:
    st.session_state.arytglkembali = []
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = ''
if 'selected_title' not in st.session_state:
    st.session_state.selected_title = ''

st.title("📄 Menu Pengembalian Buku")
st.write("Silahkan Masukkan Data Diri Anda")

def run_form_pengembalian():
    form2 = st.form(key="annotation2", clear_on_submit=True)
    with form2:
        cols = st.columns((1, 1))
        nama = cols[0].text_input("Nama Lengkap :")

        # Pilihan kategori
        kategori = cols[1].selectbox('Pilih Kategori Buku', ['', 'Filsafat', 'Psychology', 'Sejarah'], key='selected_category')

        # Perbarui pilihan judul buku berdasarkan kategori yang dipilih
        judul_list = ['']
        if kategori:
            judul_list += data.categories.get(kategori, [])

        judul = cols[0].selectbox('Pilih Judul Buku', judul_list, key='selected_title')

        cols = st.columns(2)
        tglpinjam = cols[0].date_input("Tanggal Peminjaman :", datetime.date.today() - datetime.timedelta(days=7))
        tglkembali = cols[1].date_input("Tanggal Deadline Pengembalian :", datetime.date.today())
        submitted = form2.form_submit_button(label="Submit")

        if submitted:
            if not nama or not judul:
                st.error("Nama dan judul buku harus diisi.")
                return

            tglskg = datetime.datetime.now()
            tglWajib = tglkembali.strftime('%Y-%m-%d').split('-')
            tglWajib = list(map(int, tglWajib))

            selisihTahun = tglskg.year - tglWajib[0]
            selisihBulan = tglskg.month - tglWajib[1]
            selisihTanggal = tglskg.day - tglWajib[2]
            totalHari = (selisihTahun * 365 + selisihBulan * 30 + selisihTanggal)
            denda = max(0, 5000 * totalHari)

            if denda == 0:
                st.success("Terimakasih sudah mengembalikan buku tepat pada waktunya!")
                st.balloons() 
            else:
                st.success(f"Anda terlambat mengembalikan buku sebanyak {totalHari} hari, maka harap membayar denda sebesar {denda} rupiah")

            st.session_state.arynama.append(nama)
            st.session_state.aryjudul.append(judul)
            st.session_state.arytglpinjam.append(tglpinjam)
            st.session_state.arytglkembali.append(tglkembali)

            struk_filename = f"struk-pengembalian-{nama}-{tglkembali}.txt"
            with open(struk_filename, "w") as f:
                f.write('''
************************  PERPUS MINIMALISM  ************************
********** Sistem Pengembalian Buku Perpustakaan Digital ***********
************************ Struk Bukti Pengembalian *************************
''')
                f.write(f'Tanggal : {tglkembali}\n')
                f.write(f"Nama Pengembali Buku : {nama}\n")
                f.write(f"Judul Buku : {judul}\n")
                f.write(f"Tanggal Peminjaman : {tglpinjam}\n")
                f.write(f"Tanggal Pengembalian : {tglkembali}\n")
                f.write(f"Denda : {denda} rupiah\n")
                f.write('''
---Terima Kasih Telah Mengembalikan Buku Ditempat Kami---
---Struk Harap Dibawa pada saat pengembalian Denda (jika ada)---
''')

            with open(struk_filename, "r") as f:
                st.text(f.read())

if __name__ == "__main__":
    run_form_pengembalian()
