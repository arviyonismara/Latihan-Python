import tkinter

main_window = tkinter.Tk()

# Class .Label
label1 = tkinter.Label(main_window, text = "Label 1")
label2 = tkinter.Label(main_window, text = "Label 2")

# Class .Button
tombol1 = tkinter.Button(main_window, text = "Button 1")
tombol2 = tkinter.Button(main_window, text = "Button 2")

# method positioning
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

# method menampilkan GUI
main_window.mainloop()