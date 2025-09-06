# Chaos Gacha

Welcome to your very own slice of the infinite chaos of the multiverse.

## Over a Thousand Entries

The current iteration of the Chaos Gacha features:

- Around 80,000 words of pure handwritten descriptions
- Over 1,900 Unique Entries
- Freely adjustable odds
- Customizable Gacha Entries
- And much more!

## Usage

If all you want is to start rolling, you can do so immediately by using the website located [here](https://www.chaosgacha.com/). Alternatively, for those of you that are a little more tech-savvy, you can download this repository and run ```build.bat``` to automatically generate an executable. This script requires [PyInstaller](https://pyinstaller.org/en/stable/).

Feel free to use it however you like. Add your own entries, make your own list from scratch, or just use the interface as-is. You are free to use it on your own works and project. If you are going to use it to publish a story, then BronzDeck would appreciate it if you would link back to the Chaos Gacha and maybe mention him by name or link one of his profiles (linked below).

### Verify Data

[verify.py](https://github.com/nekofuu/ChaosGacha/blob/master/verify.py) can be used to verify the formatting of the data to ensure that it can be properly parsed for the gacha. As long as you have python installed, this script requires no additional dependencies and can be immediately ran through the command ```py Verify.py```.

This script assumes the data files are saved as ```.txt``` files and are saved in a ```gachafiles``` folder within the directory that the script is called from. Otherwise it will read all text files present, no matter what their names.

### Convert the Data To and From a Spreadsheet

[Gacha Utility](https://github.com/nekofuu/ChaosGacha/blob/master/Gacha_Utility.py) is a script included in this repository that is used to either read the text files from a provided directory and convert them to an excel file (```.xlsx``` file) or take a provided excel file and convert it back into text files. This is useful because the gacha requires the data to be presented in the text file format, but the data is easier to work with in a spreadsheet. This should also help eliminate accidental formatting errors.

```Gacha_Utility.py``` has two additional dependencies: ```pandas``` and ```openpyxl```. In order to run the script, you will need to install these dependencies using the command ```pip install pandas openpyxl```, then you can run the script with the command ```py Gacha_Utility.py```.

If you are going to use the utility script, then it is recommended that you backup the text files. The preferred method of doing so would be using a version control software like git to track changes to them. If you do use a version control solution, it is recommened that you either save the *.xlsx file to a different directory from your repository or add xlsx files to your .gitignore. As long as the .txt files are backed up, you can always rebuild the spreadsheet using the utility script in the event that something happens to it.

## Acknowledgements

The Chaos Gacha was [originally created by BronzDeck](https://github.com/Bronzdeck/ChaosGacha). He has continued to add additional content to the gacha list since release with the help of members of the community.

BronzDeck can be found on [Ao3](https://archiveofourown.org/users/Bronz_Deck/pseuds/Bronz_Deck), [Questionable Questing](https://forum.questionablequesting.com/members/bronz.127219/), or [Webnovel](https://www.webnovel.com/profile/4311349979). You can also support him by becoming a member on [Patreon](https://patreon.com/BronzDeck)