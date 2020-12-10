package me.vkoutsokostas.recomenderMusic;

import android.os.Bundle;
import android.text.method.LinkMovementMethod;
import android.util.Log;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.Random;

public class regionRecommendations extends AppCompatActivity {
    TextView artist,track,duration,url;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_region_recommendations);
        String tracks = getIntent().getStringExtra("tracks");

        artist=findViewById(R.id.artist);
        track=findViewById(R.id.musicTitle );
        duration=findViewById(R.id.time);
        url=findViewById(R.id.url);

        try {
            JSONObject obj = new JSONObject(tracks);
            JSONObject obj2 = new JSONObject(obj.getJSONObject("tracks").toString());
            JSONArray allTracks = obj2.getJSONArray("track");
            Random rand = new Random();
            JSONObject A = allTracks.getJSONObject(rand.nextInt(allTracks.length()));

            track.setText(A.getString("name").toString());
            url.setText(A.getString("url").toString());
            url.setMovementMethod(LinkMovementMethod.getInstance());
            duration.setText(A.getString("duration").toString()+" seconds");
            artist.setText(A.getJSONObject("artist").getString("name").toString());


        } catch (Throwable t) {
            Log.e("My App", "Could not parse malformed JSON: \"" + tracks + "\"");
            Toast.makeText(this,R.string.apiError,Toast.LENGTH_SHORT).show();
        }

    }
}