import streamlit as st
import pandas as pd
import numpy as np
import time



wind1_excel = pd.read_excel("data/wind1.xlsx")
wind1_birim_excel = pd.read_excel("data/wind1_birim.xlsx")
wind1_data = pd.DataFrame(wind1_excel)
wind1_birim_data = pd.DataFrame(wind1_birim_excel)

def do_stuff_on_page_load():
    st.set_page_config(layout="wide")
do_stuff_on_page_load()
st.title("Gain Enerji Portal")
tab1, tab2, tab3, tab4 = st.tabs(["Wind1", "Wind2", "Hydro1", "Hydro2"])

with tab1:
    col_kazanc, col_dengesizlik, col_üretim = st.columns(3)
    col_kazanc.metric("Günlük Net Kazanç", "40.476 TL", "2.435 TL")
    col_dengesizlik.metric("Ortalama Dengesizlik Miktarı", "-0,64 MWh","-0.2 MWh")
    col_üretim.metric("Günlük Toplam Üretim", "29.54 MWh", "4.7 MWh")

    options = st.multiselect(
        'Verileri Filtrele',
        ['Tarih', 'Saat',"Gün Öncesi Üretim Tahmini (MWh)","Gün İçi Üretim Tahmini Revizesi (MWh)","Gerçekleşen Üretim  (MWh)","Dengesizlik Miktarı (MWh)",
        "Dengesizlik Tutarı (TL)","Dengesizlik Maliyeti (TL)","GÖP Satış Tutarı (TL)","GİP Satış Tutarı (TL)","GİP Alış Tutarı (TL)","Net GİP Tutarı (TL)",
        "Net GİP Kar-Zararı (TL)","Toplam Gelir (TL)","KUDUP (MWh)","Sapma Miktarı (MWh)","KUPST (TL)","İç Tasarruf","Dış Tasarruf"],
        default= ['Tarih', 'Saat',"Gün Öncesi Üretim Tahmini (MWh)","Gün İçi Üretim Tahmini Revizesi (MWh)","Gerçekleşen Üretim  (MWh)"],
        
        )
    with st.spinner('Lütfen bekleyin'):
        time.sleep(5)
    st.success('Tablo başarıyla oluşturuldu')
    with st.container():
        st.dataframe(wind1_data[options], use_container_width = True)
    
    col1,col2 = st.columns(2, gap = "large")
    with col1:
        st.bar_chart(data = wind1_birim_data, x ="Periyot", y = "Birim Dengesizlik Maliyeti", use_container_width= True)
    with col2:
        st.bar_chart(data = wind1_birim_data, x ="Periyot", y = "Birim Üretim Geliri" ,use_container_width= True)