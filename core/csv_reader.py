import csv
from .models import Legislator, Bill, Vote, VoteResult

def load_persons(file_path):
    persons = []
    with open(file_path, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            person = Legislator(int(row['id']), row['name'])
            persons.append(person)
    return persons


def load_bills(file_path):
    bills = []
    with open(file_path, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            bill = Bill(int(row['id']), row['title'], int(row['sponsor_id']))
            bills.append(bill)
    return bills


def load_votes(file_path):
    votes = []
    with open(file_path, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            vote = Vote(int(row['id']), int(row['bill_id']))
            votes.append(vote)
    return votes


def load_vote_results(file_path):
    vote_results = []
    with open(file_path, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            vote_result = VoteResult(
                int(row['id']),
                int(row['legislator_id']),
                int(row['vote_id']),
                int(row['vote_type'])  # 1 for yea, 2 for nay
            )
            vote_results.append(vote_result)
    return vote_results