package me.vkoutsokostas.recomenderMusic;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.cardview.widget.CardView;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.DocumentSnapshot;
import com.google.firebase.firestore.EventListener;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.FirebaseFirestoreException;

public class Areas extends AppCompatActivity {
    CardView myAreas,setNew;
    String dbObject = "none";
    FirebaseFirestore fstore;
    FirebaseAuth fAuth;
    String userID;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_areas);
        myAreas = findViewById(R.id.myAreas);
        setNew = findViewById(R.id.setNew);
        fAuth = FirebaseAuth.getInstance();
        fstore = FirebaseFirestore.getInstance();
        userID = fAuth.getCurrentUser().getUid();

        final DocumentReference documentReference = fstore.collection("users").document(userID).collection("areas").document("areas");
        documentReference.addSnapshotListener(Areas.this, new EventListener<DocumentSnapshot>() {
            @Override
            public void onEvent(@Nullable DocumentSnapshot value, @Nullable FirebaseFirestoreException error) {
                try {
                    dbObject = value.getString("areas");

                } catch (Throwable t) {
                    Toast.makeText(Areas.this, R.string.apiError, Toast.LENGTH_SHORT).show();
                }

            }
        });

        myAreas.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(getApplicationContext(),MyAreas.class);
                if(dbObject==null) dbObject="none";
                intent.putExtra("object", dbObject.toString());
                startActivity(intent);
            }
        });

        setNew.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(getApplicationContext(),SetArea.class);
                if(dbObject==null) dbObject="none";
                intent.putExtra("object", dbObject);
                startActivity(intent);


            }
        });
    }
}