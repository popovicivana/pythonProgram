# coding=utf-8
print "Dobar dan, šefe! Danas radimo dnevni meni."

menu_dict = {}

while True:
    ime = raw_input("Upiši ime jela: ")
    cijena = raw_input("Izrazi cijenu u kunama: ")
    print "Bravo! Novo jelo se zove " + ime + " i košta " + cijena + " kuna."

    new = raw_input("Novo jelo je uspješno stavljeno na meni! Želiš li upisati novo jelo? (yes/no) ")

    if new == "no":
        break

menu_file = open("menu.txt", "w+")

print "Menu: "
menu_file.write("Menu:\n")
for jelo in menu_dict:
    print jelo, menu_dict[jelo]

    menu_file.write("%s: %s kn/n" % (jelo, menu_dict[jelo]))

menu_file.close()
print "END"
