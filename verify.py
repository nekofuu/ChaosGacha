#########################################################
# 
# This file is used to verify the original text files
# to ensure that every entry is formatted properly
# using the legacy data format.
#
#########################################################
import os
import re

SOURCE_DIR = "gachafiles" # The source for the upstream files

def Verify(filename):
    path = os.path.join(SOURCE_DIR, filename)
    with open(path, 'r') as file:
        prevLine = ""
        for index, line in enumerate(file):
            line = line.rstrip()
            numberPrefix = r'^(\d+)\.\s*'
            poundPrefix = r'^(#\s*)'

            headingLine = re.match(numberPrefix, line)
            descriptionLine = re.match(poundPrefix, line)

            assumedDescription = False
            if index != 0:
                # Check if the last line was a heading line
                assumedDescription = re.match(numberPrefix, prevLine)

            if headingLine:
                # Check if the line has correct formatting
                formatting = r'^(\d+\.\s*.*,\s*\d\.*\d*)$'
                match = re.match(formatting, line)
                if not match:
                    print(f"Entry '{line}' is not formatted correctly.\n")

                trailingPeriod = r'^\d+(\.\s*)' # Guaranteed to have it if it got here

                # Check if the rest of the line is formatted correctly
                parts = re.sub(numberPrefix, '', line).strip().split(',')
                if len(parts) != 2:
                    # Each entry should be formatted as Name,Rarity
                    # If it isn't, then it won't work for the gacha even
                    # if it has the required number prefix
                    print(f"Entry '{line}' has {len(parts)} parts instead of the expected 2.\n")

            elif descriptionLine or assumedDescription:
                if not descriptionLine:
                    # Doesn't seem like the description line needs the # prefix, so commenting this out
                    #print(f"No pound prefix found in expected description of {prevLine}.\n")
                    pass
            else:
                # Error detected
                print(f"Line '{line}' is not formatted as either a heading or description line.\n")
            
            prevLine = line

for file in os.listdir(SOURCE_DIR):
    print(f"{file} found\n")
    if file.endswith(".txt"):
        Verify(file)
    print(os.linesep)