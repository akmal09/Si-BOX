import json
import psutil
import shutil
import wmi
import platform


#temperature
# w = wmi.WMI(namespace="root\wmi")
# temperature_info = w.MSAcpi_ThermalZoneTemperature()[0]
# print (temperature_info.CurrentTemperature)

#CPU usage
def check_monitor():
    path = 'C:/Users'
    CPU_usage = psutil.cpu_percent()
    MEMORY_used = shutil.disk_usage(path)
    RAM_used = psutil.virtual_memory()[2]
    
    value = {
        "CPU usage" : CPU_usage,
        "Memory usage" : MEMORY_used,
        "RAM usage" : RAM_used
    }
    return json.dumps(value)

#
#
# CPU Temp --REQUIRES CPU TEMPERATURE TO BE RUNNING!--
#
print (check_monitor())