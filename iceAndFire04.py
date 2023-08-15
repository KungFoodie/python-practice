#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"
AOIF_BOOKS = "https://www.anapioficeandfire.com/api/books/"
AOIF_HOUSES = "https://www.anapioficeandfire.com/api/houses/"


def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)
        print("\nHouses: ")
        for allegiance in got_dj['allegiances']:
            print(requests.get(allegiance).json().get('name') + " ")
        print("\nBooks: ")
        for book in got_dj['books']:
            print(requests.get(book).json().get('name') + " ")

if __name__ == "__main__":
        main()