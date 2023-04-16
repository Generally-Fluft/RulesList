This is a modified version of the OneRuleToRuleThemAll wordlist. I took out all of the rules that would alter the order or spelling of the words so it might not even work!
Basically, it's the relevat parts of OneRule, with 4 digits appended to the end.

In JohnTheRipper, there is a preproc system for rules lists which allows the file to be significantly shortened.

In Hashcat, as far as I can tell, there is no such system, which means each number needs to be seperately written, resulting in something like 59 million lines.
If you download both the OneRuleModifiedHashcatTemplate file and the corresponding Python script to the same directory, then run the python script, it will output the 
output the Template file and write all 59 million lines to OneRuleModifiedHashcat.rule
