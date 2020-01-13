#
#
#
# Name:			jcVDmodule.py
# Author:		Julio Carranza
# Date/Version:	2020-01-10/0.1
#
# Description:	Python modules to support VD automation
#
#
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



class analyticscluster():
    PORT = '9182'
    URL_FORMAT = 'https://%s:%s/api/config/nms/provider'
    def create(self, vd, user, password, data):
        URL = self.URL_FORMAT % (vd, self.PORT)
        print(URL, data)
        r = requests.post(URL, auth=(user, password),
                      headers={"Content-Type": "application/json", "Accept": "application/json"}, data=data,
                      verify=False)
        print (r)

    def modify(self, vd, user, password, data, clustername):
        URL = self.URL_FORMAT % (vd, self.PORT) + '/analytics-cluster/' + clustername
        print(URL, data)
        r = requests.put(URL, auth=(user, password),
                      headers={"Content-Type": "application/json", "Accept": "application/json"}, data=data,
                      verify=False)
        print (r)

    def delete(self, vd, user, password, clustername):
        URL = self.URL_FORMAT % (vd, self.PORT) + '/analytics-cluster/' + clustername

        r = requests.delete(URL, auth=(user, password),
                      headers={"Content-Type": "application/json", "Accept": "application/json"},
                      verify=False)
        print (r)

    def show(self, vd, user, password):
        URL = self.URL_FORMAT % (vd, self.PORT) + '/analytics-cluster/'

        r = requests.get(URL, auth=(user, password),
                      headers={"Content-Type": "application/json", "Accept": "application/json"},
                      verify=False)
        print (r)
        cluster = r.json()
        for ac in cluster['analytics-cluster']:
            print("Analytics Cluster:", ac["name"],"Collector:", ac["log-collector-config"]["ip-address"][0], ":",
                  ac["log-collector-config"]["port"])








