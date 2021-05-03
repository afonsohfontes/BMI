def colectInfo():
    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))
    age = float(input("Please enter your age in years: "))
    if (age <= 20) and (age >= 2):
        gender = input("Please enter your gender (M - Male, F - Female): ")
        while (gender != 'M' or gender != 'm' or gender != 'F' or gender != 'f'):
            print("You have entered an invalid option, please try again.")
            gender = input("Enter your gender (M - Male, F - Female): ")
    else:
        gender ='irrelevant'
    return height, weight, age, gender
    
def calculateBMI(height, weight):
    BMI = weight / (height/100)**2
    return BMI

def classifyBMI(BMI, age, gender):
    if age > 19:
        if BMI <= 18.4:
            return ("You are underweight.")
        elif BMI <= 24.9:
            return ("You are healthy.")
        elif BMI <= 29.9:
            return ("You are over weight.")
        elif BMI <= 34.9:
            return ("You are severely over weight.")
        elif BMI <= 39.9:
            return ("You are obese.")
        else:
            return ("You are severely obese.")

    elif age>=2:
        if (gender == 'f' or gender == 'F'): #values are an approximation of values from this table: https://www.obesityaction.org/get-educated/understanding-childhood-obesity/what-is-childhood-obesity/girls-bmi-for-age-percentile-chart/
            if age <=4:
                if BMI <= 14:
                    return ("You are underweight.")
                elif BMI <= 17.5:
                    return ("You are healthy.")
                elif BMI <= 18.5:
                    return ("You are over weight.")
                else:
                    return ("You are obese.")

            elif age <=7:
                if BMI <= 13.5:
                    return ("You are underweight.")
                elif BMI <= 14:
                    return ("You are healthy.")
                elif BMI <= 20:
                    return ("You are over weight.")
                else:
                    return ("You are obese.")

            elif age <=10:
                if BMI <= 14:
                    return ("You are underweight.")
                elif BMI <= 20:
                    return ("You are healthy.")
                elif BMI <= 22:
                    return ("You are over weight.")
                else:
                    return ("You are obese.")

            elif age <=13:
                if BMI <= 15:
                    return ("You are underweight.")
                elif BMI <= 22:
                    return ("You are healthy.")
                elif BMI <= 26.5:
                    return ("You are over weight.")
                else:
                    return ("You are obese.")

            elif age <=16:
                if BMI <= 16.5:
                    return ("You are underweight.")
                elif BMI <= 24.5:
                    return ("You are healthy.")
                elif BMI <= 29:
                    return ("You are over weight.")
                else:
                    return ("You are obese.")

            elif age <=19:
                if BMI <= 17.5:
                    return ("You are underweight.")
                elif BMI <= 26.5:
                    return ("You are healthy.")
                elif BMI <= 31:
                    return ("You are over weight.")
                else:
                    return ("You are obese.")

        if (gender == 'm' or gender == 'M'): #values are an approximation of values from this table: https://www.obesityaction.org/get-educated/understanding-childhood-obesity/what-is-childhood-obesity/boys-bmi-chart/
            if age <=4:
                if BMI <= 14.5:
                    return ("You are underweight.")
                elif BMI <= 17.5:
                    return ("You are healthy.")
                elif BMI <= 18.5:
                    return ("You are over weight.")
                else:
                    return ("You are obese.")

            elif age <=7:
                if BMI <= 14:
                    return ("You are underweight.")
                elif BMI <= 17.5:
                    return ("You are healthy.")
                elif BMI <= 19.5:
                    return ("You are over weight.")
                else:
                    return ("You are obese.")

            elif age <=10:
                if BMI <= 14.5:
                    return ("You are underweight.")
                elif BMI <= 19:
                    return ("You are healthy.")
                elif BMI <= 22:
                    return ("You are over weight.")
                else:
                    return ("You are obese.")

            elif age <=13:
                if BMI <= 15.5:
                    return ("You are underweight.")
                elif BMI <= 21.5:
                    return ("You are healthy.")
                elif BMI <= 25:
                    return ("You are over weight.")
                else:
                    return ("You are obese.")

            elif age <=16:
                if BMI <= 17:
                    return ("You are underweight.")
                elif BMI <= 23.5:
                    return ("You are healthy.")
                elif BMI <= 27.5:
                    return ("You are over weight.")
                else:
                    return ("You are obese.")

            elif age <=19:
                if BMI <= 18.5:
                    return ("You are underweight.")
                elif BMI <= 26:
                    return ("You are healthy.")
                elif BMI <= 29.5:
                    return ("You are over weight.")
                else:
                    return ("You are obese.")
                    
if __name__ == "__main__":
    h, w, a, g = colectInfo()
    if a<2:
        print("This calculator does not apply for children bellow 2 years old. Please visit a professional.")
    else:
        b = calculateBMI(h, w)
        print(f"You BMI is {b}")
        print(classifyBMI(b, a, g))