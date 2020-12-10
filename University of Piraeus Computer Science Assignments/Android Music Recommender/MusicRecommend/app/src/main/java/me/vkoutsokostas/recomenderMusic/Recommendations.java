package me.vkoutsokostas.recomenderMusic;

import android.os.Bundle;
import android.text.method.LinkMovementMethod;
import android.util.Log;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.Random;

public class Recommendations extends AppCompatActivity {
    TextView artist,track,duration,url;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_recommendations);
        artist=findViewById(R.id.artist);
        track=findViewById(R.id.musicTitle );
        duration=findViewById(R.id.time);
        url=findViewById(R.id.url);

        String songs = getIntent().getStringExtra("songs");

        try{
            Random rand = new Random();
            JSONObject obj = new JSONObject(songs);
            JSONArray songsArray = obj.getJSONObject("tracks").getJSONArray("track");
            JSONObject randSong = (JSONObject) songsArray.get(rand.nextInt(songsArray.length()));

            track.setText(randSong.getString("name").toString());
            url.setText(randSong.getString("url").toString());
            url.setMovementMethod(LinkMovementMethod.getInstance());
            duration.setText(randSong.getString("duration").toString()+" seconds");
            artist.setText(randSong.getJSONObject("artist").getString("name").toString());
        }catch (JSONException e){
            Log.e("asdasd",e.toString());
        }

    }
}