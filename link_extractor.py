import logging
import re
from newspaper import Article

read_file = "Formatted.txt"
write_file = "input.txt"
logging.basicConfig(filename='error.log', level=logging.INFO)

def start():
    f = open(read_file, "r")
    for line in f:
        if line == '':
            continue
        else:
            url = url_cleanup(line)
            if url == '':
                continue
            else: 
                w = open(write_file, "a")
                w.write('{}\n'.format(url))
                w.close()

def url_cleanup(url):
    url = url.strip()
    url = re.findall('http.+?(?=\s)', url)
    url = ''.join(url)
    return url

if __name__ == "__main__":
    start()
