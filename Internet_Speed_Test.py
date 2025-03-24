from tkinter import *
import speedtest

def speed_check():
    try:
        sp = speedtest.Speedtest()
        sp.get_best_server()  # Ensures a proper server is selected
        download_speed = f"{round(sp.download() / (10**6), 2)} Mbps"
        upload_speed = f"{round(sp.upload() / (10**6), 2)} Mbps"
        lab_down.config(text=download_speed)
        lab_down.place(x=155,y=180)
        lab_up.config(text=upload_speed)
        lab_up.place(x=155,y=330)
    except Exception as e:
        lab_down.config(text="Error")
        lab_up.config(text="Error")
        print("Error:", e)  # Debugging output

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("400x500")
sp.config(bg="black")

Label(sp, text="Internet Speed Test", font=("Arial", 20, "bold"), bg="black", fg="white").place(x=65, y=40, height=50, width=290)

Label(sp, text="Download Speed", font=("Arial", 15, "bold"), bg="black", fg="white").place(x=125, y=100)
lab_down = Label(sp, text="00.00", font=("Arial", 15, "bold"), bg="black", fg="white")
lab_down.place(x=175, y=180)

Label(sp, text="Upload Speed", font=("Arial", 15, "bold"), bg="black", fg="white").place(x=140, y=250)
lab_up = Label(sp, text="00.00", font=("Arial", 15, "bold"), bg="black", fg="white")
lab_up.place(x=175, y=330)

Button(sp, text="Check Speed", font=("Arial", 15, "bold"), relief=RAISED, bg="blue", fg="white", command=speed_check).place(x=130, y=400, height=40, width=150)

sp.mainloop()
