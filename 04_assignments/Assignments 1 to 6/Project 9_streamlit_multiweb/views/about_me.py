import streamlit as st

from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

# Hero Section 
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/profile_img.jpg", width=230)
with col2:
    st.title("Foqia Siddiqui", anchor=False)
    st.write(
        "Student at Governer Initiative for Artificial Intelligence!"
    )
    if st.button("Contact Me"):
        show_contact_form()
col3, col4 = st.columns(2, gap="small", vertical_alignment="center")

with col3:
    st.write("\n")
    st.subheader("Skills", anchor=False)
    st.write(
    """
    - Nextjs
    - Typescript
    - HTML/CSS
    - Python/Streamlit
    - AI/Web 3.0/ Metaverse
    """
)

with col4:
    st.write("\n")
    st.subheader("About Me!", anchor=False)
    st.write(
    """
    I'm pursuing undergraduate degree in Bs-English from (NUML) Karachi.
    Currently enroll in IT course at Governer House. 
    Passionate Front-end Developer intend to work on real world projects at international level.
    Looking for oppourtunity to enhance my expertise in tech industry! 

    """
    
)



