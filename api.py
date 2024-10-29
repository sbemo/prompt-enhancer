from flask import Flask, request, jsonify
from text_enhancer import TextEnhancer

# 初始化Flask应用
app = Flask(__name__)

# 创建TextEnhancer实例
text_enhancer = TextEnhancer()

# 固定 YAML 文件路径
YAML_FILE_PATH = "preset_prompts.yaml"

@app.route('/flux-enhanceprompt', methods=['POST'])
def flux_enhanceprompt():
    """
    Flask API接口，用于处理POST请求，通过TextEnhancer增强文本提示词。
    
    请求数据:
    - prompt (str): 输入的提示词，格式为JSON。
    
    返回:
    - JSON: 包含增强文本的响应，如果没有提供prompt则返回错误信息。
    """
    # 提取请求中的提示词
    data = request.get_json()
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    # 调用增强方法生成答案
    enhanced_text = text_enhancer.flux_enhance_prompt(prompt)

    # 返回中文格式的结果
    return jsonify({"response": enhanced_text})

@app.route('/mj-enhanceprompt', methods=['POST'])
def mj_enhanceprompt():
    """
    Flask API接口，用于处理POST请求，通过TextEnhancer的mj_enhance_prompt生成Midjourney增强提示词。
    
    请求数据:
    - prompt (str): 输入的用户提示词，格式为JSON。
    
    返回:
    - JSON: 包含增强提示词的响应，如果没有提供prompt则返回错误信息。
    """
    # 提取请求中的提示词
    data = request.get_json()
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    # 调用mj_enhance_prompt方法生成Midjourney增强提示词
    enhanced_text = text_enhancer.mj_enhance_prompt(YAML_FILE_PATH, prompt)

    # 返回中文格式的结果
    return jsonify({"response": enhanced_text})

# 启动Flask应用
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
