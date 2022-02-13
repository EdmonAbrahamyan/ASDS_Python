import datetime
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--days", type=int, default=0)
parser.add_argument("--years", type=int, default=0)

args = parser.parse_args()

today = datetime.date.today()
print("Current date:", today)

years = 0
days = 0

if args.years:
    print("Given years:", args.years)
    years = datetime.timedelta(days=args.year * 365)
else:
    print("Given years: not given")

if args.days:
    print("Given days:", args.days)
    days = datetime.timedelta(days=args.days)
else:
    print("Given days: not given")

print("Final date:", today + years + days)