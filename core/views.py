from django.shortcuts import render
from .csv_reader import load_persons, load_bills, load_votes, load_vote_results

def load_all_data():
    persons = load_persons('data/legislators.csv')
    bills = load_bills('data/bills.csv')
    votes = load_votes('data/votes.csv')
    vote_results = load_vote_results('data/vote_results.csv')

    return persons, bills, votes, vote_results

def get_legislator_support_opposition(persons, vote_results):
    for person in persons:
        for vote_result in vote_results:
            if vote_result.legislator_id == person.person_id:
                if vote_result.vote_type == 1:
                    person.supported_bills += 1
                elif vote_result.vote_type == 2:
                    person.opposed_bills += 1

def get_bill_support_opposition(bills, vote_results):
    for bill in bills:
        for vote_result in vote_results:
            if vote_result.vote_type == 1 and vote_result.vote_id == bill.bill_id:
                bill.supporters += 1
            elif vote_result.vote_type == 2 and vote_result.vote_id == bill.bill_id:
                bill.opposers += 1


def count_votes_for_legislator(legislator_id, vote_results):
    supported_bills = 0
    opposed_bills = 0
    for result in vote_results:
        if result.legislator_id == legislator_id:
            if result.vote_type == 1:
                supported_bills += 1
            elif result.vote_type == 2:
                opposed_bills += 1
    return supported_bills, opposed_bills


def count_votes_for_bill(bill_id, vote_results):
    supporters = 0
    opposers = 0
    for result in vote_results:
        if result.vote_id == bill_id:
            if result.vote_type == 1:
                supporters += 1
            elif result.vote_type == 2:
                opposers += 1
    return supporters, opposers


def dashboard(request):
    legislators = load_persons('data/legislators.csv')
    bills = load_bills('data/bills.csv')
    vote_results = load_vote_results('data/vote_results.csv')

    for legislator in legislators:
        legislator.supported_bills, legislator.opposed_bills = count_votes_for_legislator(legislator.legislator_id, vote_results)

    for bill in bills:
        bill.supporters, bill.opposers = count_votes_for_bill(bill.bill_id, vote_results)


    return render(request, 'core/dashboard.html', {'legislators': legislators, 'bills': bills})

