users = {}
names = ['AB','CD','EF','GH','KL']
jobs = ['JB1','JB2','JB3','JB4','JB5']
ages = [20,21,22,23,24]
for k in range(5):
    users[k] = {'username':names[k],'age':ages[k],'job':jobs[k]}

for m in users.values():
    for j,h in m.items():
        print(j,' => ',h)
    print('\n')