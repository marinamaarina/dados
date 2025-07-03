import streamlit as st
import pandas as pd

def main():
    st.title("Organizador de Grupos e Subgrupos")

    uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])

    if uploaded_file is not None:
        # Lê o arquivo CSV
        df = pd.read_csv(uploaded_file)

        # Mostra as primeiras linhas para verificar
        st.write("Visualização dos dados:")
        st.dataframe(df)

        # Exemplo de agrupamento por "Grupo", "Subgrupo"
        if "Grupo" in df.columns and "Subgrupo" in df.columns and "Descrição" in df.columns:
            st.write("Dados organizados por grupo e subgrupo:")

            # Agrupando e exibindo por grupo
            grupos = df["Grupo"].unique()
            for grupo in grupos:
                st.subheader(f"Grupo: {grupo}")
                subset = df[df["Grupo"] == grupo]
                st.table(subset[["Subgrupo", "Descrição"]])
        else:
            st.warning("O arquivo CSV deve conter as colunas: Grupo, Subgrupo e Descrição.")

if __name__ == "__main__":
    main()

