from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    download = str(round(sp.download() / (10 ** 6), 3)) + "Mbps"
    upload = str(round(sp.upload() / (10 ** 6), 3)) + "Mbps"
    lab_down.config(text=download)
    lab_up.config(text=upload)


sp = Tk()
sp.title("Internet speed")
sp.geometry("500x650")
sp.config(bg="blue")

# internet speed
lab = Label(sp, text="Internet speed-tester", font=("Time New Roman", 20, "bold"), bg="yellow")
lab.place(x=60, y=40, height=40, width=380)

# downloading speed
lab = Label(sp, text="Downloading speed", font=("Time New Roman", 20, "bold"), bg="black", fg="white")
lab.place(x=60, y=130, height=50, width=380)

# speed
lab_down = Label(sp, text="00", font=("Time New Roman", 20, "bold"), bg="black", fg="white")
lab_down.place(x=60, y=200, height=50, width=380)

# uploading speed
lab = Label(sp, text="Uploading speed", font=("Time New Roman", 20, "bold"), bg="black", fg="white")
lab.place(x=60, y=290, height=50, width=380)

# speed
lab_up = Label(sp, text="00", font=("Time New Roman", 20, "bold"), bg="black", fg="white")
lab_up.place(x=60, y=360, height=50, width=380)

# button
button = Button(sp, text="Check Speed", font=("poppins", 30, "bold"), relief=RAISED, bg="yellow", command=speedcheck)
button.place(x=60, y=460, height=40, width=380)

sp.mainloop()
