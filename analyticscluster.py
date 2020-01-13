#
#
#
# Name:			analyticscluster.py
# Author:		Julio Carranza
# Date/Version:	2020-01-11/0.1
#
# Description:	show, create, modify, delete, analytic cluster information using APIs
#
#

import yaml,argparse
from jcVDmodule import analyticscluster
from getpass import getpass

#parsing argument to the program
parser = argparse.ArgumentParser(description=
	'script to show, create, modify, delete, analytic cluster information using APIs')
parser.add_argument('VD',
    help='Versa Director IP address' )
parser.add_argument('user',
    help='user used to login to director' )
parser.add_argument('-y',
    action="store",
    dest="ymlfile",
    help='yml file with analytics cluster variables' )
parser.add_argument('-s',
    action='store_true',
    help='shows analytics cluster information' )
parser.add_argument('-m',
    action='store_true',
    help='modify analytics cluster' )
parser.add_argument('-c',
    action='store_true',
    help='create analytics cluster')
parser.add_argument('-d',
    action='store_true',
    help='delete analytics cluster')

args = parser.parse_args()



ac = analyticscluster()
passwd=getpass()

if args.s:
    ac.show(args.VD, args.user, passwd)
elif (args.ymlfile):
    with open(args.ymlfile, 'r') as stream:
        out = yaml.load(stream, Loader=yaml.FullLoader)
    for i in out['ac']:
        data =  '{"analytics-cluster": [{"name": "' + i['name'] + '", "log-collector-config": {"port": "' + \
                i['collectorport'] + '", "ip-address": ["' + i['collectorip'] + \
                '"]}, "connector-config": {"port": "'+i['northboundport'] + \
                '", "web-addresses": [{"name": "nb", "ip-address": "' + i['northboundip'] + '"}]}}]}'
        if args.c:
            ac.create(args.VD, args.user, passwd, data)
        elif args.m:
            ac.modify(args.VD, args.user, passwd, data, i['name'])
        elif args.d:
            ac.delete(args.VD, args.user, passwd, i['name'])
        else:
            print("please specify operation --s, --c, --d, --m")
else:
    print("For help, type python3 analyticscluster.py --help")
















		

