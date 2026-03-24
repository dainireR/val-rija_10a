import pyjokes
joks=pyjokes.get_joke()
print(joks)

import pyfiglet
vards=pyfiglet.figlet_format("Valērija", font="Comic Sans MS")
print(vards)

import cowsay

cowsay.cow(pyjokes.get_joke())

print(cowsay.get_output_string('cow', pyjokes.get_joke()))


#4.uzd

#pārveido ievadīto joku ar pyfiglet līdzīgi kā 6.rindā, tikai vārda vietā ieraksti joks

##pārveido 18.rindas mainīgo, kuru pārveidoji ar pyfiglet, ar cow say.  var arī 1 rindā
