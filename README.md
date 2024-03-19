# Introduction
This Software aims at optimizing custom Skyscraper layouts by bruteforcing through all possible combinations and return the most optimal layout

the software includes a User Interface which enables the user to input their own layout 

the Original Concept is based on Cracus On Github
https://github.com/Caracus/Anno1800Panorama

# Usage
For normal usage , you can run the Standalone executable from "dist\main.exe" and run it. this version calculates the best layout for sky scrapers with minimum level of 3.

For more advanced uses such as finding the best layout across all tiers you will need to edit the global variable on first line of Main.py "mintier" to your desired minimum tier. inorder to make executable file out of it you can use popular packages such as PyInstaller.

# Technicality

Skyscrapers in Anno 1800 include bonus population system called Panorama which is based on each building and their surrounding heights.
more can be read under https://anno1800.fandom.com/wiki/Skyscrapers#Panorama_Effect

# Collaboration and Issues

Any form of collaboration aiming at optimizing the approach or improving the UI is appreciated. kindly make a pull request to the "Devspace" Branch.
In case of bugs, please open an Issue ticket.

