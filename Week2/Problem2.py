import argparse

parser = argparse.ArgumentParser()
parser.add_argument("text", type=str)

args = parser.parse_args()

middle = len(args.text)//2 - 1

print("The old string:", args.text)
print("Middle 3 characters:", args.text[middle:middle+3])
print("The new string:", args.text.replace(args.text[middle:middle+3], args.text[middle:middle+3].upper()))
