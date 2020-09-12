package com.example.hello;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;

import androidx.annotation.NonNull;
import androidx.localbroadcastmanager.content.LocalBroadcastManager;

import com.google.firebase.messaging.FirebaseMessagingService;
import com.google.firebase.messaging.RemoteMessage;

import java.util.Locale;
import java.util.Map;

public class MyFirebaseMessagingService extends FirebaseMessagingService {
    @Override
    public void onMessageReceived(@NonNull RemoteMessage remoteMessage) {
        super.onMessageReceived(remoteMessage);
        Log.d("fcm message recieved", remoteMessage.toString());

         if(remoteMessage.getData().size()>0){

            String count = remoteMessage.getData().get("count");
             Intent i= new Intent("com.example.hello_fcm");
             i.putExtra("count",count);
             LocalBroadcastManager bm=LocalBroadcastManager.getInstance(this);
             bm.sendBroadcast(i);


         }

    }
}
