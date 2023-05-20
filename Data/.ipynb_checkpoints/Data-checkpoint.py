import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

st.title('Veri Seti İnceleme')

dataset_options = ["house_price.csv", "Pokemon.csv", "data.csv"]
selected_dataset = st.sidebar.selectbox("İncelemek istediğiniz veri setini seçin:", dataset_options)

df = pd.read_csv(f"Data/{selected_dataset}")

st.sidebar.header('İşlem Seçiniz')


def main():
    activities = ['Veri İnceleme', 'Görselleştirme']
    option = st.sidebar.selectbox('Seçenekleri Seçin:', activities)

    if option == 'Veri İnceleme':
        st.subheader("Veri İnceleme")
        st.dataframe(df.head(50))

        if st.checkbox("Şekli Göster"):
            st.write(df.shape)
        if st.checkbox("Sütunları Göster"):
            st.write(df.columns)
        if st.checkbox("Genel Bilgileri İçin Birden Fazla Sütun Seç"):
            selected_columns = st.multiselect('Tercih edilen sütunları seçin:', df.columns)
            df1 = df[selected_columns]
            st.dataframe(df1)

            if st.checkbox("Özet Göster"):
                st.write(df1.describe().T)

        if st.checkbox('Boş Değerleri Göster'):
            st.write(df.isnull().sum())

        if st.checkbox("Veri tiplerini göster"):
            st.write(df.dtypes)
        if st.checkbox('Veri sütunlarının korelasyonunu göster'):
            st.write(df.corr())

    elif option == 'Görselleştirme':
        st.subheader("Veri Görselleştirme")
        st.dataframe(df.head(50))
        if st.checkbox('Birden çok sütunu çizmek için seçin'):
            selected_columns = st.multiselect('Tercih edilen sütunları seçin:', df.columns)
            df1 = df[selected_columns]
            st.dataframe(df1)

            if st.checkbox('Isı Haritası Göster'):
                st.write(sns.heatmap(df1.corr(), vmax=1, square=True, annot=True, cmap='viridis'))
                st.pyplot()

            if st.checkbox('Çift Grafik Göster'):
                st.write(sns.pairplot(df1, diag_kind='kde'))
                st.pyplot()

            if st.checkbox('Pasta Grafiği Göster'):
                all_columns = df.columns.to_list()
                pie_columns = st.selectbox("Görüntülemek için sütun seçin", selected_columns)
                pieChart = df1[pie_columns].value_counts().plot.pie(autopct="%1.1f%%")
                st.write(pieChart)
                st.pyplot()

            if st.checkbox('Histogram Göster'):
                histogram = df1.plot.hist()
                st.pyplot()

            if st.checkbox('Alan Grafiği (Yığınlanmış) Göster'):
                stacked_area_chart = df1.plot.area(stacked=True)
                st.pyplot()

            if st.checkbox('Dağılım Grafiği (Hexbin) Göster'):
                if len(selected_columns) >= 2:
                    hexbin_plot = df1.plot.hexbin(x=selected_columns[0], y=selected_columns[1], gridsize=10)
                    st.pyplot()
                else:
                    st.write("En az 2 sütun seçmelisiniz.")

            if st.checkbox('Kutu Grafiği (Yatay) Göster'):
                box_plot = df1.plot.box(vert=False)
                st.pyplot()

            if st.checkbox('Çizgi Grafiği (Çoklu Sütun) Göster'):
                if len(selected_columns) >= 2:
                    line_chart = df1.plot.line(x=selected_columns[0], y=selected_columns[1:])
                    st.pyplot()
                else:
                    st.write("En az 2 sütun seçmelisiniz.")


if __name__ == '__main__':
    main()