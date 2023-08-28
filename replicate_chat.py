from langchain.chains import ConversationChain
from langchain.memory import VectorStoreRetrieverMemory
from langchain.vectorstores import Pinecone
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import Replicate

os.environ["REPLICATE_API_TOKEN"] = "api_key"


c = "zeke/nyu-llama-2-7b-chat-training-test:aae0f2ef9dd402d20aba3e83adcbb7ab8fb55fdc3081d14abb6aa082b181c981"
def chat(model , conversationid ,index_name , knowledge , environment ,api_key , text_input ) : 
    llm = Replicate(
        model=model ,
        input={"temperature": 1, "max_length": 2048, "top_p": 1},
    )
    chat = ConversationChain(
            llm=llm,
            verbose=False)
    chat.prompt.template = \
        """
        ###User:

        Personal details :
        {history}

        Current conversation:
        ###User: {input}
        ###Assistant:"""
    return chat.predict(input=text_input)
