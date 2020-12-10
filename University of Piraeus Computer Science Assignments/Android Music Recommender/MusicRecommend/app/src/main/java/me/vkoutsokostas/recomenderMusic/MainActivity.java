package me.vkoutsokostas.recomenderMusic;

import android.Manifest;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.content.res.Configuration;
import android.location.Address;
import android.location.Geocoder;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Build;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.cardview.widget.CardView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.annotations.Nullable;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.DocumentSnapshot;
import com.google.firebase.firestore.EventListener;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.FirebaseFirestoreException;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.util.List;
import java.util.Locale;
import java.util.Random;

// implements LocationListener
public class MainActivity extends AppCompatActivity implements LocationListener {

    TextView uname, uid;
    FirebaseAuth fAuth;
    FirebaseFirestore fstore;
    String userID, country;
    CardView areas, recomms, regionRecomm, settings;
    LocationManager locationManager;
    String dbObject = "none";
    JSONObject data;
    JSONArray areaList;
    double longtitude, latitude;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        SharedPreferences languagepref = getSharedPreferences("language",MODE_PRIVATE);
        String loc = languagepref.getString("languageToLoad","en") ;
        Log.e("LAGGNGNGN",loc);
        if(loc.equals("el")){
            Locale locale = new Locale(loc);
            Locale.setDefault(locale);
            Configuration config = new Configuration();
            config.locale = locale;
            getBaseContext().getResources().updateConfiguration(config, getBaseContext().getResources().getDisplayMetrics());
        }
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        locationManager = (LocationManager) this.getSystemService(Context.LOCATION_SERVICE);
        if(Build.VERSION.SDK_INT>= Build.VERSION_CODES.M && checkSelfPermission(Manifest.permission.ACCESS_FINE_LOCATION)!= PackageManager.PERMISSION_GRANTED) {
            requestPermissions(new String[]{Manifest.permission.ACCESS_FINE_LOCATION}, 1000);
        }else{
            Location location = locationManager.getLastKnownLocation(locationManager.GPS_PROVIDER);
            onLocationChanged(location);
        }

        uname = findViewById(R.id.user_name);
        uid = findViewById(R.id.user_id);
        areas = findViewById(R.id.areas);
        settings = findViewById(R.id.settings);
        regionRecomm = findViewById(R.id.regionRecomm);
        recomms = findViewById(R.id.recomm);


        try{
            fAuth = FirebaseAuth.getInstance();
            fstore = FirebaseFirestore.getInstance();
            userID = fAuth.getCurrentUser().getUid();

        }catch (Exception e){
            Log.e("Asdasda",e.toString());
        }


        final DocumentReference documentReference = fstore.collection("users").document(userID).collection("areas").document("areas");
        documentReference.addSnapshotListener(MainActivity.this, new EventListener<DocumentSnapshot>() {
            @Override
            public void onEvent(@Nullable DocumentSnapshot value, @Nullable FirebaseFirestoreException error) {
                try {
                    dbObject = value.getString("areas");
                    areaList= null;
                    if (dbObject != null) {
                        try {
                            data = new JSONObject(dbObject);
                            areaList = data.getJSONArray("areas");

                        } catch (JSONException e) {
                            Log.e("json Error", e.toString());
                        }
                    }

                } catch (Throwable t) {
                    Toast.makeText(MainActivity.this, R.string.apiError, Toast.LENGTH_SHORT).show();
                }

            }
        });


        areas.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(new Intent(getApplicationContext(), Areas.class));
            }
        });

        recomms.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String randTag="" ;
                String loc ="";
                if(Build.VERSION.SDK_INT>= Build.VERSION_CODES.M && checkSelfPermission(Manifest.permission.ACCESS_FINE_LOCATION)!= PackageManager.PERMISSION_GRANTED){
                    requestPermissions(new String[]{Manifest.permission.ACCESS_FINE_LOCATION},1000);
                }else{
                    if(areaList!=null){
                        try {
                            Random rand = new Random();
                            JSONObject A = areaList.getJSONObject(rand.nextInt(areaList.length()));
                            String[] randTags = A.getString("tags").split(",");
                            randTag = randTags[rand.nextInt(randTags.length)];
                            loc = A.getString("location");

                        }catch (JSONException e){

                        }

                        Geocoder coder = new Geocoder(MainActivity.this);
                        double distance=100;
                        double nowlat,nowlng;
                        try {
                            List<Address> addressList = coder.getFromLocationName(loc, 1);
                            if (addressList != null && addressList.size() > 0) {
                                double lat = addressList.get(0).getLatitude();
                                double lng = addressList.get(0).getLongitude();

                                if(latitude!=0 || longtitude !=0){

                                    distance =distance(lat,lng,latitude,longtitude);

                                }else{
                                    distance = 100;
                                    Toast.makeText(MainActivity.this,R.string.locationError,Toast.LENGTH_SHORT).show();
                                }

                                Log.e("Asdasda",Double.toString(distance));


                            }

                        } catch (Exception e) {
                            e.printStackTrace();

                        }

                        if(distance<0.6){


                            String URL = "https://ws.audioscrobbler.com/2.0/?method=";
                            String lastFMkey= BuildConfig.ApiKey;
                            String method = "tag.gettoptracks&tag="+randTag;
                            String apiKey = "&api_key="+lastFMkey;
                            String format = "&format=json";
                            StringBuilder url = new StringBuilder(URL).append(method).append(apiKey).append(format);


                            RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
                            JsonObjectRequest objectRequest = new JsonObjectRequest(Request.Method.GET, url.toString(),null, new Response.Listener<JSONObject>(){
                                @Override
                                public void onResponse(JSONObject response){
                                    Intent intent = new Intent(getApplicationContext(),Recommendations.class);
                                    intent.putExtra("songs", response.toString());
                                    startActivity(intent);
                                }
                            },
                                    new Response.ErrorListener() {
                                        @Override
                                        public void onErrorResponse(VolleyError error){
                                            Log.e("Rest Error",error.toString());
                                        }
                                    });

                            requestQueue.add(objectRequest);
                        }else{
                            Toast.makeText(getBaseContext(),R.string.farAwayFromAreas,Toast.LENGTH_SHORT).show();
                        }
                    }else{
                        Toast.makeText(getBaseContext(), R.string.areaError, Toast.LENGTH_LONG).show();
                    }
                }


            }
        });


        regionRecomm.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(Build.VERSION.SDK_INT>= Build.VERSION_CODES.M && checkSelfPermission(Manifest.permission.ACCESS_FINE_LOCATION)!= PackageManager.PERMISSION_GRANTED){
                    requestPermissions(new String[]{Manifest.permission.ACCESS_FINE_LOCATION},1000);
                }else{
                    country = getRegion();
                    String URL = "https://ws.audioscrobbler.com/2.0/?method=";
                    String lastFMkey= BuildConfig.ApiKey;
                    String method = "geo.gettoptracks&country="+country+"&";
                    String apiKey = "api_key="+lastFMkey;
                    String format = "&format=json";
                    StringBuilder url = new StringBuilder(URL).append(method).append(apiKey).append(format);


                    RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
                    JsonObjectRequest objectRequest = new JsonObjectRequest(Request.Method.GET, url.toString(),null, new Response.Listener<JSONObject>(){
                        @Override
                        public void onResponse(JSONObject response){
                            Log.e("Rest Response",response.toString());
                            Intent intent = new Intent(getApplicationContext(),regionRecommendations.class);
                            intent.putExtra("tracks", response.toString());
                            startActivity(intent);
                        }
                    },
                            new Response.ErrorListener() {
                                @Override
                                public void onErrorResponse(VolleyError error){
                                    Log.e("Rest Error",error.toString());
                                }
                            });

                    requestQueue.add(objectRequest);
                }
//                startActivity(new Intent(getApplicationContext(),regionRecommendations.class));

            }
        });


        settings.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(new Intent(getApplicationContext(),Settings.class));
            }
        });

        fAuth = FirebaseAuth.getInstance();
        fstore = FirebaseFirestore.getInstance();
        userID = fAuth.getCurrentUser().getUid();

        DocumentReference documentReference1 = fstore.collection("users").document(userID);
        documentReference1.addSnapshotListener(this, new EventListener<DocumentSnapshot>() {
            @Override
            public void onEvent(@Nullable DocumentSnapshot value, @Nullable FirebaseFirestoreException error) {
                uname.setText(value.getString("uName"));
            }
        });

    }

    public boolean onCreateOptionsMenu(Menu menu){
        getMenuInflater().inflate(R.menu.dashmenu,menu);
        return true;
    }

    public boolean onOptionsItemSelected(MenuItem item){
        int id = item.getItemId();

        switch (id){
            case R.id.menulogout:
                FirebaseAuth.getInstance().signOut();
                startActivity(new Intent(getApplicationContext(),Login.class));
                finish();
                break;
        }
        return true;
    }


    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        if(requestCode==1000){
            if(grantResults[0]== PackageManager.PERMISSION_GRANTED){
                SharedPreferences sharedPref = getPreferences(Context.MODE_PRIVATE);
                SharedPreferences.Editor editor = sharedPref.edit();
                editor.putBoolean("hasLocation", true);
                editor.commit();

            }else{
                SharedPreferences sharedPref = getPreferences(Context.MODE_PRIVATE);
                SharedPreferences.Editor editor = sharedPref.edit();
                editor.putBoolean("hasLocation", false);
                editor.commit();
                Toast.makeText(getApplicationContext(),"Cant use app without location ",Toast.LENGTH_LONG).show();
            }
        }
    }


    public String getRegion(){
        Geocoder geocoder = new Geocoder(getApplicationContext());
        String country_name = null;
        for(String provider: locationManager.getAllProviders()) {
            @SuppressWarnings("ResourceType") Location location = locationManager.getLastKnownLocation(provider);
            if(location!=null) {
                try {
                    List<Address> addresses = geocoder.getFromLocation(location.getLatitude(), location.getLongitude(), 1);
                    if(addresses != null && addresses.size() > 0) {
                        country_name = addresses.get(0).getCountryName();
                        break;
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
        return country_name;
    }



    private double distance(double lat1, double lng1, double lat2, double lng2) {

        double earthRadius = 6371 ;

        double dLat = Math.toRadians(lat2-lat1);
        double dLng = Math.toRadians(lng2-lng1);

        double sindLat = Math.sin(dLat / 2);
        double sindLng = Math.sin(dLng / 2);

        double a = Math.pow(sindLat, 2) + Math.pow(sindLng, 2)
                * Math.cos(Math.toRadians(lat1)) * Math.cos(Math.toRadians(lat2));

        double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));

        double dist = earthRadius * c;

        return dist;
    }


    @Override
    public void onLocationChanged(@NonNull Location location) {
        latitude = location.getLatitude();
        longtitude = location.getLongitude();
    }
}
