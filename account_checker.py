import colorama
import argparse
import requests
import time

def check_username(usernames):
    unregistered = 0
    time_string = time.strftime("%H_%M_%S")
    output = open(time_string + '.txt', 'a+')
    output.truncate()
    output.write('UNREGISTERED NAMES:\n')
    for user in usernames:
        url = 'https://pokemonshowdown.com/users/{}.json'.format(user)
        data = requests.get(url)
        parsed_data = data.json()
        if parsed_data['registertime'] == 0:
            print(colorama.Fore.GREEN + user)
            unregistered += 1
            temp = '{}\n'.format(user)
            output.write(temp)

    output.close()
    count = len(usernames)
    print(colorama.Fore.YELLOW + 'Done. {}/{} unregistered, {}%'.format(count,count, (unregistered / count) * 100))
    print(colorama.Style.RESET_ALL)


def start():
    colorama.init()
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--input", help="Text file as input")
    arg = parser.parse_args()

    with open(arg.input) as input_file:
        usernames = input_file.read().splitlines()
        check_username(usernames)

if __name__ == '__main__':
    start()
