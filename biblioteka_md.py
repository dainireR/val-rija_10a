import pyjokes

print(pyjokes.get_joke())

import pyfiglet
vards=pyfiglet.figlet_format("Valērija", font="Comic Sans MS")
print(vards)

import cowsay

cowsay.cow(pyjokes.get_joke())
 

 print(cowsay.get_output_string('cow', pyjokes.get_joke()))
