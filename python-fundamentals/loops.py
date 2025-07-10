favorites = ['creme brule', 'chocolate', 'vanilla', 'strawberry', 'pistachio',  'mint chocolate chip']

for item in favorites:
    print("I like this dessert", item) 


count = 0

while count <len(favorites):
    print("I like this dessert", favorites[count])
    count += 1


for idx, item in enumerate(favorites):
    print(idx, item)