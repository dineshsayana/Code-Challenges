import streamlit as st
from streamlit_google_auth import Authenticate
from google.cloud import firestore

def user_login_and_data():
    # Initialize authentication
    authenticator = Authenticate(
        secret_credentials_path='google_credentials.json',
        cookie_name='my_cookie_name',
        cookie_key='this_is_secret',
        redirect_uri='http://localhost:8501',
    )

    # Check authentication
    authenticator.check_authentification()

    if not st.session_state.get('connected', False):
        # Display login button if user is not authenticated
        authorization_url = authenticator.get_authorization_url()
        st.link_button('Login', authorization_url)
    else:
        # User is authenticated
        user_email = st.session_state['user_info'].get('email')
        
        # Initialize Firestore client
        db = firestore.Client()
        user_ref = db.collection('users').document(user_email)

        # Retrieve user data from Firestore
        user_data = user_ref.get().to_dict()
        if not user_data:
            user_data = {}

        # Display and allow editing of user data
        st.write(f"Welcome, {st.session_state['user_info'].get('name')}!")
        for key in user_data.keys():
            user_data[key] = st.text_input(key, user_data[key])

        # Allow adding new key-value pairs
        new_key = st.text_input("Add new field")
        new_value = st.text_input("Value for new field")
        if new_key and new_value:
            user_data[new_key] = new_value

        # Save button to update Firestore
        if st.button('Save Changes'):
            user_ref.set(user_data)
            st.success("Data saved successfully!")

        # Logout button
        if st.button('Log out'):
            authenticator.logout()
            st.experimental_rerun()

# Call the function in your Streamlit app
user_login_and_data()
