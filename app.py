import streamlit as st
from google import genai

# --- ૧૦૦% લોકલ રન માટે ડાયરેક્ટ કી સેટઅપ ---
# ગિટહબ પર અપલોડ કરતા પહેલા સુરક્ષા માટે આ લાઇન આપણે બદલીશું, પણ અત્યારે રન કરવા માટે આ બેસ્ટ છે!
GOOGLE_API_KEY = "AQ.Ab8RN6II-RCXyyUbihvRaTzD5_JLIrJlCnNJjoho_RmpZAyHzQ"
# Initialize the new GenAI client
client = genai.Client(api_key=GOOGLE_API_KEY)

# 2. Web page configurations
st.set_page_config(page_title="Gujarati Mitra - AI", page_icon="🤖", layout="centered")

# --- Sidebar Interface ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=100)
    st.title("🤖 Bot Profile")
    st.subheader("Name: Gujarati Mitra")
    st.write("---")
    st.write("**Features:**")
    st.write("• Extremely polite and friendly")
    st.write("• Multilingual (English, Gujarati, Hindi)")
    st.write("• Available 24/7 for you")
    st.write("---")
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# --- Main Screen Interface ---
st.title("✨ Gujarati Mitra AI")
st.write("Chat with your digital friend. You can ask any question!")

# 3. Initialize chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Display past chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Accept user input
if user_input := st.chat_input("Type your question here... / અહીં તમારો પ્રશ્ન લખો..."):
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # --- System Instructions for AI Persona & Style ---
    system_instruction = (
        "You are 'ગુજરાતી મિત્ર' (Gujarati Mitra), a super friendly, helpful, polite, and intelligent AI assistant. "
        "Your talking style should be respectful, warm, and engaging. Use emojis appropriately to sound friendly. "
        "Strictly detect the language of the user: "
        "- If the user asks in Gujarati, reply in beautiful, natural Gujarati. "
        "- If in Hindi, reply in polite Hindi. "
        "- If in English, reply in professional English. "
        "Always try to give complete and accurate answers."
    )
    
    prompt_with_instruction = f"{system_instruction}\n\nQuestion: {user_input}"
    
    try:
        # Generate response using the stable gemini-2.5-flash model
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt_with_instruction,
        )
        bot_response = response.text
    except Exception as e:
        bot_response = f"Error: {str(e)}. Please check your connection."

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(bot_response)
        
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": bot_response})