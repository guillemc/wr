# wr
Translate words from [Wordreference](http://www.wordreference.com/) through the command line. 

#### Requirements:
- Python 3
- [requests](https://pypi.python.org/pypi/requests)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)

#### Installation:

Make the script executable and place it under your path, for example:

    chmod a+x wr.py
    mv wr.py ~/bin/wr
  

#### Usage:

    wr <frto> <word>
  
Where *frto* corresponds to the language codes to translate *from* and *to*, and *word* is the word to translate.


#### Examples:

    ~$ wr fren flâneur
    flâneur (promeneur)
        stroller 
        loafer 
    
    flâneur (promeneur)
        wandering

-----

    ~$ wr fres désormais
    désormais (dorénavant)
        a partir de ahora 
        en adelante, de ahora en adelante 
        de aquí en adelante
  
  
