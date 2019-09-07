text = 'Industrial Light & Magic: In this case, you find Python used in the production process for scripting complex,' \
       ' computer graphic-intensive films. Originally, IndustrialLight & Magic relied on Unix shell scripting, but it was ' \
       'found that this solution just couldn’t do the job. Python was compared to other languages, such as Tcl and Perl,' \
       ' and chosen because it’s an easier-to-learn language that the organization can implement incrementally.' \
       ' In addition, Python can be embedded within a larger software system as a scripting language, even if the system' \
       ' is written in a language such as C/C++. It turns out that Python can successfully interact with these other' \
       ' languages in situations in which some languages can’t.'
listOfWords = text.replace("\n"," ").split(' ')
for word in listOfWords:
    if word.lower().find('p') >= 0:
        print(word)
        