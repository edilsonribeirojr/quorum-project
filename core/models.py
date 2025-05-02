from tkinter.font import names

from django.db import models

class Legislator:
    def __init__(self, legislator_id, name):
        self.legislator_id = legislator_id
        self.name = name
        self.supported_bills = 0
        self.opposed_bills = 0

class Bill:
    def __init__(self, bill_id, title, primary_sponsor_id):
        self.bill_id = bill_id
        self.title = title
        self.primary_sponsor_id = primary_sponsor_id
        self.supporters = 0
        self.opposers = 0

class Vote:
    def __init__(self, vote_id, bill_id):
        self.vote_id = vote_id,
        self.bill_id = bill_id
        self.vote_result = []

class VoteResult:
    def __init__(self, vote_result_id, legislator_id, vote_id, vote_type):
        self.vote_result_id = vote_result_id
        self.legislator_id = legislator_id
        self.vote_id = vote_id
        self.vote_type = vote_type


