import logging
import re
from newspaper import Article

read_file = "input.txt"
write_file = "output.txt"
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
            page = page_call(url)
            if page == '':
                continue
            else:
                title = page.title
                w = open(write_file, "a")
                w.write('[{}]({})  \n'.format(title, url))
                w.close

def url_cleanup(url):
    url = url.strip()
    url = re.sub('\?(?!(id=)|(q=)).*', '', url)
    url = re.sub('(amp\/$)|(amp$)', '/', url)
    url = re.sub('\/tnamp\/$', '/', url)
    url = re.sub('\/amp.cnn.com\/cnn\/', '/cnn.com/', url)
    url = re.sub('\/amp.theguardian.com\/','/theguardian.com/', url)
    url = re.sub('theverge.com\/platform\/amp\/','theverge.com/', url)
    url = re.sub('vice.com\/amp\/', 'vice.com/', url)
    url = re.sub('\/m.', '/', url)
    url = re.sub('\/mobile.', '/', url)
    lookup = '\/amp'
    if re.search(lookup, url):
        logging.info("AMP link found in {}\n".format(url))
        url = ''
    return url

def page_call(url):
    try:
        call = Article(url)
        call.download()
        call.parse()
    except Exception as e:
        logging.error("{}\n".format(e))
        call = ''
        return call
    else:
        return call

if __name__ == "__main__":
    start()
