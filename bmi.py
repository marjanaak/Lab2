def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / (height ** 2)
    print("BMI = " + str(bmi))

    if bmi < 18.5:
        print("Under Weight")
    if 18.5 <= bmi <= 25.0:
        print("Normal Weight")
    if bmi > 25.0:
        print("Over Weight")
calculate_bmi(weight=57, height=1.73)