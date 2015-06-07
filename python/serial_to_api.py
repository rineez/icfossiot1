import urllib2
import urllib
import serial

port = serial.Serial("/dev/ttyUSB0",9600)

while True:
    print "waiting.."
    rcv = port.readline()
    rcv = rcv.strip()
    print "going ahead: "+rcv
    if len(rcv)>0:
        if(rcv=='exit'):
          exit(0)
        else:
          query_args = { 't':rcv }
          url = 'http://192.168.2.132/api/save.php'
          data = urllib.urlencode(query_args)
          request = urllib2.Request(url, data)
          response = urllib2.urlopen(request).read()
          print response
