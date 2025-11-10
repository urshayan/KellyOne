from tkinter import *
from tkinter import messagebox

'''

   Source: https://en.wikipedia.org/wiki/Kelly_criterion
        
        The Formula: 
            f* = bp - q / b 

    f* = fraction of capital to invest
    b  = net odds recieved (e.g 1$ for each 1$ bet -> b = 1)
    p = probability of winning (50% = 0.5)
    q = 1 - p = probability of loosing

'''
def calc_kelly():
    ## All of the Logic Goes Here!
    try:
        p = float(p_value.get())
        b = float(b_value.get())
        cap = float(capital.get())

        if not (0 < p < 1):
            messagebox.showerror("Invalid Input","Probability must be between 0 & 1")
            return
    
        q = 1 - p
        ### Calculation goes here!
        f_star = (b * p - q) / b 

        if f_star <= 0:
            result.config(text="Kelly Suggests not taking this bet", fg="red")
            suggestion.config(text="DO NOT TAKE THIS TRADE!", fg="red")
        else:
            invest_amount = f_star * cap 
            result.config(text=f"Optimal Fraction : {f_star: .2%} \n Recommended Investment : {invest_amount: .2f} " , fg="green")
            half_kely = round(invest_amount/2 , 2)
            quarter_kely = round(invest_amount/4 , 2) 
            
            suggestion.config(text=f" Suggested \n  Half Kelly Investment Amount: {half_kely} \n Quarter Kelly Investment Amount : {quarter_kely} " , fg="blue")
    except ValueError:
        messagebox.showerror("Error!","Please Enter Valid Numbers!")

        
window = Tk()
window.title("KellyOne")
window.config(bg="#121212")

title = Label(window, text="KellyOne Calculator", font=("Nunito Sans",16,"bold"),bg="#101820", fg="#00AEEF")
title.pack(pady=10)

frame = Frame(window, bg="#0A2540")
frame.pack(pady = 10)


Label(frame,text="Probablity of Winning (p)",bg="#00B4D8",fg="white").grid(row=0,column=0 ,padx = 10)
p_value = Entry(frame)
#p_value.insert(0, '0.3')
p_value.grid(row=0,column =1, padx = 10 , pady = 10)

Label(frame, text="Reward-Risk Ratio (b)",bg="#00B4D8",fg="white").grid(row=1,column=0)
b_value = Entry(frame)
b_value.grid(row=1,column=1, padx = 10 , pady= 10)

Label(frame, text="Total Capital", bg="#00B4D8", fg="white").grid(row=2, column = 0)
capital = Entry(frame)
capital.grid(row=2,column=1,padx = 10 , pady = 10)

calc_button = Button(window, text="Calucalate Kelly!", command=calc_kelly,bg="#00AEEF", fg="white", relief="raised")
calc_button.pack(pady = 10)

# Add both result and Kelly Suggestion!
result = Label(window,text="")
result.pack(pady = 10)

suggestion = Label(window, text="")
suggestion.pack(pady = 10)



window.mainloop()

