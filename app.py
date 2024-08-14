from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir=Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file=current_dir / "styles" / "main.css"
resume_file =current_dir / "assests" / "Yeswanth Soma Resume.pdf"
profile_pic=current_dir / "assests" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Yeswanth Soma Portfolio"
PAGE_ICON = ":wave:"
NAME = "Yeswanth Soma"
DESCRIPTION = """
Strong foundation in both front-end and back-end development,
complemented by hands-on experience in python development and real-time data processing. 
"""
EMAIL = "yeswanthsoma83@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "www.linkedin.com/in/yeswanth-soma-266178211",
    "GitHub": "https://github.com/Yesh2344",
}
PROJECTS = {
    "🏆 ReadySetGo: Developed a gym website using Python, Django, HTML, and CSS with Amazon S3 for storage.",
    "🏆 AI-Driven Agile Software Development: Enhanced project management using AI.",
    "🏆 Real-time Data Processing Application with AWS EC2: Built a data processing app using AWS Kinesis Stream and Lambda.",
    "🏆 Predictive Analytics with Amazon Machine Learning: Created predictive models for business metrics.",
}

st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)

# --- LOAD CSS,PDF AND PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte=pdf_file.read()
    profile_pic=Image.open(profile_pic)

# --- HERO SECTION ---
col1,col2 = st.columns(2,gap="small")
with col1:
    st.image(profile_pic,width=300)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octect-stream",
    )        
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write("#")
cols=st.columns(len(SOCIAL_MEDIA))
for index, (platform,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# ---EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ CISCO (Internship): Focused on packet tracing and web development.
- ✔️ Channel Pro(Intern): Developed and managed website backend/frontend with Django and WordPress.
- ✔️ Prutor@IITK (Intern): Developed backend for an online bookstore using Python.
- ✔️ Google (Internship): Worked on scalable cloud applications using GCP.
"""
)

# ---SKILLS---
st.write("#")
st.subheader("Skills")
st.write(
    """
- 👩‍💻CLOUD TECHNOLOGIES: Google Cloud Platform (GCP) • AWS Basics • Cloud Deployment
- 🗄️FRAMEWORKS & LIBRARIES: Django Basics • Flask • Basic TensorFlow
- 🔄DEVOPS TOOLS: Basic Docker • Git for Version Control
- 🤖MACHINE LEARNING: Basic Scikit-learn • Pandas • Data Preprocessing
- 📚VERSION CONTROL: Git Basics • GitHub Collaboration
- 📊DATA VISUALIZATION: Basic Matplotlib • Seaborn for Visuals
- 🤝 🗣️TEAMWORK & COMMUNICATION: Collaborative Projects • Effective Communication • Problem Solving
"""
)


# --- WORK EXPERIENCE ---
st.write("#")
st.subheader("Work Experience")
st.write("---")

# --- JOB1
st.write("🌐","**CISCO Packet Software Developer**")
st.write("June 2020 - August 2020")
st.write(
    """
-  ➡️Packet Tracing: Conducted in-depth packet tracing exercises to analyze and optimize network performance 
for real-world applications.
-  ➡️Web Development: Contributed to the development of web-based tools, focusing on both backend and frontend
integration using modern technologies.
-  ➡️Real-world Implementation: Applied theoretical knowledge in practical scenarios, improving the network 
security and efficiency of web applications.
"""
)

# --- JOB2
st.write("🅖","**Google Cloud Platform Analyzer**")
st.write("May 2022 - August 2022")
st.write(
    """
-  ➡️Cloud Deployment: Deployed and managed scalable applications on Google Cloud Platform (GCP), ensuring efficient use of cloud resources.
-  ➡️Automation: Developed automated scripts to streamline cloud operations, enhancing deployment speed and reliability.
-  ➡️Collaboration: Worked with cross-functional teams to implement cloud-based solutions, improving overall project outcomes.
"""
)

# --- JOB3
st.write("🚧","**Channel Pro Front/Backend Developer**")
st.write("July 2022 - November 2022")
st.write(
    """
-  ➡️Full Stack Development: Worked on both backend (Django) and frontend (WordPress) aspects of the company’s website, ensuring a seamless user experience.
-  ➡️Python Integration: Developed Python scripts to automate routine tasks, enhancing the functionality and efficiency of the website.
-  ➡️Maintenance & Updates: Regularly updated and maintained the website to keep it running smoothly, addressing any technical issues promptly.
"""
)

# --- JOB3
st.write("🏫","**Prutor IITK Python Developer**")
st.write("March 2022 - May 2022")
st.write(
    """
-  ➡️Backend Development: Developed and optimized backend systems for an online bookstore, focusing on Python frameworks for robust performance.
-  ➡️API Management: Ensured smooth operation and integration of APIs with the bookstore’s website, enabling seamless user interactions.
-  ➡️Performance Enhancement: Worked on improving the efficiency and reliability of the website by optimizing code and reducing loading times.
"""
)


# --- Projects & Accomplishments ---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
st.write("""
-    🏆 ReadySetGo: Developed a gym website using Python, Django, HTML, and CSS with Amazon S3 for storage.
-    🏆 AI-Driven Agile Software Development: Enhanced project management using AI.
-    🏆 Real-time Data Processing Application with AWS EC2: Built a data processing app using AWS Kinesis Stream and Lambda.
-    🏆 Predictive Analytics with Amazon Machine Learning: Created predictive models for business metrics
"""
    )