import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { ReactiveFormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DocumentComponent } from './document/document.component';
import { MaterialModule } from './material/material.module';
import { HttpClientModule,HTTP_INTERCEPTORS }    from '@angular/common/http';
import { TokenInterceptorService } from './token-interceptor.service'
@NgModule({
  declarations: [
    AppComponent,
    DocumentComponent,
    
  ],
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    HttpClientModule,
    AppRoutingModule,
    MaterialModule
  ],
  providers: [{
    provide: HTTP_INTERCEPTORS,
    useClass: TokenInterceptorService,
    multi: true
  }],
  bootstrap: [AppComponent]
})
export class AppModule { }
