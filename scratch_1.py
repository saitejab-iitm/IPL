import streamlit as st
import pandas as pd
import sqlite3
import streamlit as st
import PyPDF2


hover_color_css = """
    <style>
        .foundational:hover {
            background-color: #50B8E7; /* Change this to the desired hover color */
        }
        .diploma:hover {
            background-color: #77dd77; /* Change this to the desired hover color */
        }
        .degree:hover {
            background-color: #FFC52B; /* Change this to the desired hover color */
        }
    </style>
"""

st.markdown(hover_color_css, unsafe_allow_html=True)

button_label = " Diploma "
button_html = f'<div style="display: flex; justify-content: center;"><button class="foundational" style="padding: 20px; text-align: left;line-height: 120%; margin: 20px; border-radius: 5px; border: 2px white;">Foundational Courses</button><button class="diploma" style="padding: 20px; text-align: left;line-height: 120%; margin: 20px; border-radius: 5px; border: 2px white;">Diploma Courses</button><button class="degree" style="padding: 20px; text-align: left;line-height: 120%; margin: 20px; border-radius: 5px; border: 2px white;">Degree Courses</button></div>'
st.markdown(button_html, unsafe_allow_html=True)


# Function to read and update page view count
def update_page_views():
    # Read the current page view count from the data store
    with open("C:/Users/saite/AppData/Roaming/JetBrains/PyCharmCE2022.1/scratches/page_views.txt", "r") as file:
        page_views = int(file.read())

    # Increment the page view count
    page_views += 1

    # Update the data store with the new count
    with open("C:/Users/saite/AppData/Roaming/JetBrains/PyCharmCE2022.1/scratches/page_views.txt", "w") as file:
        file.write(str(page_views))

    return page_views


# Get and display the current page view count
page_views = update_page_views()
st.write(f"Page Views: {page_views}")

# Create a Streamlit app
st.title("Colored Containers Example")
hi="4"
# Define custom CSS styles for colored containers
red_container = f"""
    <div style="background-color: #7beaf3; padding: 5px; text-align: left;line-height: 120%; margin: 20px; margin-bottom: 50px; border-radius: 20px; border: 2px white;">
        <i style="padding-left: 2%">    Mathematics for Data Science 1 </i>
        <div style="background-color: white; padding: 5px; text-align: left;line-height: 100%; margin: 5px; border-radius: 20px; display: flex;">
            <div style="flex: 70%;">
            <p style="font-size: 200%; margin-top: 2%;">Study Session: Week1</p>
            <p style="margin-top: 2%;">Teaching Assistants: User1 (CGPA 9.5, S in Maths1)</p>
            <p> Every saturday 7pm-9pm </p>
            </div>
            <div style="flex: 30%">
            <p style="margin-top: 4%; font-size: 75%;"> Starts: </p>
            <p style="font-size: 170%; margin-top: 10%; text-align: center;"> 1d 12hr 35min <p>
            </div>
        </div>
    </div>
"""

green_container = """
    <div style="background-color: green; padding: 20px; text-align: center;">
        <h2>Green Container</h2>
        <p>This is a green container.</p>
    </div>
"""

blue_container = """
    <div style="background-color: blue; padding: 20px; text-align: center;">
        <p>Your Score:</p>
        <h2>76/100</h2>
        <p>You attempted 10 out of 15 questions</p>
    </div>
"""

# Display the colored containers using Markdown
st.markdown(red_container, unsafe_allow_html=True)
st.markdown(green_container, unsafe_allow_html=True)
st.markdown(blue_container, unsafe_allow_html=True)
st.markdown('----')
def btn_b_callback():
    st.session_state.display_result = False
    st.session_state.reset = False



if 'display_result' not in st.session_state:
    st.session_state.display_result = False
if 'reset' not in st.session_state:
    st.session_state.reset = False

st.header("My Demo App")
result = "My Custom Text"




show_button = st.checkbox("Show Button")

if show_button:
    button_clicked = st.button("Click me!")
    if button_clicked:
        st.write("Button clicked!")
        # Replace the button with empty content
        st.empty()




answer = ''
check_button = False
Total = []
User = []

for i in range(5):
    answer = st.radio("select an option",["1","2","3","4"],key=i)

    if answer == "2":
        Total.append(1)
        User.append(1)
    else:
        Total.append(1)
        User.append(0)

check_button = st.button("submit")

if check_button:
    st.write(f"Score: {Total} --- {User}")



import time


timer_running = st.checkbox("Start Timer")

if timer_running:
    start_time = time.time()
    elapsed_time = 0
    while elapsed_time <= 10 and timer_running:
        elapsed_time = time.time() - start_time
        st.write(f"Elapsed Time: {elapsed_time:.2f} seconds")
        time.sleep(1)  # Update every 1 second

        timer_running = st.checkbox("Pause Timer")

st.write("Timer Stopped")







score = 80
total_questions = 5
attempted_questions = 3

# Create a container with specified styles
with st.container():
    st.markdown(
        """
        <style>
        .score-container {
            border: 2px dotted #008080;
            background-color: #e0f2f1;
            padding: 20px;
            text-align: center;
        }
        .score {
            font-size: 2em;
        }
        .attempted {
            font-size: 1em;
            margin-top: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Container content
    st.markdown('<div class="score-container">', unsafe_allow_html=True)

    st.markdown('<p class="score">My Score</p>', unsafe_allow_html=True)

    st.markdown(f'<p class="score">{score} out of 100</p>', unsafe_allow_html=True)

    st.markdown(f'<p class="attempted">You attempted {attempted_questions} out of {total_questions} questions</p>',
                unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

import streamlit as st
import fitz  # PyMuPDF

def extract_pdf_images(uploaded_file):
    pdf_images = []
    pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        image_list = page.get_pixmap_images(full=True)

        for image in image_list:
            img_data = image.get_image_data(output="png")
            pdf_images.append(img_data)

    pdf_document.close()

    return pdf_images

st.title("PDF Image Extractor")


# Create a dictionary with question data
questions_data = {
    1: {
        "Question": "What is the capital of France?",
        "Marks": 5,
        "Subject": "Geography",
        "User_Response": "Paris",
    },
    2: {
        "Question": "Who wrote the play 'Romeo and Juliet'?",
        "Marks": 5,
        "Subject": "Literature",
        "User_Response": "William Shakespeare",
    },
    3: {
        "Question": "What is the chemical symbol for water?",
        "Marks": 5,
        "Subject": "Chemistry",
        "User_Response": "H2O",
    },
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame.from_dict(questions_data, orient="index")

# Streamlit app title
st.title("Question Data")

# Display the DataFrame as a table
st.write(df)


# Create a sample DataFrame
data = {
    "Column 1": [1, 2, 3],
    "Column 2": [4, 5, 6],
    "Column 3": [7, 8, 9]
}

df = pd.DataFrame(data)

# Streamlit app title
st.title("Adding Spacing to a Streamlit Table")

# Custom CSS to add spacing between rows and columns
custom_css = """
    <style>
        table {
            border-collapse: separate;
            border-spacing: 0px; /* Adjust the spacing as needed */
        }
        th, td {
            padding: 5px; /* Adjust the padding as needed */
        }
    </style>
"""
st.write(custom_css, unsafe_allow_html=True)

# Display the DataFrame as a table
st.table(df)

conn = sqlite3.connect("database.db")  # Update with your database name
cursor = conn.cursor()

cursor.execute("SELECT subjectname FROM Subjects")
subjects = cursor.fetchall()
frame = []
for i in subjects:
    if i not in frame:
        frame.append(i)
        st.write(i[0])

conn.close()


pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if pdf_file is not None:
    # Read PDF file
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)
    text = ""
    for page_number in range(num_pages):
        page = pdf_reader.pages[page_number]
        text += page.extract_text()
    st.write(text)










