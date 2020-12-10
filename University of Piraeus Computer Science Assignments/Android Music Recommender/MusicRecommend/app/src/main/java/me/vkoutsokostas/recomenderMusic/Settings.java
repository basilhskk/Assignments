package me.vkoutsokostas.recomenderMusic;

import android.content.Intent;
import android.content.SharedPreferences;
import android.content.res.Configuration;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.Spinner;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.google.firebase.auth.FirebaseAuth;

import java.util.Locale;

public class Settings extends AppCompatActivity {
    Spinner lang;
    TextView Language;
    Button logout;
    Integer counter = 0;

    protected void onCreate(Bundle savedInstanceState)  {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_settings);
        final String[] languageToLoad = {"en"}; // your language


        lang = findViewById(R.id.spinner);
        ArrayAdapter<String> myAdapter = new ArrayAdapter<>(getApplicationContext(),android.R.layout.simple_list_item_1,getResources().getStringArray(R.array.langs));
        myAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        lang.setAdapter(myAdapter);


        lang.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
           @Override
           public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
               // Get the spinner selected item text
               if(counter>0){
                   String loc = lang.getSelectedItem().toString();

                   final String anguageToLoad= "";
                   if(loc.equals("Greek")){
                        languageToLoad[0] = "el"; // your language

                   }else{
                        languageToLoad[0] = "en"; // your language

                   }

                   Locale locale = new Locale(languageToLoad[0]);
                   Locale.setDefault(locale);
                   Configuration config = new Configuration();
                   config.locale = locale;
                   getBaseContext().getResources().updateConfiguration(config, getBaseContext().getResources().getDisplayMetrics());

                   SharedPreferences languagepref = getSharedPreferences("language",MODE_PRIVATE);
                   SharedPreferences.Editor editor = languagepref.edit();
                   editor.putString("languageToLoad",languageToLoad[0] );
                   editor.commit();

                   Intent intent = new Intent(getApplicationContext(),MainActivity.class);
                   intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);

                   startActivity(intent);


               }
               counter++;
           }
           @Override
           public void onNothingSelected(AdapterView<?> adapterView) {

           }
           });

        logout = findViewById(R.id.logout);

        logout.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                FirebaseAuth.getInstance().signOut();
                startActivity(new Intent(getApplicationContext(),Login.class));
            }
        });
    }


}

