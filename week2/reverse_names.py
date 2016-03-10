import pandas as pd

# s = pd.Series([1, 2, 3, 4, 5])
# def add_one(x):
#     return x + 1
# print s.apply(add_one)

names = pd.Series([
    'Andre Agassi',
    'Barry Bonds',
    'Christopher Columbus',
    'Daniel Defoe',
    'Emilio Estevez',
    'Fred Flintstone',
    'Greta Garbo',
    'Humbert Humbert',
    'Ivan Ilych',
    'James Joyce',
    'Keira Knightley',
    'Lois Lane',
    'Mike Myers',
    'Nick Nolte',
    'Ozzy Osbourne',
    'Pablo Picasso',
    'Quirinus Quirrell',
    'Rachael Ray',
    'Susan Sarandon',
    'Tina Turner',
    'Ugueth Urbina',
    'Vince Vaughn',
    'Woodrow Wilson',
    'Yoji Yamada',
    'Zinedine Zidane'
])
print names
def reverse_name(name):
    reversed_name= name.strip().split(" ")[1] +", " + name.strip().split(" ")[0]
    return reversed_name

print reverse_name("Christopher Columbus")

def reverse_names(names):
    '''
    Fill in this function to return a new series where each name
    in the input series has been transformed from the format
    "Firstname Lastname" to "Lastname, FirstName".

    Try to use the Pandas apply() function rather than a loop.
    '''


    return names.apply(reverse_name)

print reverse_names(names)
