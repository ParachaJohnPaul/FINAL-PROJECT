def show_menu():
    print("Measurement Converter")
    print("1. Millimeters to Centimeters")
    print("2. Centimeters to Millimeters")
    print("3. Feet to Meters")
    print("4. Meters to Feet")
    print("5. Inches to Centimeters")
    print("6. Centimeters to Inches")

def mm_to_cm(mm):
    return mm / 10

def cm_to_mm(cm):
    return cm * 10

def ft_to_m(ft):
    return ft * 0.3048

def m_to_ft(m):
    return m / 0.3048

def in_to_cm(inches):
    return inches * 2.54

def cm_to_in(cm):
    return cm / 2.54

def main():
    show_menu()
    choice = input("Choose a conversion (1-6): ")
    value = float(input("Enter the value to convert: "))
    
    if choice == '1':
        result = mm_to_cm(value)
        print(f"{value} mm is {result} cm")
    elif choice == '2':
        result = cm_to_mm(value)
        print(f"{value} cm is {result} mm")
    elif choice == '3':
        result = ft_to_m(value)
        print(f"{value} ft is {result} m")
    elif choice == '4':
        result = m_to_ft(value)
        print(f"{value} m is {result} ft")
    elif choice == '5':
        result = in_to_cm(value)
        print(f"{value} inches is {result} cm")
    elif choice == '6':
        result = cm_to_in(value)
        print(f"{value} cm is {result} inches")
    else:
        print("Invalid choice, please select a valid option.")

if __name__ == "__main__":
    main()
