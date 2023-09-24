import random
from datetime import datetime, time
import time as t
import tkinter as tk


field_1 = ["Computer Science", "Data Science", "Software Engineering", "Information Technology",
           "Information Systems", "Mathematics", "Graphic Design", "Data Analytics", "Business Analytics",
           "Data Management", "Database Administration", "Digital Forensics"]

field_2 = ["Systems Engineering", "Electrical Engineering", "Mechanical Engineering", "Aerospace Engineering",
           "Telecommunications Engineering", "Industrial Engineering", "Computer Engineering",
           "Operations Research"]

field_3 = ["Cyber Security", "Cryptography", "Information Security", "Network Security", "Security Engineering",
           "Risk Management", "Physical Security", "Ethical Hacking & Pen-Testing", "Social Engineering",
           "Disaster Contingency", "Forensics", "Law Policy & Ethics"]

field_4 = ["Physics", "Chemistry", "Mechanics", "Materials Science & Engineering", "Civil Engineering",
           "Chemical Engineering", "Environmental Engineering"]

field_5 = ["Control Systems Engineering", "Robotics", "System Integration", "Signal Processing",
           "Applied Mathematics"]

field_6 = ["Architecture Design", "Building Technology", "History of Architecture", "Structural Engineering",
           "Environmental Design", "Landscape Architecture", "Urban Design", "Interior Design",
           "Building Information Modeling", "3D Art & Modeling", "Project Management", "Professional Practice"]

field_7 = ["Biology", "Anatomy", "Biochemistry", "Biophysics", "Pharmacology", "Medicine", "Cell Biology",
           "Ecology", "Evolution", "Genetics", "Microbiology", "Molecular Biology", "Neuroscience", "Physiology",
           "Biotechnology", "Bioinformatics", "Agriculture"]

field_8 = ["Machine Learning", "Artificial Intelligence", "Psychology", "Computational Neuroscience",
           "Neuroimaging", "Cognitive Neuroscience", "Neuroethics"]

field_9 = ["Mechatronics", "Control Theory", "Sensors & Actuators", "Robotics Applications",
           "Human-Robot Interaction", "Statistics", "Data Visualization", "Cloud"]

field_10 = ["Astrophysics", "Astronomy", "Nuclear Physics", "Engineering Physics", "Geophysics", "Medical Physics"]

field_11 = ["Polymer Chemistry", "Analytical Chemistry", "Medicinal Chemistry", "Computational Chemistry",
            "Food Chemistry", "Actuarial Science", "Financial Mathematics", "Computational Mathematics",
            "Mathematical Biology", "Mathematical Physics"]

field_12 = ["Biotechnology", "Environmental Science", "Zoology", "Botany", "Marine Biology"]

field_13 = ["Computer Graphics", "Game Design & Development", "Digital Media", "Photography", "Animation",
            "Visual Effects", "Film Production", "Art & Design", "Multimedia Design", "Web Design & Development",
            "User Experience Design", "Digital Media Production"]

field_14 = ["Construction Management", "Historical Preservation", "Industrial Design", "Sustainable Design"]

field_15 = ["Planetary Science", "Space Science", "Space Systems Engineering", "Remote Sensing", "Earth Science"]

Field = [field_1, field_2, field_3, field_4, field_5, field_6, field_7, field_8, field_9, field_10, field_11, field_12,
         field_13, field_14, field_15]


# Generate Random Subjects
def rs(n, exclude=None):
    if exclude is None:
        exclude = []
    exc = []
    fields = [field for field in Field if not any(sub in exclude for sub in field)]
    subjects = []
    for i in range(n):
        lst = random.choice(fields)
        subject = random.sample(lst, 1)
        subjects.append(subject)
        exc.append(subject)
    exclude.extend([item for sublist in exc for item in sublist])
    return subjects


X = 3
Y = 6
Z = []
x = rs(random.randint(X, Y), exclude=Z)
y = len(x)
z = random.randint(0, y - 1)

print("\nToday's Lists of Topics: \n")
for tp in x[0:y]:
    print(tp)

print(f"\nYour Topic of the Day is: \n{x[z]}")


# Textbox
def text_box():
    # Create a new window
    window = tk.Tk()
    window.title("Daily Topics")

    # Set the size and position of the window
    window.geometry("350x216+0+785")

    # Create a label with the current date and time
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    label = tk.Label(window, text=f"Today's Date & Time: {now}")
    label.pack()

    # Display the Random Topics in the Textbox
    textbox = tk.Text(window)
    textbox.insert(tk.END, "Today's Topics: \n")
    for topic in x[0:y]:
        textbox.insert(tk.END, f"{topic}\n")
    textbox.insert(tk.END, "\nYour Topic of the Day is: \n")
    textbox.insert(tk.END, f"{x[z]}")
    textbox.pack()

    # Run the window
    window.mainloop()


# Define the target time (10:00 AM)
T = time(10, 0, 0)


# Check Time Function
def check_time(target_time):
    # Get the current time
    now = datetime.now().time()

    # Calculate the time difference between the current time and the target time
    time_diff = datetime.combine(datetime.today(), target_time) - datetime.combine(datetime.today(), now)

    # Check if the current time is past the target time
    if now >= target_time:
        # Run the script
        text_box()
    else:
        # Wait until the target time and then run the script
        t.sleep(time_diff.seconds)
        text_box()


check_time(T)
