from langchain.chains import StuffDocumentsChain, LLMChain, ConversationalRetrievalChain
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langcahin.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
import chromadb
import yaml



with open("config.yaml", "r") as f:
    # config = yaml.load(f, Loader=yaml.FullLoader)
    config = yaml.safe_load(f)


def create_llm(model_path = config["model_path"]["large"], model_type=config["model_type"]):
    llm = CTransformers(model_path, model_type)
    return llm

def create_embeddings(embeddings_path = config['embeddings_path']):
    return HuggingFaceInstructEmbeddings(embeddings_path)

def create_chat_memory(chat_history):
    return ConversationBufferMemory(memory_key="history", chat_history=chat_history, k=5)


def create_prompt_from_template(template):
    return PromptTemplate.from_template(template)

def create_llm_chain():
    pass


def load_normal_chain():
    pass


class ChatChain:
    def __init__(self) -> None:
        pass
        