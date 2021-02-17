#!/usr/bin/python3

# Imports
import vobject
import sys, getopt

def main(argv):
    inputfile = ''
    
    #Exit if no parameters are provided
    if len(argv) == 0:
        print('simple_contract_trimmer.py -i <inputfile>')
        sys.exit()
    
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print('simple_contract_trimmer.py -i <inputfile>')
        sys.exit(2)

    #Exit if anything other than the input file is provided
    for opt, arg in opts:
        if opt in ("-i", "--ifile"):
            inputfile = arg
        else:
            print('Useage: simple_contract_trimmer.py -i <inputfile>')
            sys.exit()
    try:
        contacts = open(inputfile, "r")
    except IOError as e:
        print(e)

    final_contact = open("modified_contact.vcf", "w", newline="")

    # Writes all entries with the 'tel' attribute to a new .vcf file
    vcard = vobject.readComponents(contacts.read())
    for entry in vcard:
        if hasattr(entry, 'tel'):
            final_contact.write(entry.serialize())

if __name__ == "__main__":
        main(sys.argv[1:])