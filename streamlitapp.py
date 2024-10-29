import streamlit as st
import requests

# 获取 Flask API 的 URL
FLASK_API_URL = 'http://127.0.0.1:5000'

# 设置页面标题和样式
st.set_page_config(page_title="Prompt Enhancer", layout="centered")
st.title("🔍 Prompt Enhancer")
st.markdown(
    """
    <style>
    .stButton > button {
        background-color: #5A5A5A;
        color: white;
        font-size: 18px;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
    }
    .stTextInput > div > div > input {
        font-size: 16px;
        padding: 10px;
    }
    .stTextArea > div > div > textarea {
        font-size: 16px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 初始化 session_state 用于保存按钮生成的结果
if 'flux_enhanced_text' not in st.session_state:
    st.session_state['flux_enhanced_text'] = ""
if 'mj_enhanced_text' not in st.session_state:
    st.session_state['mj_enhanced_text'] = ""

# 显示两个输入框和按钮，用于分别增强 Flux 和 MJ 提示词
st.subheader("Flux 提示词增强")
flux_prompt = st.text_input("输入 Flux 基础提示词:", key="flux_prompt_input")

if st.button("Flux 提示词增强"):
    if flux_prompt:
        flux_url = f"{FLASK_API_URL}/flux-enhanceprompt"
        response = requests.post(flux_url, json={"prompt": flux_prompt})
        st.session_state['flux_enhanced_text'] = response.json().get("response", "增强失败，请检查服务连接")
    else:
        st.warning("请先输入 Flux 提示词")
# 显示 Flux 增强的结果
st.text_area("Flux 增强结果:", value=st.session_state['flux_enhanced_text'], height=150)

st.subheader("MJ 提示词增强")
mj_prompt = st.text_input("输入 MJ 基础提示词:", key="mj_prompt_input")

if st.button("MJ 提示词增强"):
    if mj_prompt:
        mj_url = f"{FLASK_API_URL}/mj-enhanceprompt"
        response = requests.post(mj_url, json={"prompt": mj_prompt})
        st.session_state['mj_enhanced_text'] = response.json().get("response", "增强失败，请检查服务连接")
    else:
        st.warning("请先输入 MJ 提示词")
# 显示 MJ 增强的结果
st.text_area("MJ 增强结果:", value=st.session_state['mj_enhanced_text'], height=150)
