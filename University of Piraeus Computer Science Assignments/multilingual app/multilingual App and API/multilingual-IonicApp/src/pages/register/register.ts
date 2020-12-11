import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import {ApiProvider} from '../../providers/api/api'
import {SettingsProvider} from '../../providers/settings/settings'
import {AlertProvider} from '../../providers/alert/alert'


@IonicPage()
@Component({
  selector: 'page-register',
  templateUrl: 'register.html',
})
export class RegisterPage {
  public form;
  constructor(public navCtrl: NavController, public navParams: NavParams,public api: ApiProvider,public settings:SettingsProvider,public alert:AlertProvider) {
    this.form = {}
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad RegisterPage');
  }
  register(){

    let regex = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if(regex.test(this.form.email)) {
    
      if(this.form.password === this.form.password2){
    
        this.api.register(this.form).then((data:any)=>{
        
          if (data.token){
        this.settings.set('token',data.token).then(()=>{
        this.navCtrl.setRoot('TabsPage')
        }).catch(()=>{})
        }else{
          this.alert.showError('Υπάρχει ήδη χρήστης με αυτό το email ή username',()=>{})
        }
        }).catch(()=>{})

      }else{

        this.alert.showError('Παρακαλώ εισάγεται ίδιους κωδικούς.',()=>{})
      }
      }else{

        this.alert.showError('Παρακαλώ εισάγεται έγκυρο e-mail.',()=>{})
        
      }


  }

  open(page){
    this.navCtrl.push(page)
  }

}
