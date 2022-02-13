import argparse

parser = argparse.ArgumentParser()
parser.add_argument("text", type=str)
parser.add_argument("firstWord", type=str)
parser.add_argument("secondWord", type=str)

args = parser.parse_args()

print("The given text: ", args.text)
print("First word: ", args.firstWord)
print("Second word", args.secondWord)

if args.firstWord in args.text:
    print("Output string: ", args.text.replace(args.firstWord, args.secondWord, args.text.count(args.firstWord)))