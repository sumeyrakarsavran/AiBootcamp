import streamlit as st
import pandas as pd
import plotly.express as px

st.title('MLOps Streamlit Apps :coffee:') #web sitenin başlığı
#html css vs hepsinin arka planda kendi yazıyo
st.slider('Bir rakam sec',1,100)
st.audio('data/song.mp3')

menu=["Anasayfa","Makine Ogrenmesi",'AI','Contact Us', 'About Us']
st.sidebar.selectbox('Menu',menu)
df=pd.read_csv('data/prog_languages_data.csv')
fig=px.pie(df,values='Sum')
st.plotly_chart(fig)

fig2=px.bar(df,x='lang',y='Sum')
st.plotly_chart(fig2)

file=st.file_uploader('Dosyayi yukle')
st.success("Basarili")
st.error('bir hata olustu')
st.warning('Yok yok olmamis bu')
st.info("bu odevde biraz daha calismaniz lazim")
st.code("""
    import pandas as pd
    df=pd.read_excel('cars.xlsx')
    """)


isim=st.text_input('Isminizi girini',max_chars=20)
#st.video('data/secret_of_success.mp4')
#st.camera_input('camera')

st.date_input('tarih sec')
st.time_input('saat sec')
st.text_input('sifrenizi girirni',type='password')
st.text_area('Mesajiniz',height=80)
st.number_input('Yasinizi Girinit',1,100)
st.radio("Medeni Durumu", ('Evli','Bekar','Dul','Nisanli'))
st.selectbox('BildiginizProgramlara dilleri',['C++','Python','HTML','Java','Julia','Q#'])
st.multiselect('BildiginizProgramlara dilleri',['C++','Python', 'HTML','Java','Julia','Q#' ])
#st.video('http://192.168.1.117:8080/video') #burda çalışmadı ama url u croma yazınca çalisiyo
st.image('data/image_01.jpg')
st.divider()
df=pd.read_csv('data/iris.csv')
#st.table(df)
st.write(df)

