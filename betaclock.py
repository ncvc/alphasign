#!/usr/bin/env python

import AlphaSign

def main ():
	s = AlphaSign.Sign( '/dev/tty.PL2303-00001004' )
	s.clearMem()
	s.setClock()
	print s.getClock()
	s.sendTextPriority( AlphaSign.encodeText( '<slowest><green><7>test <red><5>message' ) , AlphaSign.MODE_ROTATE )
	return 0

if __name__ == '__main__': main()
