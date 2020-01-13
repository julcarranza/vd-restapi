python module for Versa Director REST APIs
=========================================

* Three files used:
  * jcVDmodule.py: Python module with analytics-cluster class for post, put, get, delete operations
  * analytics.yml: Yaml file for readable cluster data
  * Analyticscluster.py Python script to specify operation and read yaml file and convert to python dictionary

*REST API Status and Error Codes*

|Code |Description            |
|-----|-----------------------| 
|200  |OK (success)           |
|201  |Created                |
|202  |Accepted               |
|204  |No content             |
|400  |Bad request            |
|401  |Unauthorized           |
|405  |Method not allowed     |
|415  |Unsupported media type |
|500  |Internal error

julio@Julios-MacBook-Pro-2 vd-restapi % python3 analyticscluster.py                               
usage: analyticscluster.py [-h] [-y YMLFILE] [-s] [-m] [-c] [-d] VD user
analyticscluster.py: error: the following arguments are required: VD, user
julio@Julios-MacBook-Pro-2 vd-restapi % python3 analyticscluster.py  --help
usage: analyticscluster.py [-h] [-y YMLFILE] [-s] [-m] [-c] [-d] VD user

script to show, create, modify, delete, analytic cluster information using
APIs

positional arguments:
  VD          Versa Director IP address
  user        user used to login to director

optional arguments:
  -h, --help  show this help message and exit
  -y YMLFILE  yml file with analytics cluster variables
  -s          shows analytics cluster information
  -m          modify analytics cluster
  -c          create analytics cluster
  -d          delete analytics cluster
julio@Julios-MacBook-Pro-2 vd-restapi % python3 analyticscluster.py  10.48.85.102 Administrator -s
Password: 
<Response [200]>
Analytics Cluster: analytics01 Collector: 192.168.13.103 : 1234
julio@Julios-MacBook-Pro-2 vd-restapi % more analytics.yml 
#Analytics cluster variables
'ac':
  - 'name': 'analytics02'
    'collectorport': '10232'
    'collectorip': '192.168.13.222'
    'northboundip': '10.48.85.222'
    'northboundport': '8080'
  - 'name': 'analytics03'
    'collectorport': '10233'
    'collectorip': '192.168.13.223'
    'northboundip': '10.48.85.223'
    'northboundport': '8080'
  - 'name': 'analytics04'
    'collectorport': '10234'
    'collectorip': '192.168.13.224'
    'northboundip': '10.48.85.224 '
    'northboundport': '8080'
  - 'name': 'analytics05'
    'collectorport': '10235'
    'collectorip': '192.168.13.225'
    'northboundip': '10.48.85.225'
    'northboundport': '8080'


julio@Julios-MacBook-Pro-2 vd-restapi % python3 analyticscluster.py  10.48.85.102 Administrator -c -y analytics.yml 
Password: 
https://10.48.85.102:9182/api/config/nms/provider {"analytics-cluster": [{"name": "analytics02", "log-collector-config": {"port": "10232", "ip-address": ["192.168.13.222"]}, "connector-config": {"port": "8080", "web-addresses": [{"name": "nb", "ip-address": "10.48.85.222"}]}}]}
<Response [201]>
https://10.48.85.102:9182/api/config/nms/provider {"analytics-cluster": [{"name": "analytics03", "log-collector-config": {"port": "10233", "ip-address": ["192.168.13.223"]}, "connector-config": {"port": "8080", "web-addresses": [{"name": "nb", "ip-address": "10.48.85.223"}]}}]}
<Response [201]>
https://10.48.85.102:9182/api/config/nms/provider {"analytics-cluster": [{"name": "analytics04", "log-collector-config": {"port": "10234", "ip-address": ["192.168.13.224"]}, "connector-config": {"port": "8080", "web-addresses": [{"name": "nb", "ip-address": "10.48.85.224 "}]}}]}
<Response [201]>
https://10.48.85.102:9182/api/config/nms/provider {"analytics-cluster": [{"name": "analytics05", "log-collector-config": {"port": "10235", "ip-address": ["192.168.13.225"]}, "connector-config": {"port": "8080", "web-addresses": [{"name": "nb", "ip-address": "10.48.85.225"}]}}]}
<Response [201]>
julio@Julios-MacBook-Pro-2 vd-restapi % python3 analyticscluster.py  10.48.85.102 Administrator -s                 
Password: 
<Response [200]>
Analytics Cluster: analytics01 Collector: 192.168.13.103 : 1234
Analytics Cluster: analytics02 Collector: 192.168.13.222 : 10232
Analytics Cluster: analytics03 Collector: 192.168.13.223 : 10233
Analytics Cluster: analytics04 Collector: 192.168.13.224 : 10234
Analytics Cluster: analytics05 Collector: 192.168.13.225 : 10235
julio@Julios-MacBook-Pro-2 vd-restapi % more analytics1234.yml                                      
#Analytics cluster variables
'ac':
  - 'name': 'analytics02'
    'collectorport': '1234'
    'collectorip': '192.168.13.222'
    'northboundip': '10.48.85.222'
    'northboundport': '8080'
  - 'name': 'analytics03'
    'collectorport': '1234'
    'collectorip': '192.168.13.223'
    'northboundip': '10.48.85.223'
    'northboundport': '8080'
  - 'name': 'analytics04'
    'collectorport': '1234'
    'collectorip': '192.168.13.224'
    'northboundip': '10.48.85.224 '
    'northboundport': '8080'
  - 'name': 'analytics05'
    'collectorport': '1234'
    'collectorip': '192.168.13.225'
    'northboundip': '10.48.85.225'
    'northboundport': '8080'


julio@Julios-MacBook-Pro-2 vd-restapi % python3 analyticscluster.py  10.48.85.102 Administrator -m -y analytics1234.yml
Password: 
https://10.48.85.102:9182/api/config/nms/provider/analytics-cluster/analytics02 {"analytics-cluster": [{"name": "analytics02", "log-collector-config": {"port": "1234", "ip-address": ["192.168.13.222"]}, "connector-config": {"port": "8080", "web-addresses": [{"name": "nb", "ip-address": "10.48.85.222"}]}}]}
<Response [204]>
https://10.48.85.102:9182/api/config/nms/provider/analytics-cluster/analytics03 {"analytics-cluster": [{"name": "analytics03", "log-collector-config": {"port": "1234", "ip-address": ["192.168.13.223"]}, "connector-config": {"port": "8080", "web-addresses": [{"name": "nb", "ip-address": "10.48.85.223"}]}}]}
<Response [204]>
https://10.48.85.102:9182/api/config/nms/provider/analytics-cluster/analytics04 {"analytics-cluster": [{"name": "analytics04", "log-collector-config": {"port": "1234", "ip-address": ["192.168.13.224"]}, "connector-config": {"port": "8080", "web-addresses": [{"name": "nb", "ip-address": "10.48.85.224 "}]}}]}
<Response [204]>
https://10.48.85.102:9182/api/config/nms/provider/analytics-cluster/analytics05 {"analytics-cluster": [{"name": "analytics05", "log-collector-config": {"port": "1234", "ip-address": ["192.168.13.225"]}, "connector-config": {"port": "8080", "web-addresses": [{"name": "nb", "ip-address": "10.48.85.225"}]}}]}
<Response [204]>
julio@Julios-MacBook-Pro-2 vd-restapi % python3 analyticscluster.py  10.48.85.102 Administrator -s                     
Password: 
<Response [200]>
Analytics Cluster: analytics01 Collector: 192.168.13.103 : 1234
Analytics Cluster: analytics02 Collector: 192.168.13.222 : 1234
Analytics Cluster: analytics03 Collector: 192.168.13.223 : 1234
Analytics Cluster: analytics04 Collector: 192.168.13.224 : 1234
Analytics Cluster: analytics05 Collector: 192.168.13.225 : 1234
julio@Julios-MacBook-Pro-2 vd-restapi % python3 analyticscluster.py  10.48.85.102 Administrator  -d -y analytics1234.yml
Password: 
<Response [204]>
<Response [204]>
<Response [204]>
<Response [204]>
julio@Julios-MacBook-Pro-2 vd-restapi % python3 analyticscluster.py                               
usage: analyticscluster.py [-h] [-y YMLFILE] [-s] [-m] [-c] [-d] VD user
analyticscluster.py: error: the following arguments are required: VD, user
julio@Julios-MacBook-Pro-2 vd-restapi % python3 analyticscluster.py  --help
usage: analyticscluster.py [-h] [-y YMLFILE] [-s] [-m] [-c] [-d] VD user

script to show, create, modify, delete, analytic cluster information using
APIs

positional arguments:
  VD          Versa Director IP address
  user        user used to login to director

optional arguments:
  -h, --help  show this help message and exit
  -y YMLFILE  yml file with analytics cluster variables
  -s          shows analytics cluster information
  -m          modify analytics cluster
  -c          create analytics cluster
  -d          delete analytics cluster
julio@Julios-MacBook-Pro-2 vd-restapi % python3 analyticscluster.py  10.48.85.102 Administrator -s
Password: 
<Response [200]>
Analytics Cluster: analytics01 Collector: 192.168.13.103 : 1234
julio@Julios-MacBook-Pro-2 vd-restapi % more analytics.yml 
#Analytics cluster variables
'ac':
  - 'name': 'analytics02'
    'collectorport': '10232'
    'collectorip': '192.168.13.222'
    'northboundip': '10.48.85.222'
    'northboundport': '8080'
  - 'name': 'analytics03'
    'collectorport': '10233'
    'collectorip': '192.168.13.223'
    'northboundip': '10.48.85.223'
    'northboundport': '8080'
  - 'name': 'analytics04'
    'collectorport': '10234'
    'collectorip': '192.168.13.224'
    'northboundip': '10.48.85.224 '
    'northboundport': '8080'
  - 'name': 'analytics05'
    'collectorport': '10235'
    'collectorip': '192.168.13.225'
    'northboundip': '10.48.85.225'
    'northboundport': '8080'


julio@Julios-MacBook-Pro-2 vd-restapi % python3 analyticscluster.py  10.48.85.102 Administrator -c -y analytics.yml 
Password: 
https://10.48.85.102:9182/api/config/nms/provider {"analytics-cluster": [{"name": "analytics02", "log-collector-config": {"port": "10232", "ip-address": ["192.168.13.222"]}, "connector-config": {"port": "8080", "web-addresses": [{"name": "nb", "ip-address": "10.48.85.222"}]}}]}
<Response [201]>
https://10.48.85.102:9182/api/config/nms/provider {"analytics-cluster": [{"name": "analytics03", "log-collector-config": {"port": "10233", "ip-address": ["192.168.13.223"]}, "connector-config": {"port": "8080", "web-addresses": [{"name": "nb", "ip-address": "10.48.85.223"}]}}]}
<Response [201]>
https://10.48.85.102:9182/api/config/nms/provider {"analytics-cluster": [{"name": "analytics04", "log-collector-config": {"port": "10234", "ip-address": ["192.168.13.224"]}, "connector-config": {"port": "8080", "web-addresses": [{"name": "nb", "ip-address": "10.48.85.224 "}]}}]}
<Response [201]>
https://10.48.85.102:9182/api/config/nms/provider {"analytics-cluster": [{"name": "analytics05", "log-collector-config": {"port": "10235", "ip-address": ["192.168.13.225"]}, "connector-config": {"port": "8080", "web-addresses": [{"name": "nb", "ip-address": "10.48.85.225"}]}}]}
<Response [201]>
julio@Julios-MacBook-Pro-2 vd-restapi % python3 analyticscluster.py  10.48.85.102 Administrator -s                 
Password: 
<Response [200]>
Analytics Cluster: analytics01 Collector: 192.168.13.103 : 1234
Analytics Cluster: analytics02 Collector: 192.168.13.222 : 10232
Analytics Cluster: analytics03 Collector: 192.168.13.223 : 10233
Analytics Cluster: analytics04 Collector: 192.168.13.224 : 10234
Analytics Cluster: analytics05 Collector: 192.168.13.225 : 10235
julio@Julios-MacBook-Pro-2 vd-restapi % more analytics1234.yml                                      
#Analytics cluster variables
'ac':
  - 'name': 'analytics02'
    'collectorport': '1234'
    'collectorip': '192.168.13.222'
    'northboundip': '10.48.85.222'
    'northboundport': '8080'
  - 'name': 'analytics03'
    'collectorport': '1234'
    'collectorip': '192.168.13.223'
    'northboundip': '10.48.85.223'
    'northboundport': '8080'
  - 'name': 'analytics04'
    'collectorport': '1234'
    'collectorip': '192.168.13.224'
    'northboundip': '10.48.85.224 '
    'northboundport': '8080'
  - 'name': 'analytics05'
    'collectorport': '1234'
    'collectorip': '192.168.13.225'
    'northboundip': '10.48.85.225'
    'northboundport': '8080'


julio@Julios-MacBook-Pro-2 vd-restapi % python3 analyticscluster.py  10.48.85.102 Administrator -m -y analytics1234.yml
Password: 
https://10.48.85.102:9182/api/config/nms/provider/analytics-cluster/analytics02 {"analytics-cluster": [{"name": "analytics02", "log-collector-config": {"port": "1234", "ip-address": ["192.168.13.222"]}, "connector-config": {"port": "8080", "web-addresses": [{"name": "nb", "ip-address": "10.48.85.222"}]}}]}
<Response [204]>
https://10.48.85.102:9182/api/config/nms/provider/analytics-cluster/analytics03 {"analytics-cluster": [{"name": "analytics03", "log-collector-config": {"port": "1234", "ip-address": ["192.168.13.223"]}, "connector-config": {"port": "8080", "web-addresses": [{"name": "nb", "ip-address": "10.48.85.223"}]}}]}
<Response [204]>
https://10.48.85.102:9182/api/config/nms/provider/analytics-cluster/analytics04 {"analytics-cluster": [{"name": "analytics04", "log-collector-config": {"port": "1234", "ip-address": ["192.168.13.224"]}, "connector-config": {"port": "8080", "web-addresses": [{"name": "nb", "ip-address": "10.48.85.224 "}]}}]}
<Response [204]>
https://10.48.85.102:9182/api/config/nms/provider/analytics-cluster/analytics05 {"analytics-cluster": [{"name": "analytics05", "log-collector-config": {"port": "1234", "ip-address": ["192.168.13.225"]}, "connector-config": {"port": "8080", "web-addresses": [{"name": "nb", "ip-address": "10.48.85.225"}]}}]}
<Response [204]>
julio@Julios-MacBook-Pro-2 vd-restapi % python3 analyticscluster.py  10.48.85.102 Administrator -s                     
Password: 
<Response [200]>
Analytics Cluster: analytics01 Collector: 192.168.13.103 : 1234
Analytics Cluster: analytics02 Collector: 192.168.13.222 : 1234
Analytics Cluster: analytics03 Collector: 192.168.13.223 : 1234
Analytics Cluster: analytics04 Collector: 192.168.13.224 : 1234
Analytics Cluster: analytics05 Collector: 192.168.13.225 : 1234
julio@Julios-MacBook-Pro-2 vd-restapi % python3 analyticscluster.py  10.48.85.102 Administrator  -d -y analytics1234.yml
Password: 
<Response [204]>
<Response [204]>
<Response [204]>
<Response [204]>
julio@Julios-MacBook-Pro-2 vd-restapi % 
