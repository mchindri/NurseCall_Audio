package com.example.myapplication;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.textservice.SuggestionsInfo;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.ListView;
import android.widget.Toast;

import java.util.ArrayList;


public class room1_activity extends AppCompatActivity {

    ListView listview, listview2;

    ImageButton call;
    ImageButton endcall;

    private Button button_back_room1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_room1_activity);

        ////////////

        listview = findViewById(R.id.listview);
        listview2 = findViewById(R.id.listview2);
        call =  findViewById(R.id.call);
        endcall = findViewById(R.id.endcall);
        button_back_room1 = findViewById(R.id.button_back_room1);

        ////////////



        Person alex = new Person("Denis Gavrila ", "21-11-1971", "Male");
        Person diana = new Person("Pop Diana", "30-10-2006", "Female");
        Person mihai = new Person("Chindris Mihai", "29-07-1996", "Female");
        Person dan = new Person("Anton Dan", "11-11-1990", "Male");
        Person alin = new Person("Moldovan Alin", "10-04-1987", "Male");
        Person andrei = new Person("Ormenisan Andrei", "01-01-1981", "Male");

        Person e1 = new Person("Denis Gavrila", "Medicament", "15:45");
        Person e2 = new Person("Chindris Mihai", "Medicament", "16:13");
        Person e3 = new Person("Pop Alexandru", "Medicament", "17:45");
        Person e4 = new Person("Moldovan Alin", "Medicament", "18:15");

        ArrayList<Person> eventList = new ArrayList<>();
        eventList.add(e1);
        eventList.add(e2);
        eventList.add(e3);
        eventList.add(e4);

        ArrayList<Person> peopleList = new ArrayList<>();
        peopleList.add(alex);
        peopleList.add(diana);
        peopleList.add(mihai);
        peopleList.add(dan);
        peopleList.add(alin);
        peopleList.add(andrei);



        PersonListAdapter adapter = new PersonListAdapter(this, R.layout.list_layout, peopleList);
        PersonListAdapter adapter2 = new PersonListAdapter(this, R.layout.list_layout, eventList);

        listview2.setAdapter(adapter2);
        listview.setAdapter(adapter);

        listview.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapter, View view, int position, long id) {

                Toast toast = Toast.makeText(getApplicationContext(), "" + adapter.getItemIdAtPosition(position) , Toast.LENGTH_SHORT);
                toast.show();
            }
        });
        call.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                Toast toast = Toast.makeText(getApplicationContext(), "Calling..", Toast.LENGTH_SHORT);
                toast.show();
            }
        });

        endcall.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast toast = Toast.makeText(getApplicationContext(), "End Call..", Toast.LENGTH_SHORT);
                toast.show();
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
