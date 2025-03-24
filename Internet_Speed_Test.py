import speedtest
import tkinter as tk

def speed_check():
    try:
        # Show "Loading..." while fetching speeds
        lab_down.config(text="Loading...", fg="yellow")
        lab_up.config(text="Loading...", fg="yellow")
        root.update()  # Update the UI to reflect "Loading..."

        sp = speedtest.Speedtest()
        sp.get_servers()  # Selects the best speedtest server

        download_speed = f"{round(sp.download() / (10**6), 2)} Mbps"
        upload_speed = f"{round(sp.upload() / (10**6), 2)} Mbps"

        # Update labels with final results
        lab_down.config(text=download_speed, fg="green")
        lab_up.config(text=upload_speed, fg="green")

    except Exception as e:
        lab_down.config(text="Error", fg="red")
        lab_up.config(text="Error", fg="red")
        print("Error:", e)  # Debugging output

# Tkinter setup
root = tk.Tk()
root.title("Internet Speed Test")
root.geometry("400x500")
root.config(bg="black")

tk.Label(root, text="Internet Speed Test", font=("Arial", 20, "bold"), bg="black", fg="white").place(x=65, y=40, height=50, width=290)

tk.Label(root, text="Download Speed", font=("Arial", 15, "bold"), bg="black", fg="white").place(x=125, y=100)
lab_down = tk.Label(root, text="00.00 Mbps", font=("Arial", 15, "bold"), bg="black", fg="white")
lab_down.place(x=150, y=180)

tk.Label(root, text="Upload Speed", font=("Arial", 15, "bold"), bg="black", fg="white").place(x=140, y=250)
lab_up = tk.Label(root, text="00.00 Mbps", font=("Arial", 15, "bold"), bg="black", fg="white")
lab_up.place(x=150, y=330)

tk.Button(root, text="Check Speed", font=("Arial", 15, "bold"), relief=tk.RAISED, bg="blue", fg="white", command=speed_check).place(x=130, y=400, height=40, width=150)

root.mainloop()
