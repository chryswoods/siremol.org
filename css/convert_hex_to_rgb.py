__author__ = 'Antonia Mey'
__email__ = 'antonia.mey@ed.ac.uk'

#Imports
import struct
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--hexvalues", help="list of hexvalues to be converted to rgb",
                        nargs='+')
    args = parser.parse_args()
    hexlist = ['00A08A', '34D0BA', '29497F', '6A92D4', '25D500', 'FF6A00','3DA028', 'FF8F40', '00733E']
    if args.hexvalues != None:
        hexlist = args.hexvalues
    print "List of to be converted hex values is %s" %hexlist
    rgblist = []
    for i in hexlist:
        rgblist.append(struct.unpack('BBB',i.decode('hex')))
    print "RGBs of the inpute hexvalues are:"
    if len(rgblist) == 1:
        print '( %s );' %str(rgblist[0])
    else:
        count = 0
        for i in rgblist:
            if count == 0:
                print '( %s,' %str(i)
            elif count == len(rgblist)-1:
                print ('( %s );'%str(i))
            else:
                print '( %s,' %str(i)
            count = count+1
