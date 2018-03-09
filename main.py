import ptvsd
from fstrings import f 
from time import sleep

ptvsd.enable_attach("my_secret", address=('0.0.0.0', 3000))


def main():
    
    #this will block execution until a debugger attaches
    #ptvsd.wait_for_attach()

    i = 1

    while True:
        sleep(1)
        i = i+1
        print(f('looped:{i}'))


if __name__ == "__main__":
    main()
