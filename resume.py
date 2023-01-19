import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Resume", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()




# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_3rwasyjy.json")
lottie_code = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_qp1q7mct.json")
img_contact_form = Image.open("images/2023-01-17 (1).png")
img_lottie_animation = Image.open("images/2023-01-17.png")
img_1=Image.open("images/2023-01-19.png")
img_2=Image.open("images\Screenshot 2023-01-19 142107.png")
img_3=Image.open("images\download .png")
img_4=Image.open("images\Screenshot_20230118_185256.jpg")


# ---- HEADER SECTION ----
with st.container():
    image_column, text_column = st.columns((1, 5))
    with image_column:
        st.image(img_4)
    st.subheader("Hi, I am Siddharth :wave:")
    st.title("A Budding Explorer :mag:")
    st.write(
        "A very Passionate, Motivated, Keen Learner & hard worker who always looks for opportunities to grow and excel"
    )


# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Meeting the technically ME!!!")
        st.write("##")
        st.write(
            """
            :pushpin: I am a budding ML & DS enthusiast.""")
        st.write(
            """
            :pushpin: Networking Domain & IoT stuffs also fascinates me""")
        st.write(
            """
            :pushpin: Good hands on Python, C/C++, Java""")
        st.write(
            """
            :pushpin: Completed Internship at skill vertex in Robotics & IoT field for 2 months""")
            
            


        st.write("[Linkden URL >](www.linkedin.com/in/siddharth-latthe-4ab69a213)")
        st.header("Meeting the Non-technical ME!!!")
        st.write("##")
        st.write(
            """
            :pushpin: Good at leadership skills""")
        st.write(
            """
            :pushpin: Descent at communication Skill""")
        st.write(
            """
            :pushpin: At leisure, prefer reading & watching Biopics and wildlife Documentaries
            """
        )
        st.write(
            """
            :pushpin: Sustain to have Multi-Tasking Capability
            """
        )
        st.write(
            """
            :pushpin: Descent percentage of Time Management
            """
        )


    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
    with right_column:
        st_lottie(lottie_code,height=300,key="data science")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_1)
    with text_column:
        st.subheader("IoT based Home Automation")
        st.write(
            """
            Learnt how to interface various sensors with arduino board using arduino programming.
            
            Built a circuit design which can automate the room right from opening and closing of the door
            to switching on & off the lights and fans.
            
            In this project, I have used various sensors like temperature,PIR,light,servo motor etc
            """
        )
        st.markdown("[Link to Project](https://www.tinkercad.com/things/1EuVD3aTIDn-homeautomation2)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_2)
    with text_column:
        st.subheader("Movie Recommendation System")
        st.write(
            """
            This project mainly focuses on giving the user a proper and accurate recommendation of the respective search that he/she does.
            In this project, we have taken a dataset from tmdb that contains over 5000 movies with detailed description.
            By applying various data analytics processes and by using python modules of Streamlit,pickle we have made a web interface for the same
            """
        )
        st.markdown("[Link to the project](https://github.com/Siddharth-Latthe-07/Movie-Recommended-System)")
with st.container():
    image_column, text_column = st.columns((1, 2))

    with text_column:
        st.subheader("Personal Voice Assistant")
        st.write(
            """
            In this project,I have used python programming to build my own customized voice assistant which can open any application I want. 
            I have used text to speech library, speech recognition library and many other libraries according to the application.
            """
        )
        st.markdown("[Link to the project](https://github.com/Siddharth-Latthe-07/Personal-Voice-Assistant)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Air Canvas using ML & Open Cv")
        st.write(
            """
             In this Project, I have made an Air Canvas that can draw anything as per the movement of my hand. 
             We have used the Mediapipe library for hand detection and landmarks.
             Further, created two windows as output,of which the first window will detect the real time movement through webcam and the second will draw the lines as per movement.
            """
        )
        st.markdown("[Link to the project](https://github.com/Siddharth-Latthe-07/Air-Canvas)")
with st.container():
    st.write("---")
    st.header("Internship")
    st.write("##")

    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_3)
    with text_column:
        st.subheader("IoT & Robotics")
        st.write(
            """
            In this internship, I have made a Home Automation System, wherein the lights,fans and doors are automated
            and can be controlled without human interference
            """
        )


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    st.write(":telephone_receiver: 7977472790")
    st.write(":email: siddharthlatthe@gmail.com")
    st.write(":house: Kolhapur")



