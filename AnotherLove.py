m=24
k=11
s=8
mh=3
p=248
g=132
t=2202
kr=4
slav=0
infected_users = {
    m: "Moscow",
    k: "Kazan",
    s: "Saratov",
    mh: "Makhachkala",
    p: "Penza",
    g: "Grozny",
    t: "Tamboooov",
    kr: "Krasnodar"}


print("\nInfected Metropolitan Areas:")
for key in infected_users:
    print(key, "-", infected_users[key])


print("\nMegacities that will definitely end soon:")
for key in infected_users:
    if key > 50:
        print(key, "-", infected_users[key])

print("\nKrasnodar's Adventure:")
slav = infected_users.get(key)
print(slav*6)

s=slav*6
print("\nCut:")
print(s[9:18])