import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DocumentComponent } from './document/document.component';
import { LoginComponent } from './login/login.component';

import { RegisterComponent } from './register/register.component';
const routes: Routes = [
  {path: 'document', component: DocumentComponent},
  {path: 'login', component: LoginComponent},
  {path: 'register', component: RegisterComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
