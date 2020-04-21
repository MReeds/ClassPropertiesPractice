# Define a Python class named Student.
# This class will have 5 properties.

# First name (string)
# Last name (string)
# Age (integer)
# Cohort number (integer)
# Full name (read-only string)
# Define getters for all properties.
# Define a setter for all but the read only property.
# Ensure that only the appropriate value can be assigned to each.
# The full name property should return first
# name and last name separated by a space.
# It's value cannot be set.


class Student():
    def __init__(self):
        pass

    @property
    def full_name(self):
        full_name = f"{self.firstName} {self.lastName}"
        return full_name.title()

    def __repr__(self):
        return f"{self.full_name} is {self.age} years old and is in cohort {self.cohortNumber}"

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, firstName):
        self.__first_name = firstName
        if type(firstName) == int:
            pass
        else:
            raise TypeError("Name must be valid characters")

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, lastName):
        self.__last_name = lastName
        if type(lastName) == str:
            print("all good")
        else:
            raise TypeError("Name must be valid characters")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, inputAge):
        self.__age = inputAge
        if type(inputAge) == int:
            pass
        else:
            raise TypeError("Age needs to be a number")

    @property
    def cohort_number(self):
        return self.__cohort_number

    @cohort_number.setter
    def cohort_number(self, cohortNumber):
        self.__cohort_number = cohortNumber


mike = Student()
mike.firstName = "Mike"
mike.lastName = "Jones"
mike.age = 30
mike.cohortNumber = 38
print(mike)
