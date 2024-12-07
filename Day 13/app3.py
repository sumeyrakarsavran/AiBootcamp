import streamlit as st
import pickle
import numpy as np
from sklearn.neighbors import NearestNeighbors
from PIL import Image

import numpy as np
import pickle as pkl
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50,preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPool2D
from sklearn.neighbors import NearestNeighbors
import os
from numpy.linalg import norm


# Başlık ve açıklama
st.title("Ürün Öneri Sistemi")
st.write("Bu uygulama, seçtiğiniz ürüne benzer ürünleri önerir.")

# Verileri Yükleme
def load_data():
    with open("filenames.pkl", "rb") as f:
        filenames = pickle.load(f)
    with open("Images_features.pkl", "rb") as f:
        image_features = pickle.load(f)
    return filenames, image_features

filenames, image_features = load_data()
st.write(np.array(image_features ).shape)


# KNN modelini oluşturma
neighbors = NearestNeighbors(n_neighbors=6, algorithm='brute', metric='euclidean')
neighbors.fit(image_features)

"""
# Ürün Özelliklerini Çıkartma Fonksiyonu (örnek)
def extract_features_from_images(image_path, model):
    # Bu fonksiyon, eğitmiş olduğunuz modeli kullanarak görüntüden özellik çıkaracak şekilde
    # tanımlanmalıdır. Burada bir placeholder olarak rastgele bir vektör döndürüyoruz.
    # Örneğin: feature_vector = model.predict(preprocessed_image)
    feature_vector = np.random.rand(1, image_features.shape[1])
    return feature_vector
"""

model = ResNet50(weights='imagenet', include_top=False, input_shape=(224,224,3))
model.trainable = False
model = tf.keras.models.Sequential([model,
                                   GlobalMaxPool2D()
                                   ])

def extract_features_from_images(image_path, model):

    #img = image.load_img(image_path, target_size=(224,224))
    img=image_path.resize((224,224))
    img_array = image.img_to_array(img)
    img_expand_dim = np.expand_dims(img_array, axis=0)
    img_preprocess = preprocess_input(img_expand_dim)

    result = model.predict(img_preprocess).flatten()
    norm_result = result/norm(result)
    return norm_result


# Kullanıcının bir ürün yüklemesi
uploaded_file = st.file_uploader("Bir ürün resmi yükleyin:", type=["jpg", "jpeg", "png"])

# Benzer Ürünleri Bulma ve Gösterme
if uploaded_file is not None:
    # Yüklenen resmi göster
    image = Image.open(uploaded_file)
    st.image(image, caption="Yüklenen Resim", use_column_width=True)
    
    # Özellikleri çıkarma
    input_image_features = extract_features_from_images(uploaded_file, model)
    
    # Benzer ürünleri bulma
    distances, indices = neighbors.kneighbors([input_image_features])
    
    # Benzer ürünleri göster
    st.write("Benzer ürün önerileri:")
    for i in range(1, len(indices[0])):  # 0. eleman kendisi olduğu için atlanır
        similar_image_path = filenames[indices[0][i]]
        similar_image = Image.open(similar_image_path)
        st.image(similar_image, width=150, caption=f"Benzer Ürün {i}")


