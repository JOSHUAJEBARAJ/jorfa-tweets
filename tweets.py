import webbrowser
import sys
def main():
    user_input= sys.argv[1]
    webbrowser.open("https://twitter.com/search?l=&q={0}%20from%3AJofraArcher&src=typd&lang=en".format(user_input))



if __name__ == "__main__":
    main() #calling the main function