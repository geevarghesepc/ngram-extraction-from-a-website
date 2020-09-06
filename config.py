

class Config:

    remove_stop_words = True
    replace_html_entities = True
    replace_x_codes = True
    replace_umlaut = True

    stop_words = ["A", "ABOUT", "ABOVE", "ACCORDINGLY", "ACROSS", "AFTER", "THINK", "ALONG", "ALSO", "ALTHOUGH", "AM",
               "AMONG", "AN", "AND", "ANOTHER", "ANY", "ANYBODY", "ANYBODYS", "ANYMORE", "ANYONE", "ANYTHING",
               "ANYTIME", "ANYWAY", "ANYWHERE", "ARE", "AROUND", "AS", "ASSUMING", "AT", "BE", "BECAUSE", "BEEN",
               "BEFORE", "BEHIND", "BEING", "BESIDES", "BEST", "BETWEEN", "BEYOND", "BLOGGER", "BLOGGERS", "BUT", "BY",
               "CAN", "CASE", "CONCERNING", "CONSEQUENTLY", "CONVERSELY", "COULD", "DARE", "DESPITE", "DID", "DO",
               "DOES", "DOWN", "DURING", "ENOUGH", "EVEN", "EVER", "EVERY", "EVERYBODY", "EVERYBODYS", "EVERYDAY",
               "EVERYONE", "EVERYTHING", "EVERYWHERE", "EXCEPT", "FOLLOWING", "FOR", "FROM", "FURTHERMORE", "HAD",
               "HAS", "HAVE", "HAVING", "HE", "HENCE", "HIM", "HIS", "HOW", "HOWEVER", "IF", "IN", "INCLUDE",
               "INCLUDING", "INSTEAD", "INTO", "IS", "IT", "ITSELF", "JUST", "LEST", "LET", "LIKE", "LIKEWISE", "LONG",
               "MAY", "MAYBE", "ME", "MEANWHILE", "MIGHT", "MORE", "MOREOVER", "MUCH", "MUST", "NEAR", "NEED",
               "NEVERTHELESS", "NONETHELESS", "NOR", "NOW", "OF", "OFF", "ON", "ONCE", "ONETIME", "ONGOING", "ONHIS",
               "ONLY", "ONTHE", "OR", "ORDER", "OTHERWISE", "OUGHT", "OUR", "OURSELF", "OUT", "OVER", "PLUS",
               "PROVIDED", "RATHER", "SAID", "SAY", "SAYS", "SHALL", "SHE", "SHOULD", "SINCE", "SO", "SOME", "SOMEBODY",
               "SOMEHOW", "SOMEONE", "SOMEONES", "SOMEPLACE", "SOMETHING", "SOMETIME", "SOMETIMES", "SOMEWHAT",
               "SOMEWHERE", "SOON", "STILL", "SUCH", "THAN", "THAT", "THATS", "THE", "THEIR", "THEIRS", "THEM", "THEN",
               "THERE", "THEREABOUT", "THEREAFTER", "THEREBY", "THEREFORE", "THESE", "THEY", "THEYD", "THEYLL",
               "THEYRE", "THEYVE", "THIS", "THOSE", "THOUGH", "THROUGH", "THROUGHOUT", "THUS", "TILL", "TIME", "TO",
               "TOO", "TOWARD", "TOWARDS", "UNDER", "UNLESS", "UNTIL", "UP", "UPON", "VERY", "WANT", "WANTS", "WAS",
               "WE", "WENT", "WERE", "WHAT", "WHATEVER", "WHATIS", "WHEN", "WHENEVER", "WHERE", "WHEREAS", "WHEREVER",
               "WHETHER", "WHICH", "WHICHEVER", "WHILE", "WHO", "WHOEVER", "WHOLE", "WHOM", "WHOMEVER", "WHOSE", "WHY",
               "WILL", "WITH", "WITHIN", "WITHOUT", "WOULD", "YET", "YOU", "YOUR", "YOURS", "YOURSELF", "THINKS", "ALL",
               "BOTH", "EACH", "EITHER", "FEW", "HER", "HERS", "HERSELF", "HIMSELF", "I", "MANY", "MINE", "MOST", "MY",
               "MYSELF", "NEITHER", "NOBODY", "NONE", "NOTHING", "ONE", "OTHER", "OTHERS", "OURS", "OURSELVES",
               "SEVERAL", "THEE", "THEMSELVES", "THINE", "THOU", "YOURSELVES"]

    html_entities = {"\t": " ", "\n": " ", u'\xa0': u' ', u'\x03': u' ', u"\u200A": u' ', u"\u201A": u"'",
                     u"\u201B": u"'", u"\u201C": u'"', u"\u201D": u'"', u"\u202A": u' ', u"\u202C": u' ',
                     u"\u200E": u' ', u"\u200B": u' ', u"\x80": u" ", u"\x81": u" ", u"\x82": u" ", u"\x83": u" ",
                     u"\x84": u" ", u"\x85": u" ", u"\x86": u" ", u"\x87": u" ", u"\x88": u" ", u"\x89": u" ",
                     u"\x8a": u" ", u"\x8b": u" ", u"\x8c": u" ", u"\x8d": u" ", u"\x8f": u" ", u"\x90": u"-",
                     u"\x91": u"-", u"\x92": u"-", u"\x93": u"-", u"\x94": u"-", u"\x95": u"-", u'\x97': u"-",
                     u'\xad': u'-', u"\x98": u"'", u"\x99": u"'", u"\x9a": u"'", u"\x9b": u"'", u"\x9c": u'"',
                     u"\x9d": u'"', u"\x9e": u'"', u"\x9f": u'"', u"\xa1": u" ", u"\xa2": u" ", u"\xa3": u" ",
                     u"\xa4": u" ", u"\xa5": u" ", u"\uFEFF": u"", u"\u2018": u"'", u"\u2019": u"'"}

    umlaut = {"Ã": "A", "Á": "A", "Â": "A", "À": "A", "Ä": "A", "Å": "A", "Ā": "A", "Ă": "A", "Æ": "A",
                      "Ć": "C", "Ç": "C", "Č": "C", "È": "E", "É": "E", "Ē": "E", "Ê": "E", "Ë": "E", "Ĕ": "E",
                      "Ì": "I", "Í": "I", "Î": "I", "Ï": "I", "Ĭ": "I", "Ð": "D", "Ł": "L", "Ñ": "N", "Ò": "O",
                      "Ó": "O", "Ô": "O", "Õ": "O", "Ö": "O", "Ő": "O", "Š": "S", "Ù": "U", "Ú": "U", "Û": "U",
                      "Ü": "U", "Ű": "U", "Ý": "Y", "ã": "a", "á": "a", "â": "a", "à": "a", "ä": "a", "å": "a",
                      "ā": "a", "ă": "a", "æ": "a", "ć": "c", "ç": "c", "č": "c", "è": "e", "é": "e", "ē": "e",
                      "ê": "e", "ë": "e", "ĕ": "e", "ì": "i", "í": "i", "î": "i", "ï": "i", "ĭ": "i", "ð": "d",
                      "ł": "l", "ñ": "n", "ò": "o", "ó": "o", "ô": "o", "õ": "o", "ö": "o", "ő": "o", "š": "s",
                      "ù": "u", "ú": "u", "û": "u", "ü": "u", "ű": "u", "ý": "y"}

    x_codes = {'\xe2\x80\x99': "'", '\xe2\x80\x9c': '"', '\xe2\x80\x9d': '"', '\xe2\x80\x9e': '"', '\xe2\x80\x9f': '"',
               '\xc3\xa9': 'e', '\xe2\x80\x93': '-', '\xe2\x80\x92': '-', '\xe2\x80\x94': '-', '\xe2\x80\x98': "'",
               '\xe2\x80\x9b': "'", '\xe2\x80\x90': '-', '\xe2\x80\x91': '-', '\xe2\x80\xb2': "'", '\xe2\x80\xb3': "'",
               '\xe2\x80\xb4': "'", '\xe2\x80\xb5': "'", '\xe2\x80\xb6': "'", '\xe2\x80\xb7': "'", '\xe2\x81\xba': "+",
               '\xe2\x81\xbb': "-", '\xe2\x81\xbc': "=", '\xe2\x81\xbd': "(", '\xe2\x81\xbe': ")"}


