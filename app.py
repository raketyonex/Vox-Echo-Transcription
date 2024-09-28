import streamlit as st
from sp_rec import transcriber

st.set_page_config(page_icon="🗣️", page_title="VoxEcho")
st.markdown("## **VoxEcho**")
st.markdown("##### Say And Play Words Display!")
st.divider()

s1, s2 = st.columns([1,1])
with s1:
    audio = st.file_uploader("Pick audio file", type=['mp3', 'wav', 'mp4'])
    b1, b2 = st.columns([1,2])
    with b1:
        btn = st.button("Transcribe")
    st.divider()

with s2:
    if btn and audio:
        with b2:
            with st.spinner("Transcribing..."):
                with s2:
                    placeholder = st.empty()
                    alltext = ""
                    for text in transcriber(audio):
                        alltext += f"{text}\n"
                        placeholder.text_area("VoxEcho thinks you said:", value=alltext, height=450)
        with s1:
            st.success("Transcription complete!")
    else:
        st.text_area("Text will display here:", height=450, disabled=True)