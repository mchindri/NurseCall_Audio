package com.example.myapplication;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.ListView;
import android.widget.Toast;


public class room1_activity extends AppCompatActivity {

    ListView listview;
    String[] items = {"Pop Alexandru", "Chindris Mihai", "Alex pop"};
    ImageButton call;
    ImageButton endcall;

    private Button button_back_room1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_room1_activity);

        listview = findViewById(R.id.listview);
        call =  findViewById(R.id.call);

        endcall = findViewById(R.id.endcall);
        button_back_room1 = findViewById(R.id.button_back_room1);

        final ArrayAdapter<String> adapter = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, android.R.id.text1, items);
        listview.setAdapter(adapter);

        call.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                goBack();
            }
        });
        button_back_room1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                goBack();
            }
        });
    }

    public void goBack(){
        Intent intent = new Intent(this, MainActivity.class);
        startActivity(intent);
    }
}
