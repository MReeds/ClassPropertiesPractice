class Patient():
    def __init__(self, ssn, dob, ian, first_name, last_name, physical_address):
        self.__social_security_number = ssn
        self.__date_of_birth = dob
        self.__insurance_account_number = ian
        self.__firstName = first_name
        self.__lastName = last_name
        self.__address = physical_address

    @property
    def social_security_number(self):
        try:
            return self.__social_security_number
        except AttributeError:
            return 0

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @property
    def insurance_account_number(self):
        return self.__insurance_account_number

    @property
    def full_name(self):
        try:
            fullName = f"{self.__firstName} {self.__lastName}"
            return fullName.title()
        except AttributeError:
            return 0

    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, new_address):
        try:
            return self.__address
        except AttributeError:
            return 0


patient1 = Patient("111-11-1111", "08/08/1997", "22-222-2222",
                   "Mary", "Jenkins", "102 Hillwood Run")