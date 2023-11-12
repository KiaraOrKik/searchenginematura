import streamlit as st
st.set_page_config(layout="wide")

def main():
    st.title(":thread: Collegamenti per l'esame di Maturità")
    st.markdown("Benvenutə al database per eccellenza dei collegamenti per l'esame di Maturità")
    st.markdown("****")
    st_search, buzz1, st_suggestion = st.columns([10, 1, 10])
    with st_search:
        st.header(":mag: Ricerca")
        st.markdown("""**Hai trovato un argomento che ti ricorda qualcosa, ma dopo 6 mesi di scuola ti sfugge cosa sia?  
                    Cerca qui a cosa si può collegare e preparati al meglio per l'esame.**""")

    with st_suggestion:
        st.header(":left_speech_bubble: Suggerimenti")
        st.markdown("""**Ricordi di qualche collegamento che manca, o pensi che qualcosa sia incorretto?  
        Qui troverai il modulo Google dove poter inviare il feedback. (work in progress)**""")


if __name__ == '__main__':
    main()
