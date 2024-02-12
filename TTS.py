import streamlit as st
import pyttsx3

def get_available_voices():
    """
    Get a list of available voices.
    """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    return voices

def main():
    st.title("Text-to-Speech with Streamlit")

    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Get available voices
    voices = get_available_voices()

    # Display available voices
    st.sidebar.header("Available Voices")
    selected_voice = st.sidebar.selectbox("Select a voice", voices)

    # Set the selected voice
    engine.setProperty('voice', selected_voice.id)

    # Input text
    text_to_speak = st.text_area("Enter your text", "Hello, this is a test message.")

    # Convert text to speech
    if st.button("Speak"):
        engine.say(text_to_speak)
        engine.runAndWait()

if __name__ == "__main__":
    main()
