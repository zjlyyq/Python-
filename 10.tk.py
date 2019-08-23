from tkinter import Button, mainloop
button = Button(
    text='This is a button',
    command=lambda: print('being pressed')) # 点击时调用 lambda 函数
button.pack()
mainloop()
