#!/usr/local/bin/python

import sys


from moonlander import Moonlander


def main():
    the_moonlander = Moonlander()
    while the_moonlander.test() == 'in_air':
        the_moonlander.update()
        the_moonlander.output()
    print('We are no longer in the air... Final stats to follow.')
    the_moonlander.output()
    return


if __name__ == '__main__':
    sys.exit(main())
