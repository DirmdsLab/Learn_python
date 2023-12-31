ThisGlobalVal = "Hmph"

def LocalFucn():
    print(ThisGlobalVal)

LocalFucn()

def LocalHavaVal():
    ThisGlobalVal = "Hmm"
    print(ThisGlobalVal)

LocalHavaVal()

print("Hasil :",ThisGlobalVal)