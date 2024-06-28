# from dotenv import load_dotenv
# load_dotenv() ## loading all the environment variables

# import streamlit as st
# import os
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ## function to load Gemini Pro model and get repsonses
# model=genai.GenerativeModel("gemini-pro") 
# chat = model.start_chat(history=[])
# def get_gemini_response(question):
    
#     response=chat.send_message(question,stream=True)
#     return response

# ##initialize our streamlit app

# st.set_page_config(page_title="Q&A Demo")

# st.header("Gemini LLM Application")

# # Initialize session state for chat history if it doesn't exist
# if 'chat_history' not in st.session_state:
#     st.session_state['chat_history'] = []

# input=st.text_input("Input: ",key="input")
# submit=st.button("Ask the question")

# if submit and input:
#     response=get_gemini_response(input)
#     # Add user query and response to session state chat history
#     st.session_state['chat_history'].append(("You", input))
#     st.subheader("The Response is")
#     for chunk in response:
#         st.write(chunk.text)
#         st.session_state['chat_history'].append(("Bot", chunk.text))
# st.subheader("The Chat History is")
    
# for role, text in st.session_state['chat_history']:
#     st.write(f"{role}: {text}")
    









# from dotenv import load_dotenv
# load_dotenv()  # loading all the environment variables

# import streamlit as st
# import os
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Function to load Gemini Pro model and get responses
# model = genai.GenerativeModel("gemini-pro")
# chat = model.start_chat(history=[])

# def get_gemini_response(question):
#     response = chat.send_message(question, stream=True)
#     return response

# # Initialize Streamlit app
# st.set_page_config(page_title="Q&A Demo")

# st.header("Gemini LLM Application")

# # Initialize session state for chat history if it doesn't exist
# if 'chat_history' not in st.session_state:
#     st.session_state['chat_history'] = []

# input = st.text_input("Input: ", key="input")
# submit = st.button("Ask the question")

# if submit and input:
#     response = get_gemini_response(input)
#     # Add user query and response to session state chat history
#     st.session_state['chat_history'].append(("You", input))
#     response_text = ''.join(chunk.text for chunk in response)
#     st.session_state['chat_history'].append(("Bot", response_text))

# # Display chat history
# st.subheader("Chat History")

# for role, text in st.session_state['chat_history']:
#     with st.container():
#         if role == "You":
#             st.markdown(f"**{role}**: {text}")
#         else:
#             st.markdown(f"**{role}**: {text}")

# Alternative way to display chat history with each message in an expander
# st.subheader("Chat History")
# for i, (role, text) in enumerate(st.session_state['chat_history']):
#     with st.expander(f"{role} {i+1}"):
#         st.write(text)



from dotenv import load_dotenv
load_dotenv() 
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    response_text = ''.join(chunk.text for chunk in response)
    return response_text


# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("your Chatbot 🫂 ")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input you Question : ", key="input")
submit = st.button("Ask the question")

if submit and input:
    response = get_gemini_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input, "Bot", response))

# Display chat history
st.subheader("Your chatbot")

for user_role, user_text, bot_role, bot_text in st.session_state['chat_history']:
    with st.container():
        st.markdown(f"""
            <div style="padding: 10px; border-radius: 10px; background-color: #f0f0f5; margin-bottom: 10px; color: #000;">
                <strong>{user_role}</strong>: {user_text}
            </div>
            <div style="padding: 10px; border-radius: 10px; background-color: #e0f7fa; margin-bottom: 10px; color: #000;">
                <strong>{bot_role}</strong>: {bot_text}
            </div>
            """, unsafe_allow_html=True)



