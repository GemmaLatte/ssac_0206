import streamlit as st
from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = st.secrets["api_key"]
st.title("이미지 생성기")

client = OpenAI()

with st.form("form"):
    user_input = st.text_input("느 아이디어 좀 내바라")
    size = st.selectbox("size", ['1024*1024', '512*512', '256*256'])
    submit = st.form_submit_button("Submit")
    
st.button("클릭")

gpt_prompt = [{"role":"system" ,"content":"your my averyting~ 별처럼 쏟아지는 느그 운명에~"
}]

gpt_prompt.append({"role":"user","content": user_input})

with st.spinner("기다��! ����� 기다��"):
    gpt_responce = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages=gpt_prompt
    )
    
    dalle_prompt = gpt_responce.choices[0].message.content
    st.write("dalle-e prompt:", dalle_prompt)
    
    with st.spinner("기다��! ����� 기다��"):
        dalle_responce = client.images.generate(
            model = 'dall-e-3',
            prompt=dalle_prompt,
            size = '1024x1024'
        )
    st.image(dalle_responce.data[0].url)