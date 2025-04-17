import streamlit as st   

about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    default=True,
)


project_2_page = st.Page(
    page= "views/chatbot.py",
    title="Chat Bot",
    # icon="material/smart_toy:",
)

# Navigation setup 1
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])
# pg.run()

# Navigation setup 2
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_2_page],
    }
)

# Run navigation
pg.run()