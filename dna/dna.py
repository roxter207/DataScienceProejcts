import pandas as pd
import streamlit as st
import altair as alt


st.write("""DNA Nucleotide Count Web App""")


st.header("INPUT (DNA QUERY)")

sequence_input = ">DNA Query\nTAGCTGACGATCGTAGCATGTGCTA\nGATAGTGGTACTCGACGCTCGTAGA\nCTAGTAGCTAGCGATCGTAGCTAGC"
sequence = st.text_area("SEQUENCE input", sequence_input, height=25)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)


st.warning("""****""")

st.header('INPUT (DNA QUERY)')
st.header("OUTPUT DNA COUNT")


#print dictionary

st.subheader('1.Print dictionary')
def DNA_count(seq):
    d=dict([
        ('A'.seq.count('A')),
        ('T'.seq.count('T')),
        ('G'.seq.count('G')),
        ('C'.seq.count('C')),
    ])
    return d


X = DNA_count(sequence)
X_values = list(X.values())

X

#print test
st.subheader("2. Print text")
st.write('There are '+str(X['A'])+'A')
st.write('There are '+str(X['T'])+'T')
st.write('There are '+str(X['G'])+'G')
st.write('There are '+str(X['C'])+'C')



st.subheader('3.Dispaly DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0:'count'},axis='columns')
df.reset_index(inplace=True)
st.write(df)


###4.displar bar chart

st.subheader('4.Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x = 'nucleotide',
    y = 'count'
)

p = p.properties(
    width=alt.Step(80)
)
st.write(p)

