import random

# Storing random data into lists to create story.
when = ['A long time ago', 'Yesterday', 'Before you were born', 'In future', 'Before Thanos arrived']
who = ['Mollen', 'Lucy', 'Ray', 'Faith', 'Lovelace']
went = ['Akirachix', ' Moi University', 'machakos', ' Uganda', 'Joys mom']
what = ['to eat a lot of cakes', 'to futher her studies', 'to steal ice cream', 'to dance in the club with friends']

# Using string concatenition & randome.choice() to print a random element from all the lists 
print(random.choice(when) + ', ' + random.choice(who) + ' went to ' + random.choice(went) + ' ' + random.choice(what) + '.')