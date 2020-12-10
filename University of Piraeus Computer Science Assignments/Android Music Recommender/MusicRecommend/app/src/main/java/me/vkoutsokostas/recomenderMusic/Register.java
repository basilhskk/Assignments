package me.vkoutsokostas.recomenderMusic;

import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.FirebaseFirestore;

import java.util.HashMap;
import java.util.Map;

public class Register extends AppCompatActivity {
    EditText username,passwd,email;
    Button registerBtn;
    TextView loginRdr;
    FirebaseAuth fAuth;
    ProgressBar pbar;
    FirebaseFirestore fstore;
    String userID;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
        username = findViewById(R.id.uname);
        passwd = findViewById(R.id.password);
        email = findViewById(R.id.email);
        registerBtn = findViewById(R.id.loginBtn);
        loginRdr = findViewById(R.id.registerRdr);

        loginRdr.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(new Intent(getApplicationContext(),Login.class));
            }
        });

        fAuth = FirebaseAuth.getInstance();
        fstore = FirebaseFirestore.getInstance();

        if(fAuth.getCurrentUser()!= null){
            startActivity(new Intent(getApplicationContext(),MainActivity.class));
            finish();
        }


        registerBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                final String mail = email.getText().toString().trim();
                final String uname = username.getText().toString().trim();
                String password = passwd.getText().toString().trim();

                if(TextUtils.isEmpty(uname)){
                    username.setError(getString(R.string.unameErr));
                    return ;
                }

                if(TextUtils.isEmpty(mail)){
                    email.setError(getString(R.string.mailErr));
                    return ;
                }

                if(TextUtils.isEmpty(password)){
                    passwd.setError(getString(R.string.passErr));
                    return ;
                }

                if(password.length() < 6){
                    passwd.setError(getString(R.string.passErrLength));
                    return ;
                }

                fAuth.createUserWithEmailAndPassword(mail,password).addOnCompleteListener(new OnCompleteListener<AuthResult>() {
                    @Override
                    public void onComplete(@NonNull Task<AuthResult> task) {
                        if(task.isSuccessful()){
                            Toast.makeText(Register.this,getString(R.string.registerToast),Toast.LENGTH_SHORT).show();
                            userID = fAuth.getCurrentUser().getUid();
                            DocumentReference documentReference = fstore.collection("users").document(userID);
                            Map<String , Object> user = new HashMap<>();
                            user.put("uName", uname);
                            user.put("email",mail);
                            documentReference.set(user).addOnSuccessListener(new OnSuccessListener<Void>() {
                                @Override
                                public void onSuccess(Void aVoid) {
                                    Log.e("onSuccess:","user profiles is created"+ userID);
                                    startActivity(new Intent(getApplicationContext(),MainActivity.class));
                                }
                            }).addOnFailureListener(new OnFailureListener() {
                                @Override
                                public void onFailure(@NonNull Exception e) {
                                    Log.e("onFailure :",e.toString());
                                }
                            });
                        }else{
                            Toast.makeText(Register.this,getString(R.string.err)+task.getException().getMessage(),Toast.LENGTH_SHORT).show();
                        }
                    }
                });

            }
        });
    }
}