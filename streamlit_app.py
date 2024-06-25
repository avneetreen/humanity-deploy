import streamlit as st
import requests
import pandas as pd
from ast import literal_eval
import re

st.header("War & Peace", divider='rainbow')
st.subheader(
    "Editorial Pattens in News Coverage through the lens of War & Peace Journalism")
# st.write("This is a simple Streamlit app.")


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
page = st.sidebar.radio("Go to", ["Home"])

# Fetch page data
page_data = fetch_page(page.lower())


def highlight_text(text, highlights):
    """Highlight the specified words/phrases in the content."""
    for highlight in highlights:
        print(highlight)
        escaped_highlight = re.escape(highlight)  # Escape special characters
        pattern = re.compile(f"({escaped_highlight})", re.IGNORECASE)
        text = pattern.sub(
            r'<mark style="background-color: lightpink;">\1</mark>', text)
    return text


# Render the appropriate page using Streamlit elements
if page_data["page"] == "home":
    st.title("Visible Effects of War")

    # df = pd.DataFrame(data)
    # Create a DataFrame
    df = pd.read_csv("data/some_results.csv")

    # Streamlit application
    st.subheader("Article Viewer")

    # Dropdown for selecting an article
    article_title = st.selectbox(
        "Select and article to highlight keywords and identify FrameNet Frames associated with visible effects of war",
        df["title"])

    # Get the selected article's details
    selected_article = df[df["title"] == article_title].iloc[0]
    print(literal_eval(selected_article["all_text_to_highlight"]),
          selected_article["maintext"])

    # Highlight the text
    highlighted_content = highlight_text(
        selected_article["maintext"],
        literal_eval(selected_article["all_text_to_highlight"]))

    # print(highlighted_content)

    # Display the highlighted article content
    st.markdown(highlighted_content, unsafe_allow_html=True)

    # Display the keywords in the sidebar
    st.sidebar.title("FrameNet Frames")
    for keyword in set(literal_eval(selected_article["all_frames"])):
        st.sidebar.write(keyword)

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
