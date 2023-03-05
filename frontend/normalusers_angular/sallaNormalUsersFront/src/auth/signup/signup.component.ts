import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { confirmPasswordValidtor, requirePhoneOnAuth } from '../shared/customValidators';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent {

  registrationForm = this.fb.group({
    firstName: ['', [Validators.required, Validators.minLength(5)]],
    lastName: ['', Validators.required],
    email: ['', Validators.required],
    TwoStepVerficationEmail: [false],
    password: ['', Validators.required],
    confirmPassword: ['', Validators.required],
    mobilePhone: [''],
    TwoStepVerficationMobile: [''],
    birthDate: ['', Validators.required],
  },{
    validators:[confirmPasswordValidtor, requirePhoneOnAuth]
  });
  constructor(private fb: FormBuilder){}

  get firstName(){
    return this.registrationForm.get('firstName');
  }

  get lastName(){
    return this.registrationForm.get('lastName');
  }
  get email(){
    return this.registrationForm.get('email');
  }
  get TwoStepVerficationEmail(){
    return this.registrationForm.get('TwoStepVerficationEmail');
  }
  get password(){
    return this.registrationForm.get('password');
  }
  get confirmPassword(){
    return this.registrationForm.get('confirmPassword');
  }
  get mobilePhone(){
    return this.registrationForm.get('mobilePhone');
  }
  get TwoStepVerficationMobile(){
    return this.registrationForm.get('TwoStepVerficationMobile');
  }
  get birthDate(){
    return this.registrationForm.get('birthDate');
  }

  
  ngOnInit(){
   console.log(this.registrationForm)
  }



}
