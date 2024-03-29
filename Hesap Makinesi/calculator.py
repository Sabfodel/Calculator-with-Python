import tkinter as tk

pencere = tk.Tk()
pencere.title("Sabfodel's Calculator")

bg = tk.PhotoImage(file=r"C:\Users\sabri\OneDrive\Masaüstü\hesap.png")

background_label = tk.Label(pencere, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def topla():
    sa1=float(say1.get())
    sa2=float(say2.get())
    sonuc.configure(text=str(sa1+sa2))

def carp():
    sa1=float(say1.get())
    sa2=float(say2.get())
    sonuc.configure(text=str(sa1*sa2))
def bol():
    sa1=float(say1.get())
    sa2=float(say2.get())
    sonuc.configure(text=str(sa1/sa2))
def ckar():
    sa1=float(say1.get())
    sa2=float(say2.get())
    sonuc.configure(text=str(sa1-sa2))




sonuc = tk.Label(pencere,text="Sonuc = ",font="Lucid 20 bold",width=30,justify="right")
sonuc.place(x = 40, y =520)
say1 = tk.Entry(pencere, font="Lucid 20 bold",width=20,justify="left")
say1.place(x = 0 ,y=300)
say2 = tk.Entry(pencere, font="Lucid 20 bold",width=20,justify="left")
say2.place (x= 0, y = 340)




#İşlem Fonksiyonları

toplama = tk.Button(pencere,text="+",font="Lucid 20 bold",width=10,justify="right",command=topla)
toplama.place(x=0 , y=400)
carpma = tk.Button(pencere,text="x",font="Lucid 20 bold",width=10,justify="right",command=carp)
carpma.place(x=0 ,y=440)
bolme = tk.Button(pencere,text="÷",font="Lucid 20 bold",width=10,justify="right",command=bol)
bolme.place(x=0 ,y=480)
ckarma = tk.Button(pencere,text="-",font="Lucid 20 bold",width=10,justify="right",command=ckar)
ckarma.place(x=0 ,y=520)








pencere.geometry("400x650")
pencere.mainloop()