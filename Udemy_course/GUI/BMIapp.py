from tkinter import *


root = Tk()
root.title("BMI App")
root.geometry("640x480")
root.resizable(width = False, height = False)


label_for_height = Label(
    text = "Enter your height (m.) : ",
    font = ("Times new roman", 18)
)

entry_for_height = Entry(
    width = 20,
    font = ("Times new roman", "30"),
    justify = CENTER
)
label_for_weight = Label(
    text = "Enter your weight (kg.) : ",
    font = ("Times new roman", "18")
)
entry_for_weight = Entry(
    width = 20,
    font = ("Times new roman", "30"),
    justify = CENTER
)

# BMI = weight / (height**2)
def calculate():
    height = float(entry_for_height.get())
    weight = float(entry_for_weight.get())
    bmi = weight / (height**2)

    if bmi <=16:
        status = "severe underweight"
    elif bmi > 16 and bmi <18.5:
        status = "underweight"
    elif bmi >= 18.5 and bmi <25:
        status = "ok"
    elif bmi >= 25 and bmi <30:
        status = "overweight"
    elif bmi >= 30 and bmi <35:
        status = "obesity 1 degree"
    elif bmi >=35 and bmi < 40:
        status = "obesity  degree"
    else:
        status = "obesity 3 degree"


    result_label = Label(
        text = f"""
    Your bmi: {bmi} кг/м2\n
    This is {status}
        """,
        font = ("Times new roman", "18")
    )
    result_label.pack()



submit_button = Button(
    text = "Calculate",
    font = ("Times new roman", "16"),
    command = calculate
)


label_for_height.pack()
entry_for_height.pack()
label_for_weight.pack()
entry_for_weight.pack()
submit_button.pack()




if __name__ == "__main__":
    root.mainloop()