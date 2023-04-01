import whois

domain = input("Enter Domain Name: ")

while True:
    try:
        result = whois.whois(domain)
        print("This Domain Name is Unavailable")
        break
    except:
        print("This Domain Name is Available")
        break
