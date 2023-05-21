import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

st.write("""

## Pokemon Veri Seti İnceleme
Pokemon Veri Seti **İnceleme** ve **Görselleştirme**

""")
df = pd.read_csv("Pokemon/Pokemon.csv")
df.head()
st.sidebar.header('Grafik Bileşenlerini Seçiniz')

def user_input_features(df):
    x_component = st.sidebar.selectbox('X Bileşeni', df.columns)
    y_component = st.sidebar.selectbox('Y Bileşeni', df.columns)
    grafik_secimi = st.sidebar.selectbox('Grafik Türü Seçiniz', ('Çizgi Grafiği', 'Çubuk Grafiği', 'Pasta Grafiği', 'Histogram', 'Dağılım Grafiği', 'Heatmap', 'Gözlük Grafiği', 'Kutu Grafiği', 'Alan Grafiği', 'Radar Grafiği'))
    
    data = {'X Bileşeni': x_component,
            'Y Bileşeni': y_component,
            'Grafik Seçimi': grafik_secimi}
    features = pd.DataFrame(data, index=[0])
    return features

selected_components = user_input_features(df)

st.subheader('Seçilen Grafik Bileşenleri')
st.write(selected_components)

if selected_components['Grafik Seçimi'].iloc[0] == 'Çizgi Grafiği':
    st.subheader('Çizgi Grafiği')
    x = df[selected_components['X Bileşeni'].iloc[0]]
    y = df[selected_components['Y Bileşeni'].iloc[0]]
    
    plt.plot(x, y)
    st.pyplot(plt)

elif selected_components['Grafik Seçimi'].iloc[0] == 'Çubuk Grafiği':
    st.subheader('Çubuk Grafiği')
    x = df[selected_components['X Bileşeni'].iloc[0]]
    y = df[selected_components['Y Bileşeni'].iloc[0]]
    
    plt.bar(x, y)
    st.pyplot(plt)

elif selected_components['Grafik Seçimi'].iloc[0] == 'Pasta Grafiği':
    st.subheader('Pasta Grafiği')
    column = selected_components['X Bileşeni'].iloc[0]
    
    plt.figure(figsize=(6, 6))
    df[column].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.axis('equal')
    st.pyplot(plt)

elif selected_components['Grafik Seçimi'].iloc[0] == 'Histogram':
    st.subheader('Histogram')
    column = selected_components['X Bileşeni'].iloc[0]
    
    plt.hist(df[column])
    st.pyplot(plt)

elif selected_components['Grafik Seçimi'].iloc[0] == 'Dağılım Grafiği':
    st.subheader('Dağılım Grafiği')
    x = df[selected_components['X Bileşeni'].iloc[0]]
    y = df[selected_components['Y Bileşeni'].iloc[0]]
    
    plt.scatter(x, y)
    st.pyplot(plt)

elif selected_components['Grafik Seçimi'].iloc[0] == 'Heatmap':
    st.subheader('Heatmap')
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    st.pyplot(plt)
    

elif selected_components['Grafik Seçimi'].iloc[0] == 'Gözlük Grafiği':
    st.subheader('Gözlük Grafiği')
    column = selected_components['X Bileşeni'].iloc[0]
    
    plt.figure(figsize=(10, 8))
    sns.boxplot(x=df[column], y=df[selected_components['Y Bileşeni'].iloc[0]])
    st.pyplot(plt)

elif selected_components['Grafik Seçimi'].iloc[0] == 'Kutu Grafiği':
    st.subheader('Kutu Grafiği')
    column = selected_components['X Bileşeni'].iloc[0]
    
    plt.boxplot(df[column])
    st.pyplot(plt)

elif selected_components['Grafik Seçimi'].iloc[0] == 'Alan Grafiği':
    st.subheader('Alan Grafiği')
    x = df[selected_components['X Bileşeni'].iloc[0]]
    y = df[selected_components['Y Bileşeni'].iloc[0]]
    
    plt.fill_between(x, y)
    st.pyplot(plt)

elif selected_components['Grafik Seçimi'].iloc[0] == 'Radar Grafiği':
    st.subheader('Radar Grafiği')
    x = df[selected_components['X Bileşeni'].iloc[0]]
    y = df[selected_components['Y Bileşeni'].iloc[0]]
    
    plt.polar(x, y)
    st.pyplot(plt)
