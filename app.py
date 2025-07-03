import streamlit as st
import pandas as pd
from PIL import Image
import os

# Carregar dados
df = pd.read_csv("dados.csv")

# Agrupar por 'Grupo'
grupos = df['Grupo'].unique()

st.title("Análise de Testes de Liveness")
st.markdown("Visualização dos grupos, subgrupos e descrições com imagens de exemplo.")

for grupo in grupos:
    st.header(grupo)

    grupo_df = df[df['Grupo'] == grupo]

    for i, row in grupo_df.iterrows():
        subgrupo = row['Subgrupo']
        descricao = row['Descrição']

        st.subheader(f"🔹 {subgrupo}")
        st.write(descricao)

        # Mostrar imagem se existir com o nome do subgrupo
        imagem_path = f"imagens/{subgrupo.lower().replace(' ', '_')}.jpg"
        if os.path.exists(imagem_path):
            st.image(Image.open(imagem_path), caption=subgrupo)
        else:
            st.info("📷 Nenhuma imagem disponível para este item.")
