import { Component } from '@angular/core';
import { NavController,App } from 'ionic-angular';
import {SettingsProvider} from '../../providers/settings/settings'
import {ApiProvider} from '../../providers/api/api'
import { AlertProvider } from '../../providers/alert/alert';

@Component({
  selector: 'page-contact',
  templateUrl: 'contact.html'
})
export class ContactPage {
  public user;
  constructor(public navCtrl: NavController,public settings:SettingsProvider,public api: ApiProvider,public app:App,public alertProv:AlertProvider) {
    
    this.user = {
      username:"" 
    }
  }
  
  ionViewDidEnter(){
    console.log('view loaded')
    this.settings.get('token').then(data=>{
      this.api.getUser(data).then(resp=>{
        console.log(resp)
        this.user.username=resp
      }).catch(err=>{console.log(err)})
    }).catch(err=>{
      console.log(err)
    })
  }
  logout(){
    this.settings.set('token','')
    // window.location.reload();
    // this.navCtrl//setRoot('LoginPage')
    this.app.getRootNav().setRoot('LoginPage')
  }

  delete(){
    this.settings.get('token').then(data=>{
      this.api.delete(data).then(()=>{
        this.alertProv.showSuccess('Ο λογαριασμός σας διαγράφηκε με επιτυχία',()=>{
          this.logout()
        })
      }).catch(()=>{
  
      })
    }).catch(err=>{console.log(err)})

  }

}
