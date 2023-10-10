## Overview
Python CLI script to extract the file IDs/names of soundsets in Owlcat's Pathfinder cRPGs: Kingmaker and Wrath of the Righteous. This tool is useful if you want to make a new voice pack or replace an existing character's voice pack.

## Requirements
Python 3.x

This file depends on an XML file (SoundbanksInfo.xml) located in the game data, which cannot be included in this repository as it belongs to Owlcat.

For Kingmaker, that file is located in

`<GAMEDIRECTORY>/Kingmaker_Data/StreamingAssets/Audio/GeneratedSoundbanks/Windows`

For Wrath of the Righteous, the file is here:

`<GAMEDIRECTORY>/Wrath_Data/StreamingAssets/Audio/GeneratedSoundbanks/Windows`

The file needs to be in the same directory as SoundbanksInfo.xml, so drop this script's `soundbank-extract.py` file into that directory or create a copy of SoundbanksInfo.xml in this script's directory.

No changes are made to the XML file so it will not make any changes to your game data; it only reads the file to copy the data.

## Usage
`python soundbank-extract.py --game [GAME] --search [SEARCHTERM] [--output FILENAME]`

Examples:

To extract all of Seelah's voice lines in Wrath of the Righteous:

`python soundbank-extract.py --game Wrath --search Seelah`

To extract all of Jaethal's voice lines in Kingmaker:

`python soundbank-extract.py --game Kingmaker --search Jaethal`

These commands will create a CSV file with the names of the WEM audio files and their descriptions/labels.

Optionally, you can specify a custom filename, as such:

`python soundbank-extract.py --game Kingmaker --search Jaethal --output myfilename.csv`

The `--search` argument is case-insensitive.


