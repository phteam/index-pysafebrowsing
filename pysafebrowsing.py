import sys
import re
import urllib
import socket
import HTMLParser

def usage():
        print('\n\t:: [PH] Index Python Safe Browsing ::')
        print('Usage:')
        print('python pysafebrowsing.py [URL]')
        print('\nExample: $ python pysafebrowsing.py http://asianzines.blogspot.com\n')
        return


def get_result(host):
	__g_safebrowsing = 'http://google.com/safebrowsing/diagnostic?site='
        try:
	   data = str(urllib.urlopen(__g_safebrowsing + host).read())
	   result = 'Not found!'
	   if not data.find('What is the current') == -1:
	      result = data[data.find('What is the current listing status for'):]
	      result = remove_html_tags(result.replace('</blockquote>', '\n'))
	      result = result.replace('?', ':').strip().replace(':', ':\n%5s '% ('-'))

	   return result 
	except (socket.gaierror, socket.error, IOError) as e: print 'Error: ' + str(e.strerror)

def remove_html_tags(data):
	pattern = re.compile(r'<.*?>')
	return pattern.sub('', data)

if __name__ == '__main__':
   if len(sys.argv) == 2:
      h  = str(sys.argv[1])

      print '\n###### Started checking \'%s\' for safe browsing ######\n' % (h)

      results = get_result(h)
      if not results == None:
         print results
         print '\n############### GAME OVER ###############\n\n'
      else:
         print 'No results found!'
   else:
     usage()
