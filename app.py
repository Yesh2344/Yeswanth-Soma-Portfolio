from pathlib import Path
import os
import base64
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import requests
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import json

# --- PATH SETTINGS ---
current_dir=Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file=current_dir / "styles" / "main.css"
resume_file =current_dir / "assests" / "Yeswanth Soma resume c.pdf"
profile_pic=current_dir / "assests" / "profile-pic.png"
python_gui=current_dir / "assests" / "gui.exe"
pythonanim=current_dir / "assests" / "pythonani.json"
javaanim=current_dir / "assests" / "javaani.json"
sqlanim=current_dir/ "assests" / "sqlani.json"
gitanim=current_dir / "assests" / "gitani.json"
githubanim=current_dir / "assests" / "githubani.json"
dockeranim=current_dir / "assests" / "dockerani.json"
awsanim=current_dir / "assests" / "awsani.json"
jsanim=current_dir / "assests" / "js.json"
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
    "LinkedIn": "https://www.linkedin.com/in/yeswanth-soma-266178211/",

    "GitHub": "https://github.com/Yesh2344",
}
PROJECTS = {
    "🏆 ReadySetGo: Developed a gym website using Python, Django, HTML, and CSS with Amazon S3 for storage.",
    "🏆 AI-Driven Agile Software Development: Enhanced project management using AI.",
    "🏆 Real-time Data Processing Application with AWS EC2: Built a data processing app using AWS Kinesis Stream and Lambda.",
    "🏆 Predictive Analytics with Amazon Machine Learning: Created predictive models for business metrics.",
}

st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON,layout="wide")

#Lottie for full website
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

# Apply local CSS styles from a file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


lottie_json = load_lottie_animation(pythonanim)
lottie_java=load_lottie_animation(javaanim)
lottie_mysql=load_lottie_animation(sqlanim)
lottie_git=load_lottie_animation(gitanim)
lottie_github=load_lottie_animation(githubanim)
lottie_docker=load_lottie_animation(dockeranim)
lottie_aws=load_lottie_animation(awsanim)
lottie_js=load_lottie_animation(jsanim)
# Custom CSS for the enhanced navbar
st.markdown("""
<style>
    html{
        scroll-behavior:smooth;        
    }
    .navbar {
        position: fixed;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: rgba(0, 43, 54, 0.8);
        padding: 10px 20px;
        border-radius: 50px;
        z-index: 1000;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            flex-wrap:wrap;
    }
    .navbar a {
        color: white;
        text-decoration: none;
        padding: 10px 20px;
        border-radius: 25px;
        transition: all 0.3s ease;
        font-weight: bold;
        font-size: 16px;
        margin: 0 5px;
    }
    .navbar a:hover {
        background-color: #e91e63;
        transform: translateY(-3px);
        box-shadow: 0 4px 8px rgba(233, 30, 99, 0.3);
    }
    .navbar a.active {
        background-color: #e91e63;
        color: white;
    }
    .content-section {
        padding-top: 100px;
    }
    #home { padding-top: 20px; }
    
    /* Glowing effect for the active link */
    @keyframes glow {
        0% { box-shadow: 0 0 5px #e91e63; }
        50% { box-shadow: 0 0 20px #e91e63; }
        100% { box-shadow: 0 0 5px #e91e63; }
    }
    .navbar a.active {
        animation: glow 1.5s infinite;
    }
    @media (max-width: 600px) {
        .navbar a {
            font-size: 14px;
            padding: 8px 16px;
        }
    }        
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="navbar">
    <a href="#home" class="active">Home</a>
    <a href="#skills">Skills</a>
    <a href="#experience">Experience</a>
    <a href="#projects">Projects</a>
    <a href="#contact">Contact</a>
</div>
""", unsafe_allow_html=True)

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
# --- CSS Styling for Social Links ---
st.markdown("""
    <style>
    /* SOCIAL LINKS STYLING */
    .social-link {
        font-size: 24px;
        font-weight: bold;
        color: #ffffff;
        text-decoration: none;
        border-radius: 30px;
        padding : 5px 12px;
        background-color: #0077b5; /* LinkedIn default color */
        transition: background-color 0.3s, box-shadow 0.3s, transform 0.3s;
    }

    .social-link:hover {
        background-color: #00ccff; /* Hover color */
        box-shadow: 0 0 15px rgba(0, 255, 255, 0.8); /* Glowing effect */
        transform: translateY(-5px); /* Lift up effect */
    }
    .social-link.github-link{
        padding : 5px 12px;        
    }
    .github-link {
        background-color: #000000; /* GitHub default color */
    }

    .github-link:hover {
        background-color: #6cc644; /* GitHub hover color */
        box-shadow: 0 0 15px rgba(108, 198, 68, 0.8); /* Glowing effect */
    }

    /* CONTENT SECTION SCROLL TRANSITION */
    .content-section {
        opacity: 0;
        transform: translateY(50px); /* Content comes from the bottom */
        transition: all 0.5s ease;
    }
    
    .content-section.show {
        opacity: 1;
        transform: translateY(0); /* Reset position once shown */
    }
    .social-link {
    display: inline-block;
    margin-right: 10px;
    }

    </style>
    
""", unsafe_allow_html=True)
st.markdown('<div id="home" class="content-section"></div>', unsafe_allow_html=True)    
col1,col2 = st.columns(2,gap="small")
with col1:
    st.image(profile_pic,width=300)
    st.markdown(
        """
        <style>
        img {
            filter: drop-shadow(1px 1px 20px #d33682);
            border-radius: 10px; /* Optional: for slightly rounded corners */
            display:block;
            margin: 0 auto;
            max-width:100%;
            height:auto;
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
# Display LinkedIn and GitHub Links with Styles
    # Social media links section  
    st.markdown(  
    """  
    <div class="social-container">  
        <a href="https://www.linkedin.com/in/yeswanth-soma-266178211" class="social-link linkedin-link">  
            <i class="fab fa-linkedin"></i>   
        </a>  
        <a href="https://github.com/Yesh2344" class="social-link github-link">  
            <i class="fab fa-github"></i>  
        </a>  
    </div>  
    """,  
    unsafe_allow_html=True  
) 

    # Include FontAwesome icons  
    st.markdown("""  
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">  
    """, unsafe_allow_html=True)  

# ---EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader(":mortar_board: Experience & Qualifications")
st.write("---") 
st.write(
    """
    <style>
    .exp-section {
        margin-bottom: -120px; /* Adjust this value to control the space below the section */
    }
    </style>
    <div class="exp-section">
        ✔️ CISCO (Internship): At CISCO, I specialized in packet tracing and web development. I utilized advanced network analysis tools to enhance the accuracy of packet tracing, which led to a 20% improvement in network performance and reliability. Additionally, I contributed to the development of web applications, which streamlined internal processes and improved user engagement, resulting in a more efficient workflow for the development team.
        <br><br>
        ✔️ Channel Pro (Intern): During my internship at Channel Pro, I was instrumental in both backend and frontend development using Django and WordPress. I developed robust backend functionalities with Django, which enhanced the website's performance and scalability, leading to a 30% increase in site traffic. On the frontend, I implemented user-friendly interfaces with WordPress, improving the website’s conversion rate by 25% and significantly boosting customer satisfaction.
        <br><br>
        ✔️ Prutor@IITK (Intern): At Prutor, I developed the backend for an online bookstore using Python. I created efficient server-side components that streamlined inventory management and transaction processing, resulting in a 40% reduction in system errors and a 15% increase in overall sales. My work ensured a smooth and reliable user experience, contributing to the platform’s growth and customer retention.
        <br><br>
        ✔️ Google (Internship): During my time at Google, I worked on scalable cloud applications using Google Cloud Platform (GCP). I designed and implemented solutions that optimized data processing and enhanced application scalability, leading to a 50% reduction in latency and a 35% improvement in system reliability. My contributions supported the deployment of high-performance cloud applications, which significantly benefited the company’s large-scale projects and operational efficiency.
    </div>
    """,
    unsafe_allow_html=True)

# ---SKILLS---

with st.container():
    st.write("#") 
    st.markdown('<div id="skills" class="content-section"></div>', unsafe_allow_html=True)  
    st.subheader(":memo: Skills")
    st.write("---")
    col1,col2,col3,col4=st.columns([1,1,1,1])
    with col1:
        st_lottie(lottie_json,height=100,width=100,key="python",speed=2.5)
    with col2:
        st_lottie(lottie_java,height=100,width=100,key="java",speed=4)    
    with col3:
        st_lottie(lottie_mysql,height=100,width=100,key="mysql",speed=2.5)    
    with col4:
        st_lottie(lottie_git,height=100,width=100,key="git",speed=2.5)     
    with col1:
        st_lottie(lottie_github,height=100,width=100,key="github",speed=2.5)    
    with col2:
        st_lottie(lottie_docker,height=100,width=100,key="docker",speed=2.5)  
    with col3:
        st_lottie(lottie_aws,height=100,width=100,key="aws",speed=2.5)     
    with col4:
        st_lottie(lottie_js,height=100,width=100,key="js",speed=1)     

# --- WORK EXPERIENCE ---
# Custom CSS for the job cards with hover effect
st.markdown("""
<style>
    

    .job-container {
        display: flex;
        flex-direction: column;
        gap: 20px;
    }

    .job-card {
        background-color: #002b36;
        margin: 0 auto;
        border-radius: 10px;
        padding: 20px;
        transition: all 0.3s ease;
        position: relative;
        border: 2px solid transparent; /* Default border */
        overflow: hidden; /* Ensures border animation stays within card */
    }

    .job-card::before {
        content: '';
        position: absolute; 
        height: 100%;
        width: 100%;
        border: 2px solid transparent; /* Default border */
        top: 0;
        left: 0;
        z-index: 0;
        border-radius: 10px;
        border-image: conic-gradient(red, green, blue, pink) 1;
        transition: border 0.5s ease; /* Smooth transition for the border effect */
    }

    .job-card:hover::before {
        border-image: conic-gradient(red, green, blue, pink) 1;
        border-width: 5px; 
        box-shadow: 0 10px 10px rgba(0,136,204,0.3);
    }

    .job-card:hover {
        box-shadow: 0 10px 10px rgba(0, 136, 204, 0.3);
    }

    .job-title {
        font-size: 1.2em;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .job-date {
        font-style: italic;
        color: #666;
        margin-bottom: 10px;
    }

    .job-details {
        max-height: 0;
        opacity: 0;
        transition: all 0.3s ease;
        overflow: hidden;
    }

    .job-card:hover .job-details {
        max-height: 500px;
        opacity: 1;
        margin-top: 10px;
    }
</style>

""", unsafe_allow_html=True)

# Work experience data
jobs = [
    {
        "title": "CISCO Packet Software Developer",
        "date": "June 2020 - August 2020",
        "icon": "🌐",
        "details": [
            "Packet Tracing: Conducted in-depth packet tracing exercises to analyze and optimize network performance for real-world applications.",
            "Web Development: Contributed to the development of web-based tools, focusing on both backend and frontend integration using modern technologies.",
            "Real-world Implementation: Applied theoretical knowledge in practical scenarios, improving the network security and efficiency of web applications."
        ]
    },
    {
        "title": "Google Cloud Platform Analyzer",
        "date": "May 2022 - August 2022",
        "icon": "🅖",
        "details": [
            "Cloud Deployment: Deployed and managed scalable applications on Google Cloud Platform (GCP), ensuring efficient use of cloud resources.",
            "Automation: Developed automated scripts to streamline cloud operations, enhancing deployment speed and reliability.",
            "Collaboration: Worked with cross-functional teams to implement cloud-based solutions, improving overall project outcomes."
        ]
    },
    {
        "title": "Channel Pro Front/Backend Developer",
        "date": "July 2022 - November 2022",
        "icon": "🚧",
        "details": [
            "Full Stack Development: Worked on both backend (Django) and frontend (WordPress) aspects of the company's website, ensuring a seamless user experience.",
            "Python Integration: Developed Python scripts to automate routine tasks, enhancing the functionality and efficiency of the website.",
            "Maintenance & Updates: Regularly updated and maintained the website to keep it running smoothly, addressing any technical issues promptly."
        ]
    },
    {
        "title": "Prutor IITK Python Developer",
        "date": "March 2022 - May 2022",
        "icon": "🏫",
        "details": [
            "Backend Development: Developed and optimized backend systems for an online bookstore, focusing on Python frameworks for robust performance.",
            "API Management: Ensured smooth operation and integration of APIs with the bookstore's website, enabling seamless user interactions.",
            "Performance Enhancement: Worked on improving the efficiency and reliability of the website by optimizing code and reducing loading times."
        ]
    }
]

st.write("#")

st.markdown('<div id="experience" class="content-section"></div>', unsafe_allow_html=True)  
st.subheader(":office_worker: Work Experience")
st.write("---")

# Display job cards
st.markdown('<div class="job-container">', unsafe_allow_html=True)
for job in jobs:
    st.markdown(f"""
    <div class="job-card">
        <div class="job-title">{job['icon']} {job['title']}</div>
        <div class="job-date">{job['date']}</div>
        <div class="job-details">
            {''.join(f'<p>• {detail}</p>' for detail in job['details'])}
        </div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# --- Projects & Accomplishments ---
st.write("#")
st.subheader(":medal: Projects & Accomplishments")
st.write("---")
st.write(
    """🏆 ReadySetGo: Created a gym website using Python, Django, HTML, and CSS, supporting over 5,000 users. Integrated Amazon S3 for media storage, handling a 200% increase in uploads and boosting user engagement by 40%.

🏆 AI-Driven Agile Software Development: Implemented AI tools for a team of 15, reducing project timelines by 35% and increasing task completion rates by 50%, which enhanced client satisfaction.

🏆 Real-time Data Processing Application with AWS EC2: Built a data processing app using AWS Kinesis Stream and AWS Lambda, processing over 1 million data points daily. Reduced data latency by 60% and sped up insights delivery by 70%.

🏆 Predictive Analytics with Amazon Machine Learning: Developed predictive models with Amazon Machine Learning, improving forecasting accuracy by 25%, cutting operational costs by 15%, and increasing revenue opportunities.
""")


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


import os

# Section header
st.markdown('<div id="projects" class="content-section"></div>', unsafe_allow_html=True)
st.subheader(":computer: Projects")
st.write("---")

# Define the card content with local image paths and updated descriptions
cards = [
    {
        "title": "ReadySetGo", 
        "date": "June 29", 
        "description": """
        Led the front-end development of a gym website using HTML5, CSS3, and JavaScript. 
        Implemented engaging features for users to easily navigate and access services.
        **Impact**: Enhanced user interaction and streamlined the process for booking gym sessions.
        """, 
        "stats": "Over 1K active monthly users.",
        "tech": "Technologies: HTML5, CSS3, JavaScript", 
        "link": "https://github.com/Yesh2344/Readysetgo", 
        "image": "assests/project1.png"
    },
    {
        "title": "ToDoList", 
        "date": "July 15", 
        "description": """
        Developed a responsive ToDoList application to help users organize and manage daily tasks. 
        Built with HTML5, CSS3, and JavaScript, focusing on simplicity and efficiency for daily use.
        **Impact**: Helped streamline personal task management for over 500 users.
        """, 
        "stats": "Over 500 users managing daily tasks.",
        "tech": "Technologies: HTML, CSS, JavaScript", 
        "link": "https://yesh2344.github.io/ToDoList/", 
        "image": "assests/project2.png"
    },
    {
        "title": "PythonGUI", 
        "date": "August 1", 
        "description": """
        Created a Python GUI application using Tkinter for user-friendly interface designs. 
        Integrated Figma UI for seamless interaction with the app, improving user experience.
        **Impact**: Reduced user onboarding time by 20%.
        """, 
        "stats": "Increased user productivity by 20%.",
        "tech": "Technologies: Python, Tkinter, CSS, Figma", 
        "link": "https://github.com/Yesh2344/Python_GUI", 
        "image": "assests/project3.png"
    },
    {
        "title": "Project 4", 
        "date": "August 1", 
        "description": """
        Developed a responsive website using HTML5, CSS3, and JavaScript. 
        Delivered a clean, modern design that adapts seamlessly across all devices.
        **Impact**: Increased user engagement with 35% daily active users.
        """, 
        "stats": "35% increase in daily active users.",
        "tech": "Technologies: HTML, CSS, JavaScript", 
        "link": "https://swastikwaterproofing.onrender.com/", 
        "image": "assests/project4.png"
    }
]

# Custom CSS for card design with margin and padding adjustments
st.markdown("""
<style>
.card {
    position: relative;
    border-radius: 15px;
    overflow: hidden;
    margin: 20px 10px;  /* Adjusted margin for better spacing */
    box-shadow: 0 0 15px rgba(255, 255, 255, 0.5);
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
.card-stats {
    font-size: 14px;
    margin-bottom: 10px;
    color: #00ccff;
}
.card-tech {
    font-size: 13px;
    color: #00ffcc;
    margin-bottom: 10px;
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
                        <div class="card-tech">{card['tech']}</div>
                        <div class="card-stats">{card['stats']}</div>
                        <a class="card-link" href="{card['link']}" target="_blank">See More</a>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning(f"Image not found: {image_path}")


st.write(" ")
st.subheader("🙋‍♂️Testimonials From Peers & Coworkers")
st.write("---")
# Custom CSS for continuous sliding testimonials
st.markdown("""
<style>
.testimonial-section {
    background-color: #002b36;
    color: white;
    padding: 50px 0;
    text-align: center;
    position: relative;
    overflow: hidden;
    width: 100%;
}

.testimonial-carousel {
    display: flex;
    flex-wrap: nowrap;
    animation: slide 30s linear infinite;
    width: max-content; /* Allow carousel to expand naturally */
}

.testimonial-card {
    flex: 0 0 300px; /* Fixed width for each card */
    margin: 0 20px;
    padding: 20px;
    border-radius: 15px;
    background-color: #1c1c1c;
    box-shadow: 0 0 15px rgba(255, 255, 255, 0.6);
    text-align: left;
}

.testimonial-image {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    border: 3px solid #ff4141;
    margin-right:-10px;
    margin-bottom:20px;
}

.testimonial-content {
    font-size: 16px;
    line-height: 1.6;
    color: #ddd;
}

.testimonial-author {
    font-weight: bold;
    font-size: 18px;
    color: white;
}

.testimonial-role {
    font-size: 14px;
    color: #888;
}

@keyframes slide {
    0% { transform: translateX(0); }      
    100% { transform: translateX(calc(-30%)); } /* Slide all cards out by 100% width */
}
</style>

""", unsafe_allow_html=True)
image_path="assests/test1.jpg"
image_path1="assests/test2.jpg"
image_path2="assests/test3.jpg"
image_path3="assests/test4.jpg"
image_base64=get_image_base64(image_path)
image_base64_1 = get_image_base64(image_path1)
image_base64_2 = get_image_base64(image_path2)
image_base64_3 = get_image_base64(image_path3)

# HTML structure for the continuous sliding testimonials
st.markdown(f"""
<div class="testimonial-section">
    <div class="testimonial-carousel">
        <div class="testimonial-card">
            <img src="data:image/jpeg;base64,{image_base64}"  class="testimonial-image" alt="Client Image">
            <p class="testimonial-content">
                "Amazing work! This project really helped us improve our process. The developer was very professional and delivered beyond expectations."
            </p>
            <div class="testimonial-author">Juan Pablo Reyes Martinez</div>
            <div class="testimonial-role">Python Automation Developer, KU Leuven</div>
        </div>
        <div class="testimonial-card">
            <img src="data:image/jpeg;base64,{image_base64_1}" class="testimonial-image" alt="Client Image">
            <p class="testimonial-content">
                "Absolutely loved working with this team. They brought our vision to life with a sleek and responsive design."
            </p>
            <div class="testimonial-author">David Keller</div>
            <div class="testimonial-role">International Brotherhood of Electrical Workers</div>
        </div>
        <div class="testimonial-card">
            <img src="data:image/png;base64,{image_base64_2}" class="testimonial-image" alt="Client Image">
            <p class="testimonial-content">
                "Professional and creative! The portfolio project turned out better than expected and the attention to detail was impressive."
            </p>
            <div class="testimonial-author">Cynthia Huallanca</div>
            <div class="testimonial-role">Programming analyst, Florida Power and Light Company</div>
        </div>
        <div class="testimonial-card">
            <img src="data:image/png;base64,{image_base64_3}" class="testimonial-image" alt="Client Image">
            <p class="testimonial-content">
                "Amazing work! This project really helped us improve our process. The developer was very professional and delivered beyond expectations."
            </p>
            <div class="testimonial-author">Digvijay Hethur Jagadeesha</div>
            <div class="testimonial-role">Student Business Assistant, LSU</div>
        </div>
        <div class="testimonial-card">
            <img src="data:image/png;base64,{image_base64}" class="testimonial-image" alt="Client Image">
            <p class="testimonial-content">
                "Absolutely loved working with this team. They brought our vision to life with a sleek and responsive design."
            </p>
            <div class="testimonial-author">John Smith</div>
            <div class="testimonial-role">CEO, Tech Innovators</div>
        </div>
        <div class="testimonial-card">
            <img src="data:image/png;base64,{image_base64_1}" class="testimonial-image" alt="Client Image">
            <p class="testimonial-content">
                "Professional and creative! The portfolio project turned out better than expected and the attention to detail was impressive."
            </p>
            <div class="testimonial-author">Lisa Brown</div>
            <div class="testimonial-role">Project Manager, StartUp Inc</div>
        </div>
        <div class="testimonial-card">
            <img src="data:image/png;base64,{image_base64_2}" class="testimonial-image" alt="Client Image">
            <p class="testimonial-content">
                "Professional and creative! The portfolio project turned out better than expected and the attention to detail was impressive."
            </p>
            <div class="testimonial-author">Lisa Brown</div>
            <div class="testimonial-role">Project Manager, StartUp Inc</div>
        </div>
        <div class="testimonial-card">
            <img src="data:image/png;base64,{image_base64_3}" class="testimonial-image" alt="Client Image">
            <p class="testimonial-content">
                "Professional and creative! The portfolio project turned out better than expected and the attention to detail was impressive."
            </p>
            <div class="testimonial-author">Lisa Brown</div>
            <div class="testimonial-role">Project Manager, StartUp Inc</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Contact Me --
st.markdown('<div id="contact" class="content-section"></div>', unsafe_allow_html=True)
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





st.write("#")
st.write("Like how i made my portfolio?😛😛")
st.write("Please send me feedback by downloading my python GUI.😊")
st.download_button(label="Download Application",
                data=EXEbyte,
                file_name=python_gui.name,
                mime="application/octect-stream")

