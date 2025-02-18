from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name ='sentence-transformers/all-MiniLM-L6-v2')

# text = "Delhi is the capital of India"
documents = [
    "Delhi is the capital of India",
    "Paris is the capital of France",
    "Bhopal is the capital of MP"
]
vector = embedding.embed_documents(documents)
print(str(vector))