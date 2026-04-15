from __init__ import CONN , CURSOR


# this is the sql script or customer.py


class Customer:
    cache = {} # table is the source of truth
    #
    #this createwd
    def __init__(self ,name , age , gmail , phone_number , created_at , id=None):
        self.id = id 
        self.name = name 
        self.age = age 
        self.gmail = gmail
        self.phone_number = phone_number
        self.created_at = created_at