import streamlit as st
from groq import Groq

# Initialize Groq client
client = Groq(api_key="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")

# Function to interact with Groq API
def chat_with_groq(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-70b-8192",
    )
    return chat_completion.choices[0].message.content

# Streamlit app
def main():
    st.title("Chatbot")

    # Initialize chat history
    chat_history = []

    # Streamlit input for user prompt
    user_input = st.text_input("You:", "")

    if st.button("Send"):
        # Send user prompt to Groq and get response
        response = chat_with_groq(user_input)

        # Append user input and response to chat history
        chat_history.append({"user": user_input, "bot": response})

    # Display chat history
    st.write("Chat History:")
    for chat in chat_history:
        st.write(f"You: {chat['user']}")
        st.write(f"Bot: {chat['bot']}")
        st.write("")

# Run Streamlit app
if __name__ == "__main__":
    main()
