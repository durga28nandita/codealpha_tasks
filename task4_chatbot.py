import tkinter as tk
root=tk.Tk()
root.title("Simple Chatbot")
root.geometry("500*400")

chat=tk.Text(root,width=60,height=20)
chat.pack()

entry=tk.Entry(root,width=40)
entry.pack()

button=tk.Button(root,text="Send")
button.pack()

def send():
    print("Button clicked!")
button=tk.Button(root,text="Send",command=send)
root.mainloop()

def chatbot():
    print("Chatbot: Hello!, type something to talk to me")
while True:
    userinput=input("You: ").lower()
    if userinput=="hello" or userinput=="hi":
        print("Chatbot:Hi")
    elif userinput=="how are you":
        print("Chatbot: I'm fine ,thanks!")
    elif userinput=="bye":
        print("Chatbot: Goodbye!")
        break
    else:
        print("Sorry, could'nt understand that")
chatbot()