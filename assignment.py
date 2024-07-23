# Team Members: [full names of all team members]
# Course: CS701/GB735, Dr. Rajeev
# Date: [Submission date]
# Programming Assignment: 1
# Program Inputs: Dimensions of the room (length, width, height) in feet
# Program Outputs: Total area to be painted (in square feet), amount of primer (in gallons), amount of paint (in gallons)

def main():
    # Step 1: Ask the user for the dimensions of the room
    length = float(input("Enter the length of the room in feet: "))
    width = float(input("Enter the width of the room in feet: "))
    height = float(input("Enter the height of the room in feet: "))

    # Step 2: Compute the total area of the four walls and ceiling
    # Area of walls = 2 * (length * height + width * height)
    area_walls = 2 * ((length * height) + (width * height))
    # Area of ceiling = length * width
    area_ceiling = length * width
    # Total area = Area of walls + Area of ceiling
    total_area = area_walls + area_ceiling

    # Step 3: Calculate the amount of primer and paint needed
    # Primer coverage = 200 square feet per gallon
    primer_needed = total_area / 200
    # Paint coverage = 350 square feet per gallon
    paint_needed = total_area / 350

    # Step 4: Output the total area and the amount of primer and paint needed
    print(f"Total area to be painted: {total_area:.2f} square feet")
    print(f"Amount of primer needed: {primer_needed:.2f} gallons")
    print(f"Amount of paint needed: {paint_needed:.2f} gallons")

if __name__ == "__main__":
    main()