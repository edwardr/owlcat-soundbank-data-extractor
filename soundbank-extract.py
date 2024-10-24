#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import csv, argparse, time

def run_kingmaker(search):
    tree = ET.parse("SoundbanksInfo.xml")
    root = tree.getroot()
    rows = []
    for file in root.findall(".//StreamedFiles/*"):
        id = file.get("Id")
        short_name = file.find("ShortName").text.lower()
        if search.lower() in short_name:
            row = []
            row.append(id)
            row.append(short_name)
            rows.append(row)
    return rows

# this method is no longer used as they 
# reverted the Wrath file to use the Kingmaker structure
def run_wrath(search):
    tree = ET.parse("SoundbanksInfo.xml")
    root = tree.getroot()
    rows = []
    for soundbank in root.findall(".//SoundBanks/*"):
        short_name = soundbank.find("ShortName").text.lower()
        if search.lower() in short_name:
            if soundbank.find("IncludedMemoryFiles"):
                for memfile in soundbank.find("IncludedMemoryFiles"):
                    id = memfile.get("Id")
                    raw = memfile.find("ShortName").text
                    row = []
                    row.append(id)
                    row.append(raw)
                    rows.append(row)

    return rows

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--g", "--game", help="Kingmaker or Wrath")
    parser.add_argument("--s", "--search", help="Case-insensitive search term")
    parser.add_argument("--o", "--output", help="Optional custom output filename")
    args = parser.parse_args()
    if args.g is None:
        exit("Error: Game not specified")

    headings = ['Audio Filename', 'Label']

    if args.g == "Kingmaker":
        data = run_kingmaker(args.s)
    elif args.g == "Wrath":
        data = run_kingmaker(args.s)
    else:
        exit("Error: Invalid game.") 

    if len(data) == 0:
        exit("No matching data found")
    else:
        print("Generating CSV with " + str(len(data)) + " rows")
    
    if args.o is None:
        filename = args.g + "-" + args.s + "-export-" + str(time.time()) + ".csv"
    else:
        filename = args.o
              
    with open(filename, 'w') as csvfile:  
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerow(headings)  
        csvwriter.writerows(data)

if __name__ == "__main__":
  main()