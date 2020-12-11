import { Injectable } from '@angular/core';
import { Platform } from 'ionic-angular';
import { AlertProvider } from '../../providers/alert/alert';
import { Network } from '@ionic-native/network';

@Injectable()
export class NetworkProvider {

  constructor(public alertProv: AlertProvider, public platform: Platform, public network: Network) {
    console.log('Hello NetworkProvider Provider');
  }


  networkReady(showError) {

    return new Promise((resolve, reject) => {
      this.platform.ready().then(() => {
        if (this.network.type == 'none') {
          if (showError) {
            this.alertProv.showError("Please connect to the internet and try again.", () => {
              reject("noNetwork")
            });
          } else {
            reject("noNetwork")
          }
        }
        else {
          resolve()
        }
      })
    })
  }

}
