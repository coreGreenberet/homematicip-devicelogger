from models import *

print 'Connecting to database...'
db.connect()

print 'Dropping Tables'
#db.drop_tables( [ BaseModel, BaseStatisticalObject, ShutterContact, WallmountedThermostatPro, HeatingThermostat, PlugableSwitchingMeasuring ], True)

print 'Creating Tables'
db.create_tables( [ BaseModel, BaseStatisticalObject, ShutterContact, WallmountedThermostatPro, HeatingThermostat, PlugableSwitchingMeasuring ], True)

print 'Finished'