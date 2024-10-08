import asyncio
import logging

from asyncua import Server, ua
import time
import random
import sys
sys.path.insert(0, "..")


from opcua import Client


if __name__ == "__main__":
    
    client = Client("opc.tcp://192.168.43.129:51210/UA/SampleServer")
    
    # client = Client("opc.tcp://admin@localhost:4840/freeopcua/server/") #connect using a user
    try:
        client.connect()
        while True:
        # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
            time.sleep(2)
            root = client.get_root_node()
            var_hr = client.get_node("ns=3;s=AASROOT.HumidityAndTemperatureSensor.OperationalData.ActualHumidity.Value")
            var_temp = client.get_node("ns=3;s=AASROOT.HumidityAndTemperatureSensor.OperationalData.ActualTemperature.Value")
            var_batt = client.get_node("ns=3;s=AASROOT.HumidityAndTemperatureSensor.OperationalData.Batery.Value")


            var_1 = var_hr.get_value()
            var_2 = var_temp.get_value()
            var_3 = var_batt.get_value()

            #print("My Object is: ", var_hr)
            print("Actual Relative Humidity [%]: ", var_1)
            new_val_1 = random.uniform(45,55)
            var_hr.set_value(new_val_1)

            new_val_2 = random.uniform(17,20)
            var_temp.set_value(new_val_2)
            print("Actual Temperature [°C]: ", var_2)

            new_val_3 = 4.8
            var_batt.set_value(new_val_3)
            print("Actual Battery [V]: ", var_3)
    
            #asyncio.main()

    
                    

        # Stacked myvar access
        # print("myvar is: ", root.get_children()[0].get_children()[1].get_variables()[0].get_value())

    finally:
        client.disconnect()

