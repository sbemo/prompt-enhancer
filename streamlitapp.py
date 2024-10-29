import streamlit as st
import requests

# 获取 Flask API 的 URL
FLASK_API_URL = 'http://127.0.0.1:5000'

# 设置页面配置
st.set_page_config(
    page_title="Prompt Enhancer",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 现代简约风格的 CSS
st.markdown("""
    <style>
    /* 主容器样式 */
    .main {
        padding: 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    /* 标题样式 */
    h1 {
        color: #1E1E1E;
        font-weight: 600;
        font-size: 2.5rem !important;
        margin-bottom: 2rem !important;
        letter-spacing: -0.5px;
    }
    
    /* 子标题样式 */
    h3 {
        color: #2E2E2E;
        font-weight: 500;
        font-size: 1.5rem !important;
        margin: 1.5rem 0 !important;
    }
    
    /* 按钮样式 */
    .stButton > button {
        background: linear-gradient(90deg, #3498db, #2980b9);
        color: white;
        padding: 0.6rem 1.5rem;
        font-size: 1rem;
        font-weight: 500;
        border-radius: 8px;
        border: none;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* 输入框样式 */
    .stTextInput > div > div > input {
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 8px;
        padding: 0.8rem;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #3498db;
        box-shadow: 0 0 0 2px rgba(52,152,219,0.2);
    }
    
    /* 文本区域样式 */
    .stTextArea > div > div > textarea {
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 8px;
        padding: 0.8rem;
        font-size: 1rem;
        min-height: 120px;
    }
    
    /* 分割线样式 */
    hr {
        margin: 2rem 0;
        border: none;
        border-top: 1px solid #e9ecef;
    }
    
    /* 警告消息样式 */
    .stAlert {
        background-color: #fff3cd;
        color: #856404;
        padding: 0.75rem;
        border-radius: 8px;
        border: 1px solid #ffeeba;
    }
    </style>
    """, unsafe_allow_html=True)

# 页面标题
st.title("✨ Prompt Enhancer")

# 初始化 session_state
if 'flux_enhanced_text' not in st.session_state:
    st.session_state['flux_enhanced_text'] = ""
if 'mj_enhanced_text' not in st.session_state:
    st.session_state['mj_enhanced_text'] = ""

# Flux 提示词部分
st.subheader("Flux 提示词增强")
flux_prompt = st.text_input(
    "输入基础提示词",
    key="flux_prompt_input",
    placeholder="在此输入您的 Flux 提示词..."
)

col1, col2 = st.columns([1, 4])
with col1:
    if st.button("增强提示词", key="flux_button"):
        if flux_prompt:
            with st.spinner('正在增强提示词...'):
                flux_url = f"{FLASK_API_URL}/flux-enhanceprompt"
                response = requests.post(flux_url, json={"prompt": flux_prompt})
                st.session_state['flux_enhanced_text'] = response.json().get("response", "增强失败，请检查服务连接")
        else:
            st.warning("请输入提示词")

st.text_area(
    "增强结果",
    value=st.session_state['flux_enhanced_text'],
    height=120,
    key="flux_result"
)

st.markdown("---")

# MJ 提示词部分
st.subheader("MJ 提示词增强")
mj_prompt = st.text_input(
    "输入基础提示词",
    key="mj_prompt_input",
    placeholder="在此输入您的 MJ 提示词..."
)

col3, col4 = st.columns([1, 4])
with col3:
    if st.button("增强提示词", key="mj_button"):
        if mj_prompt:
            with st.spinner('正在增强提示词...'):
                mj_url = f"{FLASK_API_URL}/mj-enhanceprompt"
                response = requests.post(mj_url, json={"prompt": mj_prompt})
                st.session_state['mj_enhanced_text'] = response.json().get("response", "增强失败，请检查服务连接")
        else:
            st.warning("请输入提示词")

st.text_area(
    "增强结果",
    value=st.session_state['mj_enhanced_text'],
    height=120,
    key="mj_result"
)
