package me.vkoutsokostas.recomenderMusic;

import android.os.Bundle;
import android.util.Log;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class MyAreas extends AppCompatActivity {
    String object;
    ListView areaList;
    List<String> locations = new ArrayList<String>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_my_areas);
        object = getIntent().getStringExtra("object");
        areaList = findViewById(R.id.areaList);

        if (object.equals("none")) {
            Toast.makeText(getBaseContext(),R.string.zeroAreas,Toast.LENGTH_LONG).show();
            finish();
        }else{

        try{
            JSONObject obj = new JSONObject(object);
            JSONArray array = obj.getJSONArray("areas");
            JSONObject obj1;

            String a;
            for(int i = 0; array.length()>i;i++){
                obj1 = (JSONObject) array.get(i);
                a = obj1.getString("location");
                locations.add("Location: "+a+"\n\nGenres: "+ obj1.getString("tags"));
            }
//            Log.e("ASdasdfsdfsdfsdf",a.toString());

            ArrayAdapter<String> arrayAdapter = new ArrayAdapter<String>(this, R.layout.activity_clistview, R.id.textView, locations);
            areaList.setAdapter(arrayAdapter);

        }catch (JSONException e){
            Log.e("asdasdasd",e.toString());

        }

        }


    }
}