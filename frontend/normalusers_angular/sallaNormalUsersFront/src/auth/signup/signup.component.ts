import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent {

  registrationForm = this.fb.group({
    firstName: ['', Validators.required],
    lastName: ['', Validators.required],
    email: ['', Validators.required],
    TwoStepVerficationEmail: [false],
    password: ['', Validators.required],
    confirmPassword: ['', Validators.required],
    mobilePhone: [''],
    TwoStepVerficationMobile: [''],
    birthDate: ['', Validators.required],
  });
  constructor(private fb: FormBuilder){}

  ngOnInit(){
   console.log(this.registrationForm)
  }



}
