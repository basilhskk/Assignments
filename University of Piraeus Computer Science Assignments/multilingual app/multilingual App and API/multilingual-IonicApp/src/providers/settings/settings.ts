import { NativeStorage } from '@ionic-native/native-storage';
import { Platform } from 'ionic-angular/platform/platform';
import { Injectable } from '@angular/core';

@Injectable()
export class SettingsProvider {


  constructor(public nativeStorage: NativeStorage, public platform: Platform) {
    console.log('Hello UserSettingsProvider Provider');
  }

  get(val) {

    return new Promise((resolve, reject) => {

      if (this.platform.is('cordova')) {
        this.platform.ready().then(() => {

          this.nativeStorage.getItem(val).then(data => {
            resolve(data)
          }).catch(err => {
            this.nativeStorage.setItem(val, "").then(() => {
              resolve("")
            });
          })
        })

      }
      else {
        console.log('cordova not available ...');
        reject('cordova not available')
      }
    })

  }

  set(property, val) {

    return new Promise((resolve, reject) => {

      if (this.platform.is('cordova')) {
        this.platform.ready().then(() => {
          this.nativeStorage.setItem(property, val).then(() => {
            resolve()
          }).catch(() => {
          })
        })
      }
      else {
        console.log('cordova not available ...');
        reject('cordova not available')
      }
    })

  }


}
