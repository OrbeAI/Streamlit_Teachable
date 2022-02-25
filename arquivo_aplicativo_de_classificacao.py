from arquivo_classificador_de_imagem import funcao_classificar_imagem
import streamlit as st
from PIL import Image

# 03.Criar os elementos que compõe o aplicativo.
# TÍTULO DO SITE.
st.title("Classificador de milho.")

# BOTÃO PARA FAZER UPLOAD DA IMAGEM A SER CLASSIFICADA.
uploaded_file = st.file_uploader("Escolha um arquivo", type="jpg")

# CLASSIFICAÇÃO DA IMAGEM.
if uploaded_file is not None:

    # ABRIR A IMAGEM CARREGADA.
    image = Image.open(uploaded_file)

    # MOSTRAR A IMAGEM.
    st.image(image, caption='', use_column_width=True)

    # TEXTO INDICANDO QUE A IMAGEM ESTÁ SENDO CLASSIFICADA.
    st.write("Classificando...")

    # CHAMAR A FUNÇÃO DE CLASSIFICAÇÃO DE IMAGEM
    # E ARMAZENAR O RESULTADO NA VARIÁVEL LABEL.
    label = funcao_classificar_imagem(image, 'keras_model.h5')

    # CONDICIONAL PARA IDENTIFICAR A CLASSE DA IMAGEM.
    if label == 1:

       # INSIRA O NOME DA PRIMEIRA CLASSE.
       st.write("Milho bom.")

    else:

       # INSIRA O NOME DA SEGUNDA CLASSE.
       st.write("Milho ruim.")
