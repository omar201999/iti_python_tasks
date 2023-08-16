from fabric import Connection
c = Connection(host='10.0.2.15', user='omar',
               connect_kwargs={'password': '2011'})
result = c.run('ls -l', hide=True)
print(result.stdout)
