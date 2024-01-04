import tkinter as tk
from tkinter import ttk
import mysql.connector

def submit_data():
    student_name = student_name_entry.get()
    student_email = student_email_entry.get()
    gender = gender_type_entry.get()
    category = category_type_combobox.get()
    packs = packs_entry.get()

    # Connect to MySQL
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="netball_registration"
    )

    mycursor = mydb.cursor()

    # Inserting data into a table
    sql = "INSERT INTO student_data (Student_Name, Student_Email, Gender, Category, Packs) VALUES (%s, %s, %s, %s, %s)"
    val = (student_name, student_email, gender, category, packs)
    mycursor.execute(sql, val)
    mydb.commit()

    # Clear the entry fields after submission
    student_name_entry.delete(0, tk.END)
    student_email_entry.delete(0, tk.END)
    gender_type_entry.delete(0, tk.END)
    packs_entry.delete(0, tk.END)

    # Display a success message
    Student_info.configure(state='normal')
    Student_info.delete('1.0', tk.END)
    Student_info.insert(tk.END, "Thank you for your registration!")
    Student_info.configure(state='disabled')

# Your Main window, You need to have the title, geometry (MUST)
root = tk.Tk()
root.title("Netball Registration Form")
root.geometry('600x600')
root.configure(bg='#FFE5E5')

# Page title
label = tk.Label(root, text="Student Netball Registration", font=("Castellar", 16, "bold"), bg='#AC87C5')
label.grid(padx=20, pady=10)

frame = tk.Frame(root)
frame.grid()

# Student Info Frame
student_info_frame = tk.LabelFrame(frame, text="Student Information", font=("Castellar", 16, "bold"), bg='#756AB6')
student_info_frame.grid(row=0, column=0, padx=10, pady=20)

# Student Name
student_name_label = tk.Label(student_info_frame, text="Student Name", bg='#E0AED0')
student_name_label.grid(row=0, column=0, padx=5, pady=5)
student_name_entry = tk.Entry(student_info_frame)
student_name_entry.grid(row=1, column=0, padx=5, pady=5)

# Student Email
student_email_label = tk.Label(student_info_frame, text="Student Email", bg='#E0AED0')
student_email_label.grid(row=0, column=1, padx=5, pady=5)
student_email_entry = tk.Entry(student_info_frame)
student_email_entry.grid(row=1, column=1, padx=5, pady=5)

# Gender
gender_type_label = tk.Label(student_info_frame, text="Gender", bg='#E0AED0')
gender_type_label.grid(row=0, column=2, padx=5, pady=5)
gender_type_entry = tk.Entry(student_info_frame)
gender_type_entry.grid(row=1, column=2, padx=5, pady=5)

# Category
category_type_label = tk.Label(student_info_frame, text="Category", bg='#E0AED0')
category_type_combobox = ttk.Combobox(student_info_frame, values=["Primary School", "Secondary School"])
category_type_label.grid(row=2, column=0)
category_type_combobox.grid(row=3, column=0)

# Packs
packs_label = tk.Label(student_info_frame, text="Packs", bg='#E0AED0')
packs_label.grid(row=2, column=1, padx=5, pady=5)
packs_entry = tk.Entry(student_info_frame)
packs_entry.grid(row=3, column=1, padx=5, pady=5)

# Information by using textbox
Student_info = tk.Text(root, height=3, width=60)
Student_info.grid(pady=20)

# The defined list by using textbox
Student_info.insert(tk.END, "Registration is open to Primary school and Secondary school only! And open from 10 March until 10 May\n\n")
Student_info.configure(state='disabled')

for widget in student_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit data", command=submit_data)
submit_button.grid(pady=10)

label = tk.Label(root, text="Thank You for Your Registration!", font=("New York", 14, "bold"), bg="#AC87C5")
label.grid(padx=10, pady=10)

root.mainloop()