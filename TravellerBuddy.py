"""TravellerBuddy.ipynb

Shareable file is located at
    https://colab.research.google.com/drive/1kxJ6352BrFxdCTnQqN9maEPkGMI1FESy?usp=sharing

# Gen AI

---                   
                                                              BY: SATYAM PRAKASH
---
"""

# !pip install langchain
# !pip install openai
# !pip install gradio
# !pip install huggingface_hub
# !pip install langchain_community
# !pip install langchain-google-genai

import os
import gradio as gr
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain, PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")


from langchain_google_genai import ChatGoogleGenerativeAI

# Try creating a Gemini Flash 2.0 model
try:
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    response = llm.invoke("Hello Gemini, can you hear me?")
    print("✅ API is working!")
    print("Response:", response.content)
except Exception as e:
    print("❌ API Error:", str(e))

template = """As an adventurous and globetrotting college student named Onix, you're constantly on the lookout for new cultures, experiences, and breathtaking landscapes. You've visited numerous countries, immersing yourself in local traditions, and you're always eager to swap travel stories and offer tips on exciting destinations
{chat_history}
User: {user_message}
Chatbot:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "user_message"], template=template
)


from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory(memory_key="chat_history")

llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory
)

def get_text_response(user_message, history):
    # LangChain memory handles the history internally
    response = llm_chain.predict(user_message=user_message)
    return response

# # Gradio Chat Interface
# demo = gr.ChatInterface(
#     fn=get_text_response,
#     examples=[
#         "How are you doing?",
#         "What are your interests?",
#         "Which places do you like to visit?"
#     ]
# )

demo = gr.ChatInterface(get_text_response, examples=["How are you doing?","What are your interests?","Which places do you like to visit?"], type='messages')

if __name__ == "__main__":
    demo.launch() #To create a public link, set `share=True` in `launch()`. To enable errors and logs, set `debug=True` in `launch()`.


