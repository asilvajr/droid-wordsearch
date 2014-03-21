droid-wordsearch
================

The idea is using an OCR, tesseract-ocr, find all the words in a word search. I have lazy friend who hates doing WordSearches. 

Protoype is a python based, nothing related to the actual droid app. Python script will read a wordsearch grid from text and search for words against dictionary words
- this is to help create a simple, effecient algorithm to doing this effeciently.
- Boyer-Moore Algorithm would be best for this. 
- 4 different grids will be created.
-- Horizontal (Original Grid)
-- Vertical
-- Diagonal-Left
-- Diagonal-Right
-Runtime: Dictionary has 171,476 = w words according to oxford 20th edition. Boyer-Moore is O(nm) x 4 x w.



-My next step will be the app creation. Java based. We, or I, am still far from begining this as of 3/21/2013 [Repo creation date]

