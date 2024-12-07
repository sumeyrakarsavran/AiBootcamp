import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

model=load_model('my_cnn_model2.h5')

def process_image(img):
    img=img.resize((30,30)) #boyutunu 170 x 170 pixel yaptik
    img=np.array(img)
    img=img/255.0 #normalize ettik
    img=np.expand_dims(img,axis=0) #np tek bir array old için expand ediyoruz tek bir arraye dönştürüyoruz
    return img

st.title("Trafik İsareti Tespiti")
st.write("Resim sec ve tahmin etsin")

file=st.file_uploader('Bir Resim Sec',type=['jpg','jpeg','png'])

if file is not None:
    img=Image.open(file) #cv2 ile değil bu sefer image ile açıyoruz
    st.image(img,caption='yuklenen resim') 
    image= process_image(img) #yuklenen resme diğer resimlere yaptığımız processi yapıyoruz
    prediction=model.predict(image)
    predicted_class=np.argmax(prediction) #ihtimal yüzde elliden fazlaysa argmaxla 1, azsa 0 yapıyoruz

    class_names=['Kanser Degil','Kanser']
    st.write(predicted_class) #0sa kanser değil 1se kanser yazdırcak
    st.write(prediction)
