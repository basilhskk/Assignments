import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import {ApiProvider} from '../../providers/api/api'
import {SettingsProvider} from '../../providers/settings/settings'
import {AlertProvider} from '../../providers/alert/alert'
@IonicPage()
@Component({
  selector: 'page-login',
  templateUrl: 'login.html',
})
export class LoginPage {
  public uname;
  public password;

  constructor(public navCtrl: NavController, public navParams: NavParams, public api: ApiProvider,public settings:SettingsProvider,public alertProv:AlertProvider) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad LoginPage');
  }

  login(){
     
    this.api.login(this.uname,this.password).then((data:any)=>{
 
      if (data.token){
      this.settings.set('token',data.token).then(()=>{
        
        this.navCtrl.setRoot('TabsPage')

      }).catch(()=>{

      })}else{
        this.alertProv.showError('Λάθος Κωδικός/Email',()=>{})
      }
    }).catch(()=>{

    })
  }
  
  open(page){
    this.navCtrl.push(page)
  }

}
