from tkinter import *
from backend.blockchain.blockchain import Blockchain

blockchain = Blockchain()

def show_chain():
    json_string = blockchain.to_json()
    resault_dis.configure(text=json_string)

#============ color Palette ==============>

c1 = '#393E46' #black
c2 = '#EEEEEE' #white
c3 = '#76EAD7' #green
c4 = '#C4FB6D' #Greener

#============ window Configuration ==============>

main_window = Tk()
main_window.title("Python blockchain ")
main_window.geometry("800x250")
main_window.resizable(width=False,height=False)
main_window.configure(bg=c1)

# ===============Header=====================>
header = Frame(main_window,bg=c1,height=50)
header.pack(side=TOP, fill="x")
gap = Frame(header,height=12,bg=c1)
gap.pack(side=TOP,fill="x")
header_txt = Label(header,bg=c1 ,text=" نمایش بلاک جنسیس در پایتون ", fg=c4,font=("ariel",20,"bold"))
header_txt.pack(side=TOP)
gap = Frame(header,height=12,bg=c1)
gap.pack(side=TOP,fill="x")


# ===============resault panle=====================>


resault = Frame(main_window,bg=c1,height=50)
resault.pack(side=TOP, fill="x")

resault_dis = Label(resault,text="",width=100 , height=6 , bg=c3,font=("ariel",10,"bold"))

resault_dis.pack(side=TOP)

# =============== submit =====================>
btn_show = Frame(main_window,bg=c1,height=50)
btn_show.pack(side=TOP, fill="x")

gap = Frame(btn_show,height=12,bg=c1)
gap.pack(side=TOP,fill="x")

add_btn= Button(btn_show,text= "نمایش" ,width=30, height=2 , bg=c1 , fg=c4 , command = show_chain )
add_btn.pack(side=TOP )


main_window.mainloop()