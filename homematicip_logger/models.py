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
    label = peewee.CharField()
    lastStatusUpdate = peewee.DateTimeField(null=True)
    roomname = peewee.CharField()

class ShutterContact(BaseStatisticalObject):
    open = peewee.BooleanField()

class HeatingThermostat(BaseStatisticalObject):
    valvePosition = peewee.FloatField()

class PlugableSwitchingMeasuring(BaseStatisticalObject):
    currentPowerConsumption = peewee.FloatField()
    energyCounter = peewee.FloatField()

class WallmountedThermostatPro(BaseStatisticalObject):
    humidity = peewee.IntegerField()
    actualTemperature = peewee.FloatField()
    