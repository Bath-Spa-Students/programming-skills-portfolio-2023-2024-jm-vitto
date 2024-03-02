def calculate_area(base, height):
    # Calculate the area of the triangle
    area = 0.5 * base * height
    return area

def main():
    # Prompt the user to enter the base and height of the triangle
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))

    # Calculate the area of the triangle
    area = calculate_area(base, height)

    # Display the result
    print("The area of the triangle is:", area)

if __name__ == "__main__":
    main()
