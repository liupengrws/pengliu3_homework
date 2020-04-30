# -*- coding:utf-8 -*-
"""homework: 
@author: Peng Liu
@contact: pengliu3@cisco.com
@file: query_vendor_by_mac.py
@time: 2020/04/30 12:00
@desc: query vendor name by mac address
"""

import os, sys, time, traceback
import requests

url = 'https://api.macaddress.io/v1'
headers = {
    'Cache-Control': 'no-cache',
    'Accept': 'application/json',
    'X-Authentication-Token': 'at_7qbk4lVuq1Lxeaz6v6eYUnUweroka'
}

def query_vendor(maddr):
	params = {'search': maddr}
	res = requests.get(url, headers=headers, params=params)
	print(res.text)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('Please input MAC address.')
		sys.exit()

	query_vendor(sys.argv[1])

