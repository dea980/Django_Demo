import streamlit as st
import requests

# Set page config
st.set_page_config(
    page_title="Simple Chat & Schedule App",
    page_icon="📱",
    layout="wide"
)

# Add title and description
st.title("Simple Chat & Schedule App")
st.markdown("---")

# Sidebar for navigation
page = st.sidebar.selectbox(
    "Choose a page",
    ["Home", "Chat", "Schedule"]
)

if page == "Home":
    st.header("Welcome to Simple App")
    st.write("This is a simple application that helps you manage chats and schedules.")
    
    # Add some statistics or overview
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label="Active Chats", value="5")
    
    with col2:
        st.metric(label="Upcoming Events", value="3")

elif page == "Chat":
    st.header("Chat Room")
    
    # Chat room selection
    room_name = st.text_input("Enter Room Name")
    if st.button("Join Chat"):
        if room_name:
            st.success(f"Joined chat room: {room_name}")
            
            # Chat message input
            message = st.text_input("Type your message")
            if st.button("Send"):
                if message:
                    st.write(f"You: {message}")

elif page == "Schedule":
    st.header("Schedule Manager")
    
    # Add new schedule form
    with st.form("new_schedule"):
        title = st.text_input("Event Title")
        date = st.date_input("Event Date")
        description = st.text_area("Description")
        
        submitted = st.form_submit_button("Add Schedule")
        if submitted:
            st.success(f"Added new schedule: {title}")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")