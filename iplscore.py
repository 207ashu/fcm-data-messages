from pyfcm import FCMNotification

api_key="YOUR_SERVER_KEY"
registration_id="YOUR_DEVICE_TOKEN"
push_service = FCMNotification(api_key)

for i in range(1,2):
    data={
    "collapse_key":"123456",
    "name":"ashutosh",
    "no":"9911224455",
    "count":1
    }
    result = push_service.single_device_data_message(registration_id, data_message=data)
    print(result)
