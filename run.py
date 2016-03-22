#!/usr/bin/env python
# coding=utf8

import sys
from lakers import app


host='127.0.0.1'
port=7000

argv = sys.argv

if len(argv) == 2:
  if ":" in argv[1]:
    args = argv[1].split(":")
    if len(args) == 2:
      host = args[0]
      port = int(args[1])
  else:
    port = int(argv[1])

elif len(argv) == 3:
  host = argv[1]
  port = int(argv[2])

else:
  host = '127.0.0.1'
  port = 7000

def show():
  mode = 'Debug' if app.debug else 'Production'
  print ('''
        __          ____          _     __         _________      _______        ______
       / /         /    \        | |   / /        / _______/     /  __   \      /  ___ \ 
      / /         /  --  \       | |__/ /        / /______      /  /  \   |    |  /___\_\ 
     / /         /  /  \  \      |  __  \       / _______/     /  /\__/__/      \____ \ 
    / /_____    /  /----\  \     | |  \  \     / /______      /  /  \  \       ______\ \ 
   /_______/   /__/------\__\    |_|   \__\   /________/     /__/    \__\      \_______/
		''')

  print ('''

##########################################################################################
                                      running in %s
                                   bind at http://%s:%s
    ''' % (mode, host, port))

if __name__ == '__main__':
    show()
    app.run(host=host, port=port)