import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_66=tk.Button(root)
        GButton_66["bg"] = "#6b6b6b"
        ft = tkFont.Font(family='Times',size=10)
        GButton_66["font"] = ft
        GButton_66["fg"] = "#ffffff"
        GButton_66["justify"] = "center"
        GButton_66["text"] = "Input"
        GButton_66.place(x=250,y=360,width=70,height=25)
        GButton_66["command"] = self.GButton_66_command

        GButton_357=tk.Button(root)
        GButton_357["bg"] = "#6b6b6b"
        ft = tkFont.Font(family='Times',size=10)
        GButton_357["font"] = ft
        GButton_357["fg"] = "#ffffff"
        GButton_357["justify"] = "center"
        GButton_357["text"] = "Output"
        GButton_357.place(x=250,y=400,width=70,height=25)
        GButton_357["command"] = self.GButton_357_command

        GMessage_953=tk.Message(root)
        ft = tkFont.Font(family='Times',size=28)
        GMessage_953["font"] = ft
        GMessage_953["fg"] = "#c8c3bc"
        GMessage_953["justify"] = "center"
        GMessage_953["text"] = "DAT Bio Tracker"
        GMessage_953.place(x=150,y=80,width=263,height=86)

        GMessage_824=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_824["font"] = ft
        GMessage_824["fg"] = "#c8c3bc"
        GMessage_824["justify"] = "center"
        GMessage_824["text"] = "Select 'Input' to add an entry."
        GMessage_824.place(x=150,y=180,width=214,height=32)

        GMessage_810=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_810["font"] = ft
        GMessage_810["fg"] = "#c8c3bc"
        GMessage_810["justify"] = "center"
        GMessage_810["text"] = "- It is recommended to log each day."
        GMessage_810.place(x=170,y=210,width=240,height=30)

        GMessage_124=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_124["font"] = ft
        GMessage_124["fg"] = "#c8c3bc"
        GMessage_124["justify"] = "center"
        GMessage_124["text"] = "Select 'Output' for visualization of data logged"
        GMessage_124.place(x=140,y=250,width=331,height=30)

        GMessage_748=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_748["font"] = ft
        GMessage_748["fg"] = "#c8c3bc"
        GMessage_748["justify"] = "center"
        GMessage_748["text"] = "- It is recommended to have a few weeks worth of logs for proper visualizing"
        GMessage_748.place(x=190,y=280,width=305,height=40)

    def GButton_66_command(self):
        print("command")


    def GButton_357_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
