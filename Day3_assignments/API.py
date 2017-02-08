import sys
from urllib import urlopen

def get_data(url):
    array = []
    with urlopen(url) as read:
        data =  line.decode('utf-8').split()
        for i in data:
            array.append(i)
        return array

def main(url):
    data_required = get_data(url)

    print("Data required is:{}").format(data_required)        


if__name__ == '__main__':
    main
