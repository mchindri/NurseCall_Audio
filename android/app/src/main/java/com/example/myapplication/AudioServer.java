package com.example.myapplication;

import android.media.AudioFormat;
import android.media.AudioManager;
import android.media.AudioTrack;
import android.util.Log;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;


public class AudioServer extends Thread {
    String line;
    private ServerSocket server;
    private Socket client;
    Socket socket;
    private InputStream in;
    private PrintWriter out;


    public AudioServer()
    {
    }

    public void playWav(AudioTrack at, byte[] buff, int len)
    {
    }

    public void run()
    {

        //format 2
        //channels 2
        //frmae rate 44100
        int minBufferSize = AudioTrack.getMinBufferSize(44100, AudioFormat.CHANNEL_IN_STEREO, AudioFormat.ENCODING_PCM_16BIT);
        int bufferSize = 1024;
        if (minBufferSize > bufferSize)
            bufferSize = minBufferSize;
        AudioTrack at = new AudioTrack(AudioManager.STREAM_MUSIC, 44100, AudioFormat.CHANNEL_IN_STEREO, AudioFormat.ENCODING_PCM_16BIT, bufferSize , AudioTrack.MODE_STREAM);
        at.play();

        listenSocket();
        while(true){
            try{

                int CHUNK = 1024;
                byte[] buff = new byte[CHUNK + 1];

                int len;
                while ((len = in.read(buff, 0, CHUNK)) > -1)
                {
                    at.write(buff, 0, len);
                }
                //Send data back to client
                out.println("Response");

            } catch (IOException e) {
                Log.d("MY_TAG", "Read failed");
                System.exit(-1);
            }
            catch (Exception e)
            {
                Log.d("MY_TAG", e.getMessage());
                System.exit(-1);
            }
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

    }

    public void listenSocket(){
        Log.d("MY_TAG", "Starting server");
        try{
            server = new ServerSocket(50007);

        } catch (IOException e) {
            Log.d("MY_TAG", "Could not listen on port 50007");
            Log.d("MY_TAG", e.getMessage()
            );

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
            in = client.getInputStream();
            out = new PrintWriter(client.getOutputStream(),
                    true);
        } catch (IOException e) {
            Log.d("MY_TAG", "Read failed");
            System.exit(-1);
        }
    }

}

