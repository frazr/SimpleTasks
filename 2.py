import re
import urllib2

def cmp_fnd(pattern, data):
    p = re.compile(pattern)
    m = p.findall(data)
    return m

def hrefs(data):
    return cmp_fnd('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', data)

def anchors(data):
    return cmp_fnd('<a href="(?!\/)(?!#)?\'?([^"\'>]*)', data)

def parse_url():
    response = urllib2.urlopen(url).read()

    if action == 1:
        print anchors(response)
    elif action == 2:
        print hrefs(response)


if __name__ == '__main__':
    print '1: Get anchor href attributes\n'
    print '2: Get all href attributes\n'
    action = int(raw_input('Choose action:'))
    url = raw_input('Paste url:')
    parse_url()
