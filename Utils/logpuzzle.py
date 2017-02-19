#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import operator

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def print_duplicates(dict_elem):
	if dict_elem[1] > 1:
		print dict_elem[0]

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""

  url_dict = {}
  
  ufile = urllib.urlopen(filename)
  lines = ufile.readlines()

  for line in lines:
  	match = re.search(r'GET\s(\S+puzzle\S+)\sHTTP', line)
  	if match:
  		complete_url = filename+match.group(1)
  		if complete_url not in url_dict:
  			url_dict[complete_url] = 0
  		url_dict[complete_url] += 1

  map(print_duplicates, url_dict.items())

  elems = sorted(url_dict.keys(), key=operator.itemgetter(0))
  return elems
 

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  if not os.path.exists(dest_dir):
  	os.mkdir(dest_dir)

  print 'Retrieving...'
  basename = 'img'

  for i in range(len(img_urls)):
    name = basename+str(i)
    #urllib.urlretrieve(img_urls[i], dest_dir+'\\'+name)

  htmlfile = open(dest_dir+'\\index.html', 'w')
  if htmlfile:
  	htmlfile.write('<verbatim>\n<html>\n<body>\n')
  	for i in range(len(img_urls)):
  	  name = basename+str(i)
  	  htmlfile.write('<img src="'+dest_dir+'\\'+name+'">')
  	htmlfile.write('\n</body>\n</html>')
  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
