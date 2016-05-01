from getpass import getpass
from foreman.client import Foreman
f = Foreman('https://192.168.99.100:8443', ('admin', 'changeme'))


print(f.index_hosts())

print(f.show_hosts(id=1))

res = f.create_hosts(host={'name': 'mynewhost', 'ip': '192.168.1.1', 'mac': '00:00:00:00:00:00'})
