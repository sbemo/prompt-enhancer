# Prompt Enhancer

## 项目描述
Prompt Enhancer 是一个用于增强提示词的应用。该项目包含两个主要部分：
- Flask API：用于处理文本增强请求并返回增强结果。
- Streamlit 前端应用：提供用户界面，允许用户输入提示词并查看增强结果。

## 功能
- Flux 提示词增强：利用预训练模型增强输入提示词。
- MJ 提示词增强：调用 OpenAI 的 GPT-4 模型生成 Midjourney 风格的增强提示词。

# 项目结构
```bash
project-folder/
│
├── streamlitapp.py         # Streamlit 应用文件
├── api.py                  # Flask API 文件
├── text_enhancer.py        # 文本增强功能模块
├── preset_prompts.yaml     # 提示词配置文件
├── config.yaml             # 配置文件（API key 和 base URL）
├── model/                  # 预训练模型文件夹（已被 .gitignore 忽略）
└── requirements.txt        # 依赖文件
```

## 安装与配置

### 1. 克隆仓库
```bash
git clone https://github.com/sbemo/prompt-enhancer.git
cd prompt-enhancer
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 配置 API key 和 base URL
mj提示词扩充的接口必要条件，创建 config.yaml 文件，添加 OpenAI API 的密钥和 base URL（请参考模板）：
```yaml
openai:
  api_key: "your_api_key_here"
  base_url: "https://ganjiuwanshi.com/v1"
```

### 4. 下载模型
将必要的开源模型文件（flux提示词增强模型）放入 model/ 文件夹中（该文件夹已被 .gitignore 忽略，上传代码时不会上传模型文件）。

模型地址：https://huggingface.co/gokaygokay/Flux-Prompt-Enhance


### 5. 启动 Flask API（终端1）
```bash
python api.py
```

### 6. 启动 Streamlit 应用（终端2）
```bash
streamlit run streamlitapp.py
```

