package com.example.myapplication;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.animation.AlphaAnimation;
import android.view.animation.Animation;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.ListView;
import android.widget.Toast;

import java.util.List;
import java.util.Random;

import static java.lang.Thread.sleep;

public class MainActivity extends AppCompatActivity {

    ListView listview;
    private Button button_room1, button_room2, button_room3, button_room4, button_room5;
    private CheckBox checkbox_1, checkbox_2, checkbox_3, checkbox_4, checkbox_5;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        button_room1 = findViewById(R.id.button_room1);
        button_room2 = findViewById(R.id.button_room2);
        button_room3 = findViewById(R.id.button_room3);
        button_room4 = findViewById(R.id.button_room4);
        button_room5 = findViewById(R.id.button_room5);
        listview = findViewById(R.id.listview);
        checkbox_1 = findViewById(R.id.checkBox_1);

        new AudioServer().start();

        final Animation anim = new AlphaAnimation(0.0f, 1.0f);
        anim.setDuration(150); //You can manage the blinking time with this parameter
        anim.setStartOffset(20);
        anim.setRepeatMode(Animation.REVERSE);
        anim.setRepeatCount(Animation.INFINITE);

        //button.startAnimation(anim);

        checkbox_1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(checkbox_1.isChecked())
                    button_room1.startAnimation(anim);
                else
                    button_room1.clearAnimation();
            }
        });


        button_room1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openRoom1();

            }
        });

        button_room2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openRoom2();
            }
        });

        button_room3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openRoom3();
            }
        });

        button_room4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openRoom4();
            }
        });

        button_room5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openRoom5();
            }
        });
    }

    public void openRoom1(){
        Intent intent = new Intent(this, room1_activity.class);
        startActivity(intent);
    }
    public void openRoom2(){
        Intent intent = new Intent(this, room2_activity.class);
        startActivity(intent);
    }
    public void openRoom3(){
        Intent intent = new Intent(this, room3_activity.class);
        startActivity(intent);
    }
    public void openRoom4(){
        Intent intent = new Intent(this, room4_activity.class);
        startActivity(intent);
    }
    public void openRoom5(){
        Intent intent = new Intent(this, room5_activity.class);
        startActivity(intent);
    }

}
