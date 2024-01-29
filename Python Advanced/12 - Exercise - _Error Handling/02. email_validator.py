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
    elif len(email.split("@")[0]) <= MIN_NAME_SYMBOLS_COUNT:
        raise NameTooShortError("Name must be more than 4 characters!")
    elif email.split(".")[-1] not in VALID_DOMAINS:    
        raise InvalidDomainError(f"Domain must be one of the following: .com, .bg, .org, .net")
    
    
    
    email = input()

    
# Second task from me



