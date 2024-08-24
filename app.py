from pathlib import Path
import os
import base64
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# --- PATH SETTINGS ---
current_dir=Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file=current_dir / "styles" / "main.css"
resume_file =current_dir / "assests" / "Yeswanth Soma Resume.pdf"
profile_pic=current_dir / "assests" / "profile-pic.png"
python_gui=current_dir / "assests" / "gui.exe"

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
selected=option_menu(
    menu_title=None,
    options=["Home","Projects","Contact"],
    icons=["house","book","envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container":{"padding":"0!important","background-color":"#002b36"},
        "icon":{"color":"white"},
        "nav-link":{
            "text-align":"center",
            "margin":"0px",
            "--hover-color":"#9b4770"
        }
        

    }
)
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')
    
# --- LOAD CSS,PDF AND PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte=pdf_file.read()
    profile_pic=Image.open(profile_pic)
with open(python_gui, "rb") as exe_file:
    EXEbyte = exe_file.read()
# --- HERO SECTION ---
if selected=="Home":
    
    col1,col2 = st.columns(2,gap="small")
    with col1:
        st.image(profile_pic,width=300)
        st.markdown(
            """
            <style>
            img {
                filter: drop-shadow(1px 1px 20px #d33682);
                border-radius: 10px; /* Optional: for slightly rounded corners */
            }
            </style>
            """,
            unsafe_allow_html=True
        )

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
    st.write("---") 
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
    st.write("---")
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


    st.write("#")
    st.write("Like how i made my portfolio?😛😛")
    st.write("Please send me feedback by downloading my python GUI.😊")
    st.download_button(label="Download Application",
                    data=EXEbyte,
                    file_name=python_gui.name,
                    mime="application/octect-stream")

    

    # --- CUSTOM CSS FOR FOOTER ---
    st.markdown("""
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #002b36;
            color: black;
            text-align: center;
            padding: 10px 0;
            box-shadow: 0 -1px 10px rgba(0, 0, 0, 0.1);
        }
        .footer-quote {
            font-style: italic;
            margin-bottom: 5px;
        }
        .footer-copyright {
            font-size: 12px;
            color: #555;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- FOOTER CONTENT ---
    st.markdown("""
        <div class="footer">
            <div class="footer-quote">"Yesterday is history, tomorrow is a mystery, but today is a gift. That is why it is called the present." — Kung Fu Panda</div>
            <div class="footer-copyright">© 2024 Yeswanth Soma. All rights reserved.</div>
        </div>
    """, unsafe_allow_html=True)


if selected == "Projects":
    # Define the card content with local image paths
    cards = [
        {"title": "ReadySetGo", "date": "June 29", 
         "description": "A Web based application using HTML5, CSS3 and Javascript. This is a gym website with front-end developement.", "link": "https://github.com/Yesh2344/Readysetgo", "image": "assests/project1.png"},
        {"title": "ToDoList", "date": "July 15", "description": "ToDoList is a website which is used to remember all the todo to do in your daily life.", "link": "https://github.com/Yesh2344/ToDoList", "image": "assests/project2.png"},
        {"title": "PythonGUI", "date": "August 1", "description": "PythonGUI using Tkinter is a software created by python and css which is designed by Figma UI.", "link": "https://github.com/Yesh2344/Python_GUI", "image": "assests/project3.png"},
        {"title": "Project 4", "date": "August 1", "description": "Description for Project 4", "link": "#", "image": "images/project4.jpg"}
    ]

    # Custom CSS for card design
    st.markdown("""
    <style>
    .card {
        position: relative;
        border-radius: 15px;
        overflow: hidden;
        margin-top: 30px;
        box-shadow: 0 0 15px rgba(0, 255, 0, 0.5);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        height: 300px;
    }
    .card:hover {
        transform: translateY(-10px);
        box-shadow: 0 0 30px rgba(0, 255, 0, 0.8);
    }
    .card-image {
        width: 100%;
        height: 100%;
        background-size: cover;
        background-position: center;
        transition: transform 0.3s ease;
    }
    .card:hover .card-image {
        transform: scale(1.1);
    }
    .card-content {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0, 43, 54, 0.9);
        color: white;
        padding: 20px;
        opacity: 0;
        transition: opacity 0.3s ease;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .card:hover .card-content {
        opacity: 1;
    }
    .card-title {
        font-size: 24px;
        margin-bottom: 15px;
    }
    .card-date {
        font-size: 16px;
        color: #ff4141;
        margin-bottom: 10px;
    }
    .card-description {
        font-size: 14px;
        margin-bottom: 15px;
    }
    .card-link {
        text-decoration: none;
        color: #00ccff;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    # Display the cards in Streamlit
    cols = st.columns(2)
    for i, card in enumerate(cards):
        with cols[i % 2]:
            image_path = card['image']
            if os.path.exists(image_path):
                image_base64 = get_image_base64(image_path)
                st.markdown(f"""
                    <div class="card">
                        <div class="card-image" style="background-image: url('data:image/jpeg;base64,{image_base64}');"></div>
                        <div class="card-content">
                            <div class="card-date">{card['date']}</div>
                            <div class="card-title">{card['title']}</div>
                            <div class="card-description">{card['description']}</div>
                            <a class="card-link" href="{card['link']}">See More</a>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.warning(f"Image not found: {image_path}")

if selected=="Contact":
    # --- Contact Me --
    st.subheader(":mailbox: Contact Me")
    st.write("---")
    contact_form="""
    <form action="https://formsubmit.co/yeswanthsoma77@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message" requried></textarea>
        <button type="submit">Send</button>
    </form>"""
    st.markdown(contact_form,unsafe_allow_html=True)