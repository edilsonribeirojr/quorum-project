from django.shortcuts import render
from csv_reader import load_persons, load_bills, load_votes, load_vote_results

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

def dashboard(request):
    persons, bills, votes, vote_results = load_all_data()
    get_legislator_support_opposition(persons, vote_results)
    get_bill_support_opposition(bills, vote_results)

    return render(request, 'core/dashboard.html', {'persons': persons, 'bills': bills})
