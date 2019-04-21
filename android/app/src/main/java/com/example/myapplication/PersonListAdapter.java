package com.example.myapplication;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import java.util.ArrayList;

public class PersonListAdapter extends ArrayAdapter<Person> {

    private static final String TAG = "PersonListAdapter";
    private  Context mContext;
    int mResource;

    public PersonListAdapter(Context context, int resource, ArrayList<Person> objects) {
        super(context, resource, objects);
        mContext = context;
        mResource = resource;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {

        String name = getItem(position).getName();
        String birthday = getItem(position).getBirthday();
        String sex = getItem(position).getSex();

        Person person = new Person(name, birthday, sex);

        LayoutInflater inflate = LayoutInflater.from(mContext);
        convertView = inflate.inflate(mResource, parent, false);

        TextView tvName = (TextView) convertView.findViewById(R.id.textView6);
        TextView tvBirthday = (TextView) convertView.findViewById(R.id.textView7);
        TextView tvSex = (TextView) convertView.findViewById(R.id.textView8);

        tvName.setText(name);
        tvBirthday.setText(birthday);
        tvSex.setText(sex);

        return convertView;
    }
}
