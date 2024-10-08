import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import paho.mqtt.client as mqtt
import json



#Este script funciona tomando los datos de broker MQTT generado por TTN

#host_name = "eu1.cloud.thethings.network"
#socket.getaddrinfo(host_name,1883)
topic = "v3/ht-sensor-project-br@ttn/devices/eui-a840416051871229/up"

def on_connect(client, userdata, flags, reason_code, properties=None):
    
    client.subscribe(topic)

def on_message(client, userdata, msg, properties=None):
    print(msg.topic, msg.payload)
    arch = json.loads(msg.payload)#'{"end_device_ids":{"device_id":"eui-a840416051871229","application_ids":{"application_id":"ht-sensor-project-br"},"dev_eui":"A840416051871229","join_eui":"A840410000000101","dev_addr":"260BD7F2"},"correlation_ids":["pba:uplink:01J1ABGBN9H0FCZKZEDEGMMX8Q"],"received_at":"2024-06-26T13:24:35.323956942Z","uplink_message":{"session_key_id":"AZBUuA2id+tKAflucVnzOg==","f_port":2,"frm_payload":"Dm8AAAEMAAEXAfY=","decoded_payload":{"ADC_CH0V":0.268,"BatV":3.695,"Digital_IStatus":"L","Door_status":"OPEN","EXTI_Trigger":"FALSE","Hum_SHT":50.2,"TempC1":0,"TempC_SHT":27.9,"Work_mode":"IIC"},"rx_metadata":[{"gateway_ids":{"gateway_id":"packetbroker"},"packet_broker":{"message_id":"01J1ABGBN9H0FCZKZEDEGMMX8Q","forwarder_net_id":"000013","forwarder_tenant_id":"ttnv2","forwarder_cluster_id":"ttn-v2-legacy-eu","forwarder_gateway_eui":"7076FF0056050C89","forwarder_gateway_id":"eui-7076ff0056050c89","home_network_net_id":"000013","home_network_tenant_id":"ttn","home_network_cluster_id":"eu1.cloud.thethings.network"},"time":"2024-06-26T13:24:37.052Z","rssi":-113,"channel_rssi":-113,"snr":5.5,"location":{"latitude":53.36784045,"longitude":7.18291479,"altitude":12},"uplink_token":"CvwCZXlKaGJHY2lPaUpCTVRJNFIwTk5TMWNpTENKbGJtTWlPaUpCTVRJNFIwTk5JaXdpYVhZaU9pSXRNMHd3VVZSRVZuaDJjbUo1YnpscElpd2lkR0ZuSWpvaVUxb3lRMmxGTW5kMWNuTkNVMGxJTlRoUU9EbHFaeUo5LkpjREtOR0hBUkJ2d0pLRG15TDBQQVEuV3lsdklERHdISmFycFhkay55OXVkbUxjcWtacTZWVHlKemNOSllZNnFxaDFkSTVaLVNlSjZZZFF0WGxCLU13R2lLclVSdjhjcGpoSno0ZDRseXIxeG1fUXlNOXZaLVhZSTdqQXNOQ2swbjJrM0Z1Sjh4VnBCRXhCeFBVNlJXYXdfTUIzSVdwV1ZPZ1RqREZpQlVzMFFUcG5PblpJbDNnRTR5TDdCX3dYU1d6Mnk2VTctZ2pqSmR4NUlzdllCN0l3UHBNb1FHbm5hRFUwN3J0eVhrbUR4LkFKV1VwTmU0OFRjeGNhYm4zWUJJQ2caHgoDAAATEgV0dG52MhoQdHRuLXYyLWxlZ2FjeS1ldQ==","received_at":"2024-06-26T13:24:35.106209352Z"},{"gateway_ids":{"gateway_id":"eui-58a0cbfffe801169","eui":"58A0CBFFFE801169"},"time":"2024-06-26T13:24:35.000891923Z","timestamp":2784814452,"rssi":-112,"channel_rssi":-112,"snr":-7.25,"uplink_token":"CiIKIAoUZXVpLTU4YTBjYmZmZmU4MDExNjkSCFigy//+gBFpEPTK868KGgsIk63wswYQ/MjzOiCgmoGfhpsS","received_at":"2024-06-26T13:24:35.094708939Z"},{"gateway_ids":{"gateway_id":"gateway-s115-v3","eui":"58A0CBFFFE8026D0"},"time":"2024-06-26T13:24:35.032876968Z","timestamp":4151335428,"rssi":-104,"channel_rssi":-104,"snr":3.5,"uplink_token":"Ch0KGwoPZ2F0ZXdheS1zMTE1LXYzEghYoMv//oAm0BCEtMG7DxoLCJOt8LMGEPjx5z0goL/+9ujCEg==","received_at":"2024-06-26T13:24:35.023642150Z"},{"gateway_ids":{"gateway_id":"lorix-hs-emden-leer","eui":"FCC23DFFFE0B74E6"},"timestamp":1892638044,"rssi":-82,"channel_rssi":-82,"snr":9.8,"location":{"latitude":53.3677715,"longitude":7.18512,"altitude":13,"source":"SOURCE_REGISTRY"},"uplink_token":"CiEKHwoTbG9yaXgtaHMtZW1kZW4tbGVlchII/MI9//4LdOYQ3Lq9hgcaCwiTrfCzBhCPppE+IODektCK9RU=","channel_index":4,"received_at":"2024-06-26T13:24:35.113487101Z"}],"settings":{"data_rate":{"lora":{"bandwidth":125000,"spreading_factor":12,"coding_rate":"4/5"}},"frequency":"867300000"},"received_at":"2024-06-26T13:24:35.116615676Z","consumed_airtime":"1.482752s","version_ids":{"brand_id":"dragino","model_id":"lsn50v2-s31","hardware_version":"_unknown_hw_version_","firmware_version":"1.7.4","band_id":"EU_863_870"},"network_ids":{"net_id":"000013","ns_id":"EC656E0000000181","tenant_id":"ttn","cluster_id":"eu1","cluster_address":"eu1.cloud.thethings.network"}}}')

#print(arch['uplink_message'])

    arch_2 = arch['uplink_message']

#print(arch_2['decoded_payload'])
    arch_3 = arch_2['decoded_payload']

    #var_1 = arch_3['BatV']
    print(arch_3['BatV'])
    print(arch_3['Hum_SHT'])
    #var_2 = arch_3['Hum_SHT']
    #var_3 = arch_3['TempC_SHT']
    #conect_DB.insert_data(var_1, var_2, var_3)




client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, protocol=mqtt.MQTTv311)

client.on_connect = on_connect
client.on_message = on_message
#client.username_pw_set(username="ht-sensor-project-br@ttn", password="NNSXS.HVXQUTRIXKKGXW2TVRUJUPM5WRUVOCUXMHRWWRQ.NSBQB4F6UPMNM35FFC3M7ASGFJMAIAYMANM6UVVI2F5GK55DZMFA")
client.tls_set()  # <--- even without arguments

print("Connecting...")
client.connect("eu1.cloud.thethings.network", port=8883,keepalive=60) #Public TLS Address from TTN
client.loop_forever()
