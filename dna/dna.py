import pandas as pd
import streamlit as st
import altair as alt


st.write("""DNA Nucleotide Count Web App""")


st.header("INPUT (DNA QUERY)")

sequence_input = ">DNA Query\nGAAACATCTGAAATGCATAGGCAAAGTAAGTTGATGATCTATCTGACCTGACTGATCGCGTAGA"
sequence = st.text_area("SEQUENCE input", sequence_input, height=25)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)


st.warning("""****""")

st.header('INPUT (DNA QUERY)')
st.header("OUTPUT DNA COUNT")

