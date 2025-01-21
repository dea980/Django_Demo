import os
import sys
from datetime import datetime

# Add Django project root and SimpleApp directory to Python path first
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
sys.path.append(os.path.join(project_root, 'SimpleApp'))

# Set up Django settings before any Django imports
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SimpleApp.SimpleApp.settings')

# Set up Django
import django
django.setup()

# Now we can safely import Django-related modules
import streamlit as st
from django.utils import timezone
from Message_Chat_app.models import ChatMessage
from scheduler.models import Schedule
from django.contrib.auth.models import User

# Set page config
st.set_page_config(
    page_title="Simple Chat & Schedule App",
    page_icon="📱",
    layout="wide"
)

# Initialize session state
if 'user' not in st.session_state:
    # For demo purposes, use the first user in the database
    st.session_state.user = User.objects.first()

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
    
    # Add real statistics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        active_chats = ChatMessage.objects.values('room').distinct().count()
        st.metric(label="Active Chat Rooms", value=active_chats)
    
    with col2:
        upcoming_events = Schedule.objects.filter(
            date__gte=timezone.now().date(),
            status='pending'
        ).count()
        st.metric(label="Upcoming Events", value=upcoming_events)
    
    with col3:
        total_messages = ChatMessage.objects.count()
        st.metric(label="Total Messages", value=total_messages)

elif page == "Chat":
    st.header("Chat Room")
    
    # Chat room selection
    rooms = (ChatMessage.objects.values_list('room', flat=True)
             .distinct() or ['general'])
    room_name = st.selectbox("Select or Enter Room Name", 
                            list(rooms),
                            index=0)
    
    # Display chat messages
    messages = ChatMessage.objects.filter(room=room_name).select_related('user')
    for msg in messages:
        with st.chat_message(msg.user.username):
            st.write(f"{msg.timestamp.strftime('%H:%M:%S')} - {msg.content}")
    
    # Chat message input
    message = st.chat_input("Type your message")
    if message:
        # Save and display new message
        new_msg = ChatMessage.objects.create(
            content=message,
            user=st.session_state.user,
            room=room_name
        )
        with st.chat_message(st.session_state.user.username):
            st.write(f"{new_msg.timestamp.strftime('%H:%M:%S')} - {message}")

elif page == "Schedule":
    st.header("Schedule Manager")
    
    # Display existing schedules
    st.subheader("Upcoming Schedules")
    schedules = Schedule.objects.filter(
        date__gte=timezone.now().date()
    ).order_by('date', 'time')
    
    for schedule in schedules:
        with st.expander(f"{schedule.title} - {schedule.date} {schedule.time}"):
            st.write(f"Description: {schedule.description}")
            st.write(f"Status: {schedule.status}")
            if st.button(f"Mark Complete {schedule.id}", key=f"complete_{schedule.id}"):
                schedule.status = 'completed'
                schedule.save()
                st.rerun()
    
    # Add new schedule form
    st.subheader("Add New Schedule")
    with st.form("new_schedule"):
        title = st.text_input("Event Title")
        date = st.date_input("Event Date")
        time = st.time_input("Event Time")
        description = st.text_area("Description")
        status = st.selectbox("Status", ['pending', 'completed', 'cancelled'])
        
        submitted = st.form_submit_button("Add Schedule")
        if submitted and title and date and time:
            Schedule.objects.create(
                title=title,
                description=description,
                date=date,
                time=time,
                status=status
            )
            st.success(f"Added new schedule: {title}")
            st.rerun()

# Footer
st.markdown("---")
st.markdown("Streamlit UI connected to Django backend")