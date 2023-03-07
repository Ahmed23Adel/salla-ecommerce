import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {
  loginForm = this.fb.group({
    email: ['', [Validators.required]],
    password: ['', Validators.required],
  });
  get email(){
    return this.loginForm.get("email")
  }

  get password(){
    return this.loginForm.get("password")
  }
    
  constructor(private fb: FormBuilder){}


}
