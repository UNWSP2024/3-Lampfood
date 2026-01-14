#Elliott Morris, 1/14/2026, Age Classifier
#This program asks for an age and categorizes it based on an if-elif tree

#function to categorize the age
def categorize_age(age):
    # placeholder variable
    ageCategory = "TBD"

    #decision structure to find age
    if age < 0 or age > 100:
        ageCategory = "Invalid age"
    elif age > 0 and age <= 1:
        ageCategory = "Infant"
    elif age > 1 and age < 13:
        ageCategory = "Child"
    elif age >= 13 and age < 20:
        ageCategory = "Teenager"
    elif age >= 20 and age < 100:
        ageCategory = "Adult"

    return ageCategory

#Main script
if __name__ == '__main__':
    # Local variables
    # Get age from the user.
    age = float(input("Enter the person's age: "))
    # Display the age
    ageBucket = categorize_age(age)
    print (ageBucket)
