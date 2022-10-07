from cmath import pi

def area():
    while True:
        response = input("To have your house footage calculated, enter yes; otherwise, enter no. ")
        
        if response.lower() == 'yes':
            print("House square footage: ")
            user_response_length = input("Enter length: ")
            user_response_width = input("Enter width: ")
            calculation = int(user_response_length)*int(user_response_width)
            print(f'The square footage of your house is {calculation} ft^2.')
        else:
            break
    
area()


print(5*5)

def circumference():
    while True:
        response = input("To calculate a circle's circumference, enter yes; otherwise, enter no. ")
        
        if response.lower() == 'yes':
            print("Circumference of circle: ")
            user_response_radius = input("Enter radius: ")
            calculation2 = int(user_response_radius)*2*pi
            print(f'The circumference of your circle is {calculation2}.')
        else:
            break
    
circumference()