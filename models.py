import config
from datetime import datetime
import peewee

db = None
if config.DBTYPE == 'postgresql':
    db = peewee.PostgresqlDatabase(config.PSQL_DBNAME,
        user=config.PSQL_USERNAME,
        password=config.PSQL_PASSWORD,
        host=config.PSQL_HOST)
else:
    db = peewee.SqliteDatabase(config.SQLITE_DBNAME)

class BaseModel(peewee.Model):
    class Meta:
        database = db

class BaseStatisticalObject(BaseModel):
    hmip_id = peewee.CharField()
    label = peewee.CharField(null=True)
    lastStatusUpdate = peewee.DateTimeField(null=True)
    roomname = peewee.CharField(null=True)
    rssiDeviceValue = peewee.IntegerField (null=True)
    rssiPeerValue = peewee.IntegerField(null=True)

class ShutterContact(BaseStatisticalObject):
    open = peewee.BooleanField(null=True)

class HeatingThermostat(BaseStatisticalObject):
    valvePosition = peewee.FloatField(null=True)

class PlugableSwitchingMeasuring(BaseStatisticalObject):
    currentPowerConsumption = peewee.FloatField(null=True)
    energyCounter = peewee.FloatField(null=True)
    on = peewee.BooleanField(null=True)

class WallmountedThermostatPro(BaseStatisticalObject):
    humidity = peewee.IntegerField(null=True)
    actualTemperature = peewee.FloatField(null=True)
    
