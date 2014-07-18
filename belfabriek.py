#!/usr/bin/python

'''Script for printing Belfabriek (http://www.belfabriek.nl) availability.'''
__author__ =  'Martijn van de Rijdt'

from datetime import datetime
from xmlrpclib import ServerProxy

'''Belfabriek account code.'''
# Enter your actual Belfabriek account code here.
ACCOUNT_CODE = '12345'

'''Tuples of name and Belfabriek extension ID.'''
# Enter your actual team members' names and extension ids here.
PEOPLE = [('Alice', '01234'),
  ('Bob', '56789'),
  ('Carol', '11111')]

'''Server proxy for the Belfabriek XMLRPC API.'''
SERVER = ServerProxy("http://api1.belfabriek.nl/xml/agent/xml.asp")

'''Main function. Prints everyone's availability.'''
def main():
  print
  print 'Current time:', datetime.now()
  
  for (name, extensionId) in PEOPLE:
    print
    print 'Name:        ', name
    print 'Extension id:', extensionId

    response = SERVER.ivr.getAgentAvail({'accountCode': ACCOUNT_CODE, 'extensionId': extensionId})

    print 'Available:   ', response['available']
    print 'Reason:      ', response['availReason']
    print 'Extension:   ', response['extension']

if (__name__ == "__main__"):
    main()
