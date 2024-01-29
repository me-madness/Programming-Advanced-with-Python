# First task from the lecture

class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

class MoreThanOneAtSymbol(Exception):
    pass

class InvalidNameError(Exception):
    pass
    
 
VALID_DOMAINS = (".com", ".bg", ".org", ".net", ) 
MIN_NAME_SYMBOLS_COUNT = 4

email = input()

while email != "End":
    
    if email.count("@") > 1:
        raise MoreThanOneAtSymbol("Email should contain only one @ symbol!")
    elif "@" not in email:
        raise MoreThanOneAtSymbol("Email must contain @!")
    
    
    email = input()

    
# Second task from me



