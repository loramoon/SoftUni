class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


email = input()
domains = ['com', 'bg', 'net', 'org']

while email != "End":
    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")
    name = email.split('@')
    if len(name[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    domain = name[1].split('.')
    if domain[1] not in domains:
        raise InvalidDomainError("Domain must be one of the following: ." + ', .'.join(domains))

    print("Email is valid")

    email = input()
