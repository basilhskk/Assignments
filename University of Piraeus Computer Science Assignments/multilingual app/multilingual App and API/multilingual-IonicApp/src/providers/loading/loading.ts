import { Injectable } from '@angular/core';
import { LoadingController } from 'ionic-angular';

@Injectable()
export class LoadingProvider {

  waitText: string = "Παρακαλώ Περιμένετε..."

  constructor(public loadingCtrl: LoadingController) {
    console.log('Hello LoadingProvider Provider');
  }

  create() {
    return this.loadingCtrl.create({
      content: this.waitText
    });
  }

}
