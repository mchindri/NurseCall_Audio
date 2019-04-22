package com.example.myapplication;

import android.util.Log;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;


public class AudioServer extends Thread {
    String line;
    private ServerSocket server;
    private Socket client;
    private BufferedReader in;
    private PrintWriter out;

    public AudioServer()
    {
    }

    public void run()
    {
/*
        listenSocket();
        while(true){
            try{
                line = in.readLine();

                //Send data back to client
                out.println(line);
                Log.d("MY_TAG","From client:" + line);
            } catch (IOException e) {
                Log.d("MY_TAG", "Read failed");
                System.exit(-1);
            }
        }
*/
    }

    public void listenSocket(){
        Log.d("MY_TAG", "Starting server");
        try{
            server = new ServerSocket(50007);
        } catch (IOException e) {
            Log.d("MY_TAG", "Could not listen on port 50007");
            System.exit(-1);
        }

        //listenSocketSocketserver.acceptSocket
        try{
            client = server.accept();
        } catch (IOException e) {
            Log.d("MY_TAG", "Accept failed: 50007");
            System.exit(-1);
        }


        Log.d("MY_TAG", "Client connected");

        //listenSocketBufferedReaderclientPrintWriter
        try{
            in = new BufferedReader(new InputStreamReader(
                    client.getInputStream()));
            out = new PrintWriter(client.getOutputStream(),
                    true);
        } catch (IOException e) {
            Log.d("MY_TAG", "Read failed");
            System.exit(-1);
        }
    }

}

