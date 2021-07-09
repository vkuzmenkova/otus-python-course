import configparser

config = configparser.ConfigParser()
config.read('db.ini')

host = config['mysql']['host']
print(host)

sections = config.sections()
print(sections)


