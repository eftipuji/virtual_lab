import streamlit as st

st.title("Kalkulator Aritmatika Sederhana")

# Input angka
angka1 = st.number_input("Masukkan angka pertama", value=0.0)
angka2 = st.number_input("Masukkan angka kedua", value=0.0)

# Inisialisasi session_state untuk hasil
if "hasil" not in st.session_state:
    st.session_state.hasil = ""
    st.session_state.error = ""

# Tombol operasi matematika dalam 4 kolom
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Tambah (+)"):
        st.session_state.hasil = f"Hasil: {angka1} + {angka2} = {angka1 + angka2}"
        st.session_state.error = ""

with col2:
    if st.button("Kurang (-)"):
        st.session_state.hasil = f"Hasil: {angka1} - {angka2} = {angka1 - angka2}"
        st.session_state.error = ""

with col3:
    if st.button("Kali (×)"):
        st.session_state.hasil = f"Hasil: {angka1} × {angka2} = {angka1 * angka2}"
        st.session_state.error = ""

with col4:
    if st.button("Bagi (:)"):
        if angka2 != 0:
            st.session_state.hasil = f"Hasil: {angka1} : {angka2} = {angka1 / angka2}"
            st.session_state.error = ""
        else:
            st.session_state.error = "Tidak bisa dibagi dengan nol!"
            st.session_state.hasil = ""

# Tampilkan hasil di tengah, setelah semua tombol
st.markdown("---")
if st.session_state.hasil:
    st.success(st.session_state.hasil)
if st.session_state.error:
    st.error(st.session_state.error)
