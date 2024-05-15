import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import ArgumentParser, ConfigLoader, LOG
from model import GLMModel, OpenAIModel
from translator import PDFTranslator

if __name__ == "__main__":
    # 实例化argument_parser类，解析命令行参数，结果存储在args中。
    argument_parser = ArgumentParser()
    args = argument_parser.parse_arguments()
    # 使用解析得到的配置文件路径实例化ConfigLoader类，加载配置文件，结果存储在cofig字典中
    config_loader = ConfigLoader(args.config)
    config = config_loader.load_config()
    
    # 确定使用的模型名称，优先使用命令行参数中的值，否则使用配置文件中的值
    openai_model_name = args.openai_model if args.openai_model else config['OpenAIModel']['model']
    glm_model_name = args.openai_model if args.glm_model else config['GLMModel']['model']
    # 确定使用的api密钥，优先使用命令行参数中的值，否则使用配置文件中的值
    openai_api_key = args.openai_api_key if args.openai_api_key else config['OpenAIModel']['api_key']
    glm_api_key = args.glm_api_key if args.glm_api_key else config['GLMModel']['api_key']
    glm_model_url = args.glm_model_url if args.glm_model_url else config['GLMModel']['model_url']
    model_type = args.model_type
    timeout = args.timeout if args.timeout else config['GLMModel']['timeout']
    
    # 实例化openaimodel类，使用指定的模型名称和api密钥
    if model_type == "OpenAIModel":
        model = OpenAIModel(model=openai_model_name, api_key=openai_api_key)
    elif model_type == "GLMModel":
        model = GLMModel(model=glm_model_name,model_url=glm_model_url,api_key = glm_api_key,timeout=timeout)

    # 确定要翻译的pdf文件路径，优先使用命令行参数中的值，否则使用配置文件中的值
    pdf_file_path = args.book if args.book else config['common']['book']
    # 确定文件格式，优先使用命令行参数中的值，否则使用配置文件中的值
    file_format = args.file_format if args.file_format else config['common']['file_format']
    target_language = args.target_language if args.target_language else config['common']['target_language']

    # 实例化 PDFTranslator 类，并调用 translate_pdf() 方法
    translator = PDFTranslator(model)
    # 翻译指定的pdf文件
    translator.translate_pdf(pdf_file_path, file_format,target_language)
