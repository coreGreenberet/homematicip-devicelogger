import models
from homematicip.home import Home
import config
import time
from homematicip.device import ShutterContact,HeatingThermostat,PlugableSwitchMeasuring,WallMountedThermostatPro
models.db.connect()

home = Home()
home.set_auth_token(config.AUTH_TOKEN)
home.init(config.ACCESS_POINT)


def write_shutter(room,device):
    result = models.ShutterContact.select().where((models.ShutterContact.hmip_id==device.id) & (models.ShutterContact.lastStatusUpdate==device.lastStatusUpdate)).execute()
    if len(result)==0:
        models.ShutterContact.create(roomname=room, hmip_id=device.id, label=device.label, lastStatusUpdate=device.lastStatusUpdate, open=device.windowState=='OPEN', rssiPeerValue=device.rssiPeerValue, rssiDeviceValue=device.rssiDeviceValue)

def write_heatingthermostat(room,device):
    result = models.HeatingThermostat.select().where((models.HeatingThermostat.hmip_id==device.id) & (models.HeatingThermostat.lastStatusUpdate==device.lastStatusUpdate)).execute()
    if len(result)==0:
        models.HeatingThermostat.create(roomname=room, hmip_id=device.id, label=device.label, lastStatusUpdate=device.lastStatusUpdate, valvePosition=device.valvePosition, rssiPeerValue=device.rssiPeerValue, rssiDeviceValue=device.rssiDeviceValue)

def write_plugableswitchmeasuring(room,device):
    result = models.PlugableSwitchingMeasuring.select().where((models.PlugableSwitchingMeasuring.hmip_id==device.id) & (models.PlugableSwitchingMeasuring.lastStatusUpdate==device.lastStatusUpdate)).execute()
    if len(result)==0:
        models.PlugableSwitchingMeasuring.create(roomname=room, hmip_id=device.id, label=device.label, lastStatusUpdate=device.lastStatusUpdate, currentPowerConsumption=device.currentPowerConsumption, energyCounter=device.energyCounter, on=device.on, rssiPeerValue=device.rssiPeerValue, rssiDeviceValue=device.rssiDeviceValue)

def write_wallmountedthermostatpro(room,device):
    result = models.WallmountedThermostatPro.select().where((models.WallmountedThermostatPro.hmip_id==device.id) & (models.WallmountedThermostatPro.lastStatusUpdate==device.lastStatusUpdate)).execute()
    if len(result)==0:
        models.WallmountedThermostatPro.create(roomname=room, hmip_id=device.id, label=device.label, lastStatusUpdate=device.lastStatusUpdate, actualTemperature=device.actualTemperature, humidity=device.humidity, rssiPeerValue=device.rssiPeerValue, rssiDeviceValue=device.rssiDeviceValue)


def main():
    global home
    home.get_current_state()
    for g in home.groups:
        if g.groupType=="META":
            for d in g.devices:
                if isinstance(d,ShutterContact):
                    write_shutter(g.label,d)
                elif isinstance(d,HeatingThermostat):
                    write_heatingthermostat(g.label,d)
                elif isinstance(d,PlugableSwitchMeasuring):
                    write_plugableswitchmeasuring(g.label,d)
                elif isinstance(d,WallMountedThermostatPro):
                    write_wallmountedthermostatpro(g.label,d)

if __name__ == "__main__":
    main()