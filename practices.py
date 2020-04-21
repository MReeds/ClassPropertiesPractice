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
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.title()

    def __repr__(self):
        return f"{self.full_name} is {self.age} years old and is in cohort {self.cohortNumber}"

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, firstName):
        if type(firstName) is str:
            self.__first_name = firstName
        else:
            raise TypeError("Name must be valid characters")

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, lastName):
        if type(lastName) == str:
            self.__last_name = lastName
        else:
            raise TypeError("Name must be valid characters")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, inputAge):
        if type(inputAge) is int:
            self.__age = inputAge
        else:
            raise TypeError("Age needs to be a number")

    @property
    def cohort_number(self):
        return self.__cohort_number

    @cohort_number.setter
    def cohort_number(self, cohortNumber):
        self.__cohort_number = cohortNumber


mike = Student()
mike.first_name = "Bob"
mike.last_name = "Jones"
mike.age = 30
mike.cohortNumber = 38
print(mike.full_name)

# print(dir(Student))
