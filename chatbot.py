import streamlit as st

st.set_page_config(page_title="Adarsh Chatbot")

st.title(" Adarsh Chatbot")

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
prompt = st.chat_input("Ask me anything...")

if prompt:

    # Show User Message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Convert to lowercase
    user_text = prompt.lower()

    # Bot Responses
    if "hi" in user_text or "hello" in user_text:
        response = "Hello! How can I help you?"

    elif "who are you" in user_text:
        response = "I am Adarsh Chatbot built using Python and Streamlit."

    elif "how are you" in user_text:
        response = "I am fine. Thank you for asking."

    elif "prime minister" in user_text:
        response = "Narendra Modi is the Prime Minister of India."

    elif "president" in user_text:
        response = "Droupadi Murmu is the President of India."

    elif "capital of india" in user_text:
        response = "New Delhi is the capital of India."

    elif "python" in user_text:
        response = "Python is a popular programming language."

    elif "artificial intelligence" in user_text or "ai" in user_text:
        response = "AI stands for Artificial Intelligence."

    elif "machine learning" in user_text:
        response = "Machine Learning is a branch of AI that learns from data."

    elif "your name" in user_text:
        response = "My name is Adarsh Chatbot."

    elif "thank you" in user_text:
        response = "You're welcome!"

    elif "good morning" in user_text:
        response = "Good Morning! Have a great day."

    elif "good night" in user_text:
        response = "Good Night! Sweet dreams."

    elif "bye" in user_text:
        response = "Goodbye! Have a nice day."

    elif "india" in user_text:
        response = "India is a country in South Asia."

    elif "largest planet" in user_text:
        response = "Jupiter is the largest planet in our solar system."

    elif "sun" in user_text:
        response = "The Sun is the star at the center of our solar system."

    elif "moon" in user_text:
        response = "The Moon is Earth's natural satellite."

    elif "water formula" in user_text:
        response = "The chemical formula of water is H₂O."

    elif "nda" in user_text:
        response = "NDA stands for National Defence Academy."

    else:
        response = "Sorry, I don't know the answer to that question."

    # Show Bot Message
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )                   
