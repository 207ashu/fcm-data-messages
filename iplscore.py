from pyfcm import FCMNotification

push_service = FCMNotification(api_key="SERVER_KEY_FROM_FIREBASE_CONSOLE")

data_message = {
"match":{
"2_inning": {
    "teamName": "",
    "runs": 152,
    "wickets": 3,
    "overs": "4.5",
    "teamColor": "ffffff",
    "batting": {
        "striker": {
            "fullname": "Dwayne Bravo",
            "name": "Dwayne Bravo",
            "firstName": "",
            "lastName": "",
            "runs": 50,
            "balls": 5
        },
        "non_striker": {
            "fullname": "Dwayne Bravo",
            "name": "Dwayne Bravo",
            "firstName": "",
            "lastName": "",
            "runs": 50,
            "balls":5
        }
    }
},
"1_inning": {
    "teamName": "",
    "runs": 152,
    "wickets": 5,
    "overs": "20",
    "teamColor": "000000",
    "batting": {
        "striker": {
            "fullname": "Dwayne Bravo",
            "name": "Dwayne Bravo",
            "firstName": "",
            "lastName": "",
            "runs":100 ,
            "balls":20
        },
        "non_striker": {
            "runs": 100,
            "balls": 20
        }
    }
},
"match_status": "",
"toss": {
    "details": "Australia won the toss and chose to bowl first"
}
}
}


result = push_service.single_device_data_message(registration_id="CLIENT_SIDE_FIREBASE_TOKEN", data_message=data_message)
