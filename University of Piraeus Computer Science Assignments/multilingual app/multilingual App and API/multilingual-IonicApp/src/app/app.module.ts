import { NgModule, ErrorHandler } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { IonicApp, IonicModule, IonicErrorHandler } from 'ionic-angular';
import { HttpClientModule } from '@angular/common/http';

import { MyApp } from './app.component';

import { Network } from '@ionic-native/network';
import { NativeStorage } from '@ionic-native/native-storage';

import { ContactPage } from '../pages/contact/contact';
import { HomePage } from '../pages/home/home';
import { TabsPage } from '../pages/tabs/tabs';
import {ExercisesPage} from '../pages/exercises/exercises'

import { StatusBar } from '@ionic-native/status-bar';
import { SplashScreen } from '@ionic-native/splash-screen';
import { AlertProvider } from '../providers/alert/alert';
import { ApiProvider } from '../providers/api/api';
import { LoadingProvider } from '../providers/loading/loading';
import { NetworkProvider } from '../providers/network/network';
import { RestApiProvider } from '../providers/rest-api/rest-api';
import { SettingsProvider } from '../providers/settings/settings';
import { ValidateProvider } from '../providers/validate/validate';

@NgModule({
  declarations: [
    MyApp,
    ContactPage,
    ExercisesPage,
    HomePage
  ],
  imports: [
    BrowserModule,
    IonicModule.forRoot(MyApp),
    HttpClientModule
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    ContactPage,
    HomePage,
    ExercisesPage
  ],
  providers: [
    StatusBar,
    SplashScreen,
    Network,
    NativeStorage,
    {provide: ErrorHandler, useClass: IonicErrorHandler},
    AlertProvider,
    ApiProvider,
    LoadingProvider,
    NetworkProvider,
    RestApiProvider,
    SettingsProvider,
    ValidateProvider
  ]
})
export class AppModule {}
