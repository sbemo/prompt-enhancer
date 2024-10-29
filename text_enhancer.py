from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from openai import OpenAI
import yaml
import os

# 设备选择（CUDA 或 CPU）
device = "cuda" if torch.cuda.is_available() else "cpu"

# 模型检查点路径
MODEL_CHECKPOINT = "./model" 

class TextEnhancer:
    def __init__(self, model_checkpoint=MODEL_CHECKPOINT, prefix="enhance prompt: ", max_target_length=256):
        self.prefix = prefix
        self.max_target_length = max_target_length
        self.tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)
        self.enhancer = pipeline(
            'text2text-generation',
            model=self.model,
            tokenizer=self.tokenizer,
            repetition_penalty=1.2,
            device=0 if device == "cuda" else -1
        )

        # 加载配置文件中的 OpenAI API 信息
        config = self.load_config("config.yaml")
        self.api_key = config["openai"]["api_key"]
        self.base_url = config["openai"]["base_url"]

    def flux_enhance_prompt(self, prompt):
        input_text = self.prefix + prompt
        generated_response = self.enhancer(input_text, max_length=self.max_target_length)
        enhanced_text = generated_response[0]['generated_text']
        return enhanced_text

    def mj_enhance_prompt(self, yaml_file_path: str, user_message: str) -> str:
        # 加载系统提示词
        system_prompt = self.load_preset_prompts(yaml_file_path)

        # 初始化 OpenAI 客户端
        client = OpenAI(api_key=self.api_key, base_url=self.base_url)
        
        # 调用模型并获取响应
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )
        
        # 返回模型生成的内容
        return response.choices[0].message.content

    @staticmethod
    def load_preset_prompts(file_path: str) -> str:
        with open(file_path, 'r', encoding='utf-8') as file:
            preset_prompts = yaml.safe_load(file)
        return preset_prompts['system_prompt']

    @staticmethod
    def load_config(file_path: str) -> dict:
        """
        加载配置文件，用于获取API key和base URL等信息。
        
        参数:
        - file_path (str): 配置文件的路径。
        
        返回:
        - (dict): 配置文件的内容。
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
        return config
