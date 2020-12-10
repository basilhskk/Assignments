package me.vkoutsokostas.recomenderMusic;

import android.Manifest;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.location.Address;
import android.location.Geocoder;
import android.location.Location;
import android.location.LocationManager;
import android.os.Build;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.FirebaseFirestore;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class SetArea extends AppCompatActivity {
    Button setTags,setArea,useLocation;
    TextView selectedTags;
    EditText location;
    boolean[] checkedItems;
    String [] listItems;
    ArrayList<Integer> mUserItems = new ArrayList<>();
    LocationManager locationManager;
    FirebaseFirestore fstore;
    FirebaseAuth fAuth;
    String userID;
    JSONArray allAreas = null;
    String object;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_set_area);
        setTags = findViewById(R.id.setTags);
        selectedTags = findViewById(R.id.selectedTags);
        listItems = getResources().getStringArray(R.array.genres);
        locationManager = (LocationManager) this.getSystemService(Context.LOCATION_SERVICE);
        fAuth = FirebaseAuth.getInstance();
        fstore = FirebaseFirestore.getInstance();
        object = getIntent().getStringExtra("object");

        checkedItems = new boolean[listItems.length];
        setArea=findViewById(R.id.setArea);
        useLocation=findViewById(R.id.useLocation);
        location = findViewById(R.id.location);

        String tags = getIntent().getStringExtra("object");


        setTags.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                AlertDialog.Builder mBuilder = new AlertDialog.Builder(SetArea.this);
                mBuilder.setTitle(R.string.tagsTitle);
                mBuilder.setMultiChoiceItems(listItems, checkedItems, new DialogInterface.OnMultiChoiceClickListener() {
                    @Override
                    public void onClick(DialogInterface dialogInterface, int position, boolean isChecked) {

                        if(isChecked){
                            mUserItems.add(position);
                        }else{
                            mUserItems.remove((Integer.valueOf(position)));
                        }
                    }
                });

                mBuilder.setCancelable(false);
                mBuilder.setPositiveButton(R.string.ok, new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialogInterface, int which) {
                        String item = "";
                        for (int i = 0; i < mUserItems.size(); i++) {
                            item = item + listItems[mUserItems.get(i)];
                            if (i != mUserItems.size() - 1) {
                                item = item + ", ";
                            }
                        }
                        selectedTags.setText(item);
                    }
                });

                mBuilder.setNegativeButton(R.string.dismiss, new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialogInterface, int i) {
                        dialogInterface.dismiss();
                    }
                });

                mBuilder.setNeutralButton(R.string.clearAll, new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialogInterface, int which) {
                        for (int i = 0; i < checkedItems.length; i++) {
                            checkedItems[i] = false;
                            mUserItems.clear();
                            selectedTags.setText("");
                        }
                    }
                });

                AlertDialog mDialog = mBuilder.create();
                mDialog.show();
            }
        });


        useLocation.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(Build.VERSION.SDK_INT>= Build.VERSION_CODES.M && checkSelfPermission(Manifest.permission.ACCESS_FINE_LOCATION)!= PackageManager.PERMISSION_GRANTED){
                    requestPermissions(new String[]{Manifest.permission.ACCESS_FINE_LOCATION},1000);
                }else{
                    location.setText(getLocationAddress());
                }
            }
        });

        setArea.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                userID = fAuth.getCurrentUser().getUid();
                String tags = selectedTags.getText().toString();
                String loc = location.getText().toString();
                // this is what to change
                JSONObject obj = null;
                try {
                    if(object.equals("none")){
                        DocumentReference documentReference1 = fstore.collection("users").document(userID).collection("areas").document("areas");
                        Map<String, Object> area = new HashMap<>();
                        String areaObj = "{'location':'" + loc + "','tags':'" + tags + "'}";
                        JSONObject jsobj = new JSONObject(areaObj);
                        area.put("areas", "{\"areas\":["+jsobj.toString()+"]}");

                        documentReference1.set(area).addOnSuccessListener(new OnSuccessListener<Void>() {
                            @Override
                            public void onSuccess(Void aVoid) {
                                Log.e("onSuccess:", "user profiles is created" + userID);
                                Toast.makeText(getBaseContext(),R.string.areaSuccess,Toast.LENGTH_LONG).show();
                                startActivity(new Intent(getApplicationContext(),Areas.class));
                            }
                        }).addOnFailureListener(new OnFailureListener() {
                            @Override
                            public void onFailure(@NonNull Exception e) {
                                Log.e("onFailure :", e.toString());
                            }
                        });
                    }else{

                    obj = new JSONObject(object);

                        allAreas = obj.getJSONArray("areas");

                    JSONObject obj2 = new JSONObject("{\"location\":\"" + loc + "\",\"tags\":\"" + tags + "\"}");
                    allAreas.put(obj2);
                    DocumentReference documentReference1 = fstore.collection("users").document(userID).collection("areas").document("areas");
                    Map<String, Object> area = new HashMap<>();
                    area.put("areas", "{\"areas\":" + allAreas.toString()+"}");

                    documentReference1.set(area).addOnSuccessListener(new OnSuccessListener<Void>() {
                        @Override
                        public void onSuccess(Void aVoid) {
                            Log.e("onSuccess:", "user profiles is created" + userID);
                            Toast.makeText(getBaseContext(),R.string.areaSuccess,Toast.LENGTH_LONG).show();
                            startActivity(new Intent(getApplicationContext(),Areas.class));
                        }
                    }).addOnFailureListener(new OnFailureListener() {
                        @Override
                        public void onFailure(@NonNull Exception e) {
                            Log.e("onFailure :", e.toString());
                        }
                    });}

                } catch (JSONException e) {
                    Log.e("ASDASDASDASDASDADAd",e.toString());

                    e.printStackTrace();
                }




                updateDB();
//

            }

        });
    }

    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        if(requestCode==1000){
            if(grantResults[0]== PackageManager.PERMISSION_GRANTED){
                Toast.makeText(SetArea.this,R.string.locationSuccess,Toast.LENGTH_LONG).show();
            }else{
                Toast.makeText(SetArea.this,R.string.locationError,Toast.LENGTH_LONG).show();
            }
        }
    }

    public String getLocationAddress() {
        String locationAddress = null;
        Geocoder geocoder = new Geocoder(getApplicationContext());
        for(String provider: locationManager.getAllProviders()) {
            @SuppressWarnings("ResourceType") Location location = locationManager.getLastKnownLocation(provider);
            if(location!=null) {
                try {
                    List<Address> addresses = geocoder.getFromLocation(location.getLatitude(), location.getLongitude(), 1);
                    if(addresses != null && addresses.size() > 0) {
                        locationAddress = addresses.get(0).getAddressLine(0);
                        break;
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

        return locationAddress;
    }

    public void updateDB(){

    }
}