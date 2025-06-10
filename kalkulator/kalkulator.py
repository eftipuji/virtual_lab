import streamlit as st
import time

def main():
    st.set_page_config(
        page_title="Kalkulator Pengukuran", # Judul di tab browser
        layout="centered",
        initial_sidebar_state="expanded"
    )

    # --- CSS untuk Latar Belakang Kustom ---
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1547432026-64154b5ee57f?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"); /* Ganti dengan URL gambar bunga Anda */
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }
        .stApp > header {
            background-color: rgba(0,0,0,0); /* Menghilangkan background header */
        }
        .stSidebar {
            background-color: rgba(255, 255, 255, 0.7); /* Background sidebar sedikit transparan */
            border-radius: 10px;
            padding: 10px;
            margin: 10px;
        }
        .stRadio > label {
            color: #333;
            font-weight: bold;
        }
        .stNumberInput > div > label,
        .stSelectbox > label {
            color: #333;
            font-weight: bold;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            cursor: pointer;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
        .stSuccess {
            background-color: rgba(144, 238, 144, 0.8);
            color: #1a5e20;
            border-radius: 8px;
            padding: 10px;
            margin-top: 15px;
            font-weight: bold;
        }
        h1, h2, h3 {
            color: #2F4F4F;
            text-shadow: 1px 1px 2px rgba(255,255,255,0.7);
        }
        p {
            color: #4682B4;
        }
        .animation-container {
            font-size: 2.5em; /* Ukuran emoji */
            text-align: center;
            margin-bottom: 20px;
            height: 80px; /* Cukup tinggi untuk animasi */
            overflow: hidden; /* Pastikan tidak ada scrollbar dari animasi */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # --- Animasi Pembuka: Kelopak Bunga Berjatuhan ---
    placeholder_animasi_awal = st.empty()
    emojis = ["🌸", "🌺", "🌼", "🌷", "🏵️"]
    for _ in range(3): # Mengulang animasi beberapa kali
        for i in range(10): # Jumlah frame animasi
            frame = ""
            for j in range(len(emojis)):
                pos = (i + j * 2) % 10
                frame += " " * pos + emojis[j] + " " * (9 - pos)
            
            placeholder_animasi_awal.markdown(f"<div class='animation-container'>{frame}</div>", unsafe_allow_html=True)
            time.sleep(0.1)
    placeholder_animasi_awal.empty() # Hapus setelah selesai

    st.markdown("<h1 style='text-align: center; color: #8B4513;'>📏 Kalkulator Pengukuran ⚖️🌡️</h1>", unsafe_allow_html=True)
    st.write("<p style='text-align: center; font-size: 1.1em;'>Konversi berbagai unit pengukuran dengan mudah dan interaktif.</p>", unsafe_allow_html=True)

    st.markdown("---")

    # --- Pilihan Pengukuran di Sidebar ---
    pilihan_pengukuran = st.sidebar.radio(
        "Pilih Jenis Pengukuran:",
        ("Panjang", "Berat", "Suhu")
    )

    if pilihan_pengukuran == "Panjang":
        kalkulator_panjang()
    elif pilihan_pengukuran == "Berat":
        kalkulator_berat()
    elif pilihan_pengukuran == "Suhu":
        kalkulator_suhu()

    st.markdown("---")

    # --- Animasi Penutup: Bunga Mekar/Berkembang ---
    placeholder_animasi_akhir = st.empty()
    bunga_mekar = [
        "🌱", # Tunas
        "🌿", # Daun
        "🌷", # Kuncup
        "🌸", # Mekar sebagian
        "🌺"  # Mekar penuh
    ]
    for _ in range(2): # Mengulang animasi
        for i in range(len(bunga_mekar)):
            placeholder_animasi_akhir.markdown(f"<div class='animation-container'>{bunga_mekar[i] * (i + 1)}</div>", unsafe_allow_html=True)
            time.sleep(0.2)
        for i in range(len(bunga_mekar) - 2, -1, -1): # Kembali layu
            placeholder_animasi_akhir.markdown(f"<div class='animation-container'>{bunga_mekar[i] * (i + 1)}</div>", unsafe_allow_html=True)
            time.sleep(0.2)
    placeholder_animasi_akhir.empty() # Hapus setelah selesai


    st.markdown("<p style='text-align: center;'>Semoga kalkulator ini bermanfaat!</p>", unsafe_allow_html=True)


def kalkulator_panjang():
    st.header("Konversi Panjang")

    col1, col2 = st.columns(2)
    with col1:
        satuan_asal = st.selectbox(
            "Pilih Satuan Asal:",
            ("Meter", "Centimeter", "Kilometer", "Inci", "Mil", "Yard", "Kaki")
        )
    with col2:
        nilai = st.number_input(f"Masukkan Nilai ({satuan_asal}):", min_value=0.0, format="%.4f", key="panjang_nilai")

    satuan_target = st.selectbox(
        "Pilih Satuan Target:",
        ("Meter", "Centimeter", "Kilometer", "Inci", "Mil", "Yard", "Kaki"),
        key="panjang_target"
    )

    if st.button("Konversi Panjang"):
        hasil = 0
        faktor_ke_meter = {
            "Meter": 1,
            "Centimeter": 0.01,
            "Kilometer": 1000,
            "Inci": 0.0254,
            "Mil": 1609.34,
            "Yard": 0.9144,
            "Kaki": 0.3048
        }

        nilai_dalam_meter = nilai * faktor_ke_meter[satuan_asal]

        if satuan_target == "Meter":
            hasil = nilai_dalam_meter
        elif satuan_target == "Centimeter":
            hasil = nilai_dalam_meter * 100
        elif satuan_target == "Kilometer":
            hasil = nilai_dalam_meter / 1000
        elif satuan_target == "Inci":
            hasil = nilai_dalam_meter / 0.0254
        elif satuan_target == "Mil":
            hasil = nilai_dalam_meter / 1609.34
        elif satuan_target == "Yard":
            hasil = nilai_dalam_meter / 0.9144
        elif satuan_target == "Kaki":
            hasil = nilai_dalam_meter / 0.3048

        st.success(f"{nilai} {satuan_asal} = **{hasil:.4f}** {satuan_target}")

def kalkulator_berat():
    st.header("Konversi Berat")

    col1, col2 = st.columns(2)
    with col1:
        satuan_asal = st.selectbox(
            "Pilih Satuan Asal:",
            ("Kilogram", "Gram", "Pound", "Ons", "Ton (Metrik)")
        )
    with col2:
        nilai = st.number_input(f"Masukkan Nilai ({satuan_asal}):", min_value=0.0, format="%.4f", key="berat_nilai")

    satuan_target = st.selectbox(
        "Pilih Satuan Target:",
        ("Kilogram", "Gram", "Pound", "Ons", "Ton (Metrik)"),
        key="berat_target"
    )

    if st.button("Konversi Berat"):
        hasil = 0
        faktor_ke_kg = {
            "Kilogram": 1,
            "Gram": 0.001,
            "Pound": 0.453592,
            "Ons": 0.0283495,
            "Ton (Metrik)": 1000
        }

        nilai_dalam_kg = nilai * faktor_ke_kg[satuan_asal]

        if satuan_target == "Kilogram":
            hasil = nilai_dalam_kg
        elif satuan_target == "Gram":
            hasil = nilai_dalam_kg * 1000
        elif satuan_target == "Pound":
            hasil = nilai_dalam_kg / 0.453592
        elif satuan_target == "Ons":
            hasil = nilai_dalam_kg / 0.0283495
        elif satuan_target == "Ton (Metrik)":
            hasil = nilai_dalam_kg / 1000

        st.success(f"{nilai} {satuan_asal} = **{hasil:.4f}** {satuan_target}")

def kalkulator_suhu():
    st.header("Konversi Suhu")

    col1, col2 = st.columns(2)
    with col1:
        satuan_asal = st.selectbox(
            "Pilih Satuan Asal:",
            ("Celcius", "Fahrenheit", "Kelvin", "Reamur")
        )
    with col2:
        nilai = st.number_input(f"Masukkan Nilai ({satuan_asal}):", format="%.2f", key="suhu_nilai")

    satuan_target = st.selectbox(
        "Pilih Satuan Target:",
        ("Celcius", "Fahrenheit", "Kelvin", "Reamur"),
        key="suhu_target"
    )

    if st.button("Konversi Suhu"):
        hasil = 0

        # Konversi ke Celcius terlebih dahulu
        nilai_dalam_celcius = 0
        if satuan_asal == "Celcius":
            nilai_dalam_celcius = nilai
        elif satuan_asal == "Fahrenheit":
            nilai_dalam_celcius = (nilai - 32) * 5/9
        elif satuan_asal == "Kelvin":
            nilai_dalam_celcius = nilai - 273.15
        elif satuan_asal == "Reamur":
            nilai_dalam_celcius = nilai * 5/4

        # Konversi dari Celcius ke satuan target
        if satuan_target == "Celcius":
            hasil = nilai_dalam_celcius
        elif satuan_target == "Fahrenheit":
            hasil = (nilai_dalam_celcius * 9/5) + 32
        elif satuan_target == "Kelvin":
            hasil = nilai_dalam_celcius + 273.15
        elif satuan_target == "Reamur":
            hasil = nilai_dalam_celcius * 4/5

        st.success(f"{nilai} {satuan_asal} = **{hasil:.4f}** {satuan_target}")

if __name__ == "__main__":
    main()
