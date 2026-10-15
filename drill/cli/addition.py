import argparse
import time

parser = argparse.ArgumentParser()


parser.add_argument('--name', '-N',type= str, help = "name of the user")
parser.add_argument('-n','--numbers', nargs = '*', type = float, help = 'numbers to be added')
parser.add_argument('-v', '--verbosity', type = int, choices=[0, 1, 2], help = 'determines how much  detailed is displayed')
parser.add_argument('--debug', action = 'store_true', help = 'Enables debug mode')

args = parser.parse_args()


if args.debug:
    start = time.perf_counter()

print(args)
print(args.numbers)

if args.verbosity is None:
    print(args.name)
    if args.numbers is not None:
        print(sum(args.numbers))
else:
    if args.verbosity >= 0:
        print(args.name)
        if args.numbers is not None:
            print(sum(args.numbers))

    if args.verbosity >= 1:
        print(args.numbers)

    if args.verbosity == 2:
        print('Extra info')


if args.debug:
    end = time.perf_counter()
    print(end - start,'seconds')