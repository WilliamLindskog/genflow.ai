# File: llm.py

from langchain.llms import CTransformers

# Local CTransformers wrapper for Llama-2-7B-Chat
llama_path = './src/llama'


llm = CTransformers(
    model = f'{llama_path}/llama-2-7b-chat.ggmlv3.q8_0.bin', # Location
    model_type = 'llama', # Model type llama
    config = {
        'max_new_tokens' : 256, 
        'temperature' : 0.01
    }
)