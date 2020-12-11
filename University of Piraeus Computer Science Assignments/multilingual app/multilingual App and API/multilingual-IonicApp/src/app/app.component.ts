import { Component } from '@angular/core';
import { Platform} from 'ionic-angular';
import { StatusBar } from '@ionic-native/status-bar';
import { SplashScreen } from '@ionic-native/splash-screen';
import {SettingsProvider} from '../providers/settings/settings'
@Component({
  templateUrl: 'app.html'
})

export class MyApp {
  rootPage:any ='LoginPage';

  constructor(platform: Platform, statusBar: StatusBar, splashScreen: SplashScreen,settings:SettingsProvider) {
    platform.ready().then(() => {
      statusBar.styleDefault();
      splashScreen.hide();
      settings.get('token').then(data=>{
        if(data!=""){
          this.rootPage='TabsPage'
        }
  
      }).catch(err=>{console.log(err)})
    });

  }
  
}
