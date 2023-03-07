import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthComponent } from 'src/auth/auth.component';
import { AuthModule } from 'src/auth/auth.module';
import { LoginComponent } from 'src/auth/login/login.component';
import { SignupComponent } from 'src/auth/signup/signup.component';
import { TstComponent } from './tst/tst.component';

const routes: Routes = [
  {path: 'tst', component: TstComponent},
  {path: 'auth', component: AuthComponent, children:[
    {path: 'signup', component: SignupComponent},
    {path: 'login', component: LoginComponent}
  ]}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
