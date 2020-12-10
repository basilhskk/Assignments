package me.vkoutsokostas.recomenderMusic;

import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;

public class Login extends AppCompatActivity {
    Button login;
    EditText email,passwd;
    TextView registerRdr;
    FirebaseAuth fAuth;
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        login = findViewById(R.id.loginBtn);
        email = findViewById(R.id.email);
        passwd = findViewById(R.id.password);
        registerRdr = findViewById(R.id.registerRdr);
        fAuth = FirebaseAuth.getInstance();


        registerRdr.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(new Intent(getApplicationContext(),Register.class));
            }
        });

        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String mail = email.getText().toString().trim();
                String password = passwd.getText().toString().trim();

                if(TextUtils.isEmpty(mail)){
                    email.setError(getString(R.string.mailErr));
                    return ;
                }

                if(TextUtils.isEmpty(password)){
                    passwd.setError(getString(R.string.passErr));
                    return ;
                }

                fAuth.signInWithEmailAndPassword(mail,password).addOnCompleteListener(new OnCompleteListener<AuthResult>() {
                    @Override
                    public void onComplete(@NonNull Task<AuthResult> task) {
                        if(task.isSuccessful()){
                            Toast.makeText(Login.this,getString(R.string.loginToast),Toast.LENGTH_SHORT).show();
                            startActivity(new Intent(Login.this,MainActivity.class));
                        }else{
                            Toast.makeText(Login.this,getString(R.string.validateErr),Toast.LENGTH_SHORT).show();
                        }
                    }
                });
            }
        });
    }

}