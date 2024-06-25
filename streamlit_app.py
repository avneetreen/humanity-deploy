import streamlit as st
import requests

st.header("Humanity-deploy", divider='rainbow')
st.subheader("War & Peace")
st.write("This is a simple Streamlit app.")


# Function to fetch page data from FastAPI
def fetch_page(page: str) -> dict:
    url = f"http://localhost:8000/{page}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"page": "not_found"}


# Streamlit sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# Fetch page data
page_data = fetch_page(page.lower())

# Render the appropriate page using Streamlit elements
if page_data["page"] == "home":
    st.title("Home Page")
    st.write(
        "Welcome to the Home Page! This is a dynamic page created using Streamlit.")
    st.line_chart([1, 2, 3, 4, 5])

elif page_data["page"] == "about":
    st.title("About Page")
    st.write(
        "This is the About Page. Here you can find information about this application.")
    st.bar_chart([1, 2, 3, 4, 5])

elif page_data["page"] == "contact":
    st.title("Contact Page")
    st.write("This is the Contact Page. Get in touch with us here.")
    st.map()

else:
    st.title("404")
    st.write("Page not found.")
