from collections import Counter

import streamlit as st
import pandas as pd
import altair as alt
import graphviz

import ner


example = (
    "My name is Percy Jackson.\n"
    "I'm twelve years old. Until a few months ago, I was a boarding student at Yancy Academy, "
    "a private school for troubled kids in upstate New York.\n"
    "Am I a troubled kid?\n"
    "Yeah. You could say that.")


# st.set_page_config(layout='wide')
st.markdown('## spaCy Visualization')

view = st.sidebar.radio('View', ('Entities', 'Dependencies'))

text = st.text_area('Text to process', value=example, height=100)

doc = ner.SpacyDocument(text)

if view == 'Entities':
    entities = doc.get_entities()
    tokens = doc.get_tokens()
    counter = Counter(tokens)
    words = list(sorted(counter.most_common(30)))

    # https://pandas.pydata.org
    chart = pd.DataFrame({
        'frequency': [w[1] for w in words],
        'word': [w[0] for w in words]})

    # https://pypi.org/project/altair/
    bar_chart = alt.Chart(chart).mark_bar().encode(x='word', y='frequency')

    st.markdown(f'Total number of tokens: {len(tokens)}<br/>'
                f'Total number of types: {len(counter)}', unsafe_allow_html=True)

    # https://docs.streamlit.io/library/api-reference/data/st.table
    st.table(entities)

    # https://docs.streamlit.io/library/api-reference/charts/st.altair_chart
    st.altair_chart(bar_chart)

else:
    dependencies = doc.get_parse()
    sentence_dependencies = doc.get_parse_per_sent()

    tab1, tab2 = st.tabs(('Table', 'Graph'))
    with tab1:
        st.table(dependencies.values())
    with tab2:
        for sentence in sentence_dependencies:
            graph = graphviz.Digraph()
            for dependency in sentence:
                graph.edge(sentence[dependency][2], sentence[dependency][0], label=sentence[dependency][1])
            st.graphviz_chart(graph)
