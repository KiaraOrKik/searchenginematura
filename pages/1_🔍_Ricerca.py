import streamlit as st
import pandas as pd
url = f"https://docs.google.com/spreadsheets/d/17XPuqbqrvfq97j9pJr1cX6NKx5E3WMXUf0S3tgfYJx8/gviz/tq?tqx=out:csv&sheet=Databasematura"
df = pd.read_csv(url, dtype=str)
st.set_page_config(layout="wide")

def main():
    st.title(":mag: Ricerca")
    st.markdown("*Qui potrai cercare ogni argomento e tramite cosa collegarlo ad altri!*")
    text_search = st.text_input("Cerca un argomento", value="")
    ita = df["Italiano"].str.contains(text_search, na=False)
    eng = df["Inglese"].str.contains(text_search, na=False)
    sto = df["Storia"].str.contains(text_search, na=False)
    fil = df["Filosofia"].str.contains(text_search, na=False)
    lat = df["Latino"].str.contains(text_search, na=False)
    mate = df["Matematica"].str.contains(text_search, na=False)
    fis = df["Fisica"].str.contains(text_search, na=False)
    sci = df["Scienze"].str.contains(text_search, na=False)
    art = df["Storia dell'arte"].str.contains(text_search, na=False)
    civ = df["Educazione civica"].str.contains(text_search, na=False)
    df_search = df[ita|eng|sto|fil|lat|mate|fis|sci|art|civ]
    if text_search:
        st.write(df_search)


if __name__ == '__main__':
    main()