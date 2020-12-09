
import time, sys, os
from pygame import mixer

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

mixer.init()
mixer.music.load(str(os.getcwd())+str("/Pay Phone.mp3"))
mixer.music.play()

menu_resp = 0

while menu_resp != 3:
    print("\n1 => Encode\n2 => Decode\n3 => Exit")
    menu_resp = int(input("\nSelect and option => "))

    if menu_resp == 1:
        cypher_string = str("")
        plain_text = str(input("\nType message: "))

        for i in range(len(plain_text)):
            cypher_string = cypher_string + chr(ord(plain_text[i])+1)
        
        print("\nSecret_K message: ",cypher_string)

    elif menu_resp == 2:
        cypher_string = str(input("\nSecret_K message: "))
        plain_text = str("")

        for i in range(len(cypher_string)):
            plain_text = plain_text + chr(ord(cypher_string[i])-1)

        print("\nOriginal message: ",plain_text)

    elif menu_resp == 3:
        print("\nExiting. Food for thought, what if Area51 is just a cover and the real things happen at Area52?")
        time.sleep(7)
        sys.exit()
        