print("Welcome to my Quiz")

x = input("Do you Wanna Play (Yes/No): ")

# for X
if x == "Yes" or x == "yes":
    print("Let's Start it!")
elif x == "No" or x == "no":
    quit()
else:
    quit()

# Quiz 1
y = input("Pada tahun berapakah Indonesia Merdeka? ")
if y == "1945":
    print("benar!")
else:
    print("Salah!")
    quit()

#Quiz 2
y = input("Pada tahun berapakah Valorant Rilis? ")
if y == "2020":
    print("benar!")
else:
    print("Salah!")
    quit()

#Quiz 3
y = input("Berapa hasil dari 5+5? ")
if y == "10":
    print("benar!")
else:
    print("Salah!")
    quit()

print("Selamat Anda Berhasil Menjawab semuanya")