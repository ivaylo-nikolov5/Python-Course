test = {}

def add_name_age(**kwargs):
    for name, age in kwargs.items():
        test[name] = age


add_name_age(Ivaylo=17, Emin=16)
print(test)