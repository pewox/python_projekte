#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) > 1:
        gruss = sys.argv[1]
        print(f'Schönen guten {gruss}')
    else:
        sys.exit()

if __name__ == '__main__':
    main()
    print([i for i in sys.argv])
