import argparse

class ArgumentParser:
    def __init__(self):
        # 初始化一个argparse.ArgumentParser对象，并设置描述信息
        self.parser = argparse.ArgumentParser(description='Translate English PDF book to Chinese.')
        # 添加命令行参数
        self.parser.add_argument('--config', type=str, default='config.yaml', help='Configuration file with model and API settings.') # 给出配置yaml文件的路径
        self.parser.add_argument('--model_type', type=str, required=True, choices=['GLMModel', 'OpenAIModel'], help='The type of translation model to use. Choose between "GLMModel" and "OpenAIModel".')   
        # glm模型参数
        self.parser.add_argument('--glm_model', type=str, help='The model name of GLM Model. Required if model_type is "GLMModel".')
        self.parser.add_argument('--glm_model_url', type=str, help='The URL of the ChatGLM model URL.')
        self.parser.add_argument('--glm_api_key', type=str, help='The API key for GLMModel. Required if model_type is "GLMModel".')
        self.parser.add_argument('--timeout', type=int, help='Timeout for the API request in seconds.')
        # openai gpt模型参数
        self.parser.add_argument('--openai_model', type=str, help='The model name of OpenAI Model. Required if model_type is "OpenAIModel".')
        self.parser.add_argument('--openai_api_key', type=str, help='The API key for OpenAIModel. Required if model_type is "OpenAIModel".')
        # 输出格式参数
        self.parser.add_argument('--book', type=str, help='PDF file to translate.')
        self.parser.add_argument('--file_format', type=str, help='The file format of translated book. Now supporting PDF and Markdown')
        self.parser.add_argument('--target_language', type=str, help='The target language of translated book. ')

    def parse_arguments(self):
        # 解析命令行参数，并将结果存储在args中
        args = self.parser.parse_args()
        # 检查如果model_type是openaimodel，且没有提供openai_model或者openai_api_key，则报错
        if args.model_type == 'OpenAIModel' and not args.openai_model and not args.openai_api_key:
            self.parser.error("--openai_model and --openai_api_key is required when using OpenAIModel")
        return args
