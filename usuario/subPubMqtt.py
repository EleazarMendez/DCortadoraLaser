from awscrt import io, mqtt
from awsiot import mqtt_connection_builder
import json, os
from dotenv import load_dotenv

def publish():
    load_dotenv()
    TOPIC=os.getenv('TOPIC')
    event_loop_group=io.EventLoopGroup(1)
    host_resolver=io.DefaultHostResolver(event_loop_group)
    client_boostrap=io.ClientBootstrap(event_loop_group, host_resolver)
    mqtt_connection=mqtt_connection_builder.mtls_from_path(
        endpoint=os.getenv('ENDPOINT'),
        cert_filepath='usuario/AWS/certificate.pem.crt',
        pri_key_filepath='usuario/AWS/private.pem.key',
        client_boostrap=client_boostrap,
        ca_filepath='usuario/AWS/AmazonRootCA1.pem',
        client_id=os.getenv('CLIENT_ID'),
        clean_session=False,
        keep_alive_secs=60
    )
    connect_future=mqtt_connection.connect()
    mensaje={"Inicio":1}
    payload=json.dumps(mensaje)
    mqtt_connection.publish(topic=TOPIC, payload=payload, qos=mqtt.QoS.AT_LEAST_ONCE) 
    return 

