# Simple Contract Trimmer

This is a simple Python script that uses the vobject library to trim out contacts without phone numbers listed in a .vcf file.

Google tends to include many contacts without phone numbers when mass exporting the data from a Google account. In order to simplify
the contacts that are exported, this script parses the .vcf file, pulls out the contacts with phone numbers, and serializes it in a 
new .vcf file.
