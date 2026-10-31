import tkinter
from tkinter import messagebox
import openpyxl

# Create main Window
window = tkinter.Tk()
window.geometry("400x350")
window.title("Student Registration - FATIMA WANI")

# Display your name
name_heading = tkinter.Label(
    window, text="FATIMA WANI",
    font=("Arial", 14, "bold")
)
name_heading.pack()

# Excel file path
file_path = r"C:\Users\fatim\Downloads\textfile.xlsx"

# Load Excel workbook
A = openpyxl.load_workbook(file_path)

# Select Worksheet
B = A["Registration"]

def Onclick_Submit():
    name = name_textbox.get()
    email = email_textbox.get()
    phone = phone_textbox.get()

    # Check whether all fields are filled
    if name and email and phone:

        # Store data in the next empty row
        B.append([name, email, phone])

        # Save Excel file
        A.save(file_path)

        messagebox.showinfo(
            "Success", "Data saved successfully!"
        )

        # Clear the textboxes
        name_textbox.delete(0, tkinter.END)
        email_textbox.delete(0, tkinter.END)
        phone_textbox.delete(0, tkinter.END)

    else:
        messagebox.showwarning(
            "Warning", "Please fill all fields!"
        )

# Name
name_label = tkinter.Label(window, text="Name:")
name_label.pack()

name_textbox = tkinter.Entry(window, width=30)
name_textbox.pack()

# Email
email_label = tkinter.Label(window, text="Email:")
email_label.pack()

email_textbox = tkinter.Entry(window, width=30)
email_textbox.pack()

# Phone
phone_label = tkinter.Label(window, text="Phone:")
phone_label.pack()

phone_textbox = tkinter.Entry(window, width=30)
phone_textbox.pack()

# Submit Button
submit_button = tkinter.Button(
    window, text="Submit", command=Onclick_Submit
)
submit_button.pack()

# Run the application
window.mainloop()