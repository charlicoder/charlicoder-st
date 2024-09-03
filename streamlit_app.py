from streamlit_gsheets import GSheetsConnection
import streamlit as st

from pathlib import Path
from PIL import Image

# --- Path Settings ---

current_dir = Path("__name__").parent
resume_file = current_dir / "assets" / "Resume_Of_K_Md_Mamunur_Rashid.pdf"

# --- General Settings ---
EMAIL = "charlicoder@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/charlicoder/",
    "Github": "https://github.com/charlicoder/"
}

# cols = st.columns(len(SOCIAL_MEDIA))
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].write(f"[{platform}]({link})")


# --- Page setup ----

about_page = st.Page(
    title="About Me",
    page="views/about_me.py",
    icon=":material/account_circle:",
    default=True
)

work_history = st.Page(
    title="Work History",
    page="views/experiences.py",
    icon=":material/account_circle:"
)

project_1_page =  st.Page(
    title="Dashboard",
    page="views/dashboard.py",
    icon=":material/smart_toy:"
)

# ---- Navigation Setup [without sections] ------
# pg = st.navigation(pages=[about_page, project_1_page])

# ---- Navigation Setup [with sections] ----

pg = st.navigation(
    {
        "Info": [about_page, work_history],
        "Projects": [project_1_page]
    }
)


# --- Load resume ---
with open(resume_file, 'rb') as resume:
    resume_byte = resume.read()

# --- shared on all pages ---
st.logo("images/mamun_circle_pic.png")
st.sidebar.download_button(
    label="Download Resume",
    data=resume_byte,
    file_name=resume_file.name,
    mime="application/octet-stream"
)

pg.run()