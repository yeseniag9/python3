from cmath import pi

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