# pengliu3_homework
query vendor name by MAC address

# environment
CentOS7, Python3

# install
$ pip install requests

# run
$ python query_vendor_by_mac.py <mac_address>

# docker
$ docker build -t homework-python3-pengliu3 .  
$ docker run homework-python3-pengliu3 python ./query_vendor_by_mac.py <mac_address>

# security considerations
- use https
- save token in a file which can be accessed by only specifiled users.
