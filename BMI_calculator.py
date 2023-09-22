def calc_bmi(hgtCm, wgt):
    hgt = hgtCm / 100
    bmi =  wgt / hgt ** 2
    return bmi

def result_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 24.9 <= bmi:
        return "Overweight"
    else :
        return "Obese"

while True:    
    print("\n\n------------------------------------Welcome to BMI (Body Mass Index) Calculator------------------------------------\n\n")
    hgtCm = float(input("Enter your height : "))
    wgt = float(input("Enter your weight : "))

    bmi = calc_bmi(hgtCm, wgt)

    interpretation = result_bmi(bmi)
    print(f"Your BMI is {bmi:.2f}, which is considered {interpretation}.")