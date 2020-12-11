import { Injectable } from '@angular/core';
import { AlertController } from 'ionic-angular';

@Injectable()
export class AlertProvider {

  errorTitle: string = "Σφάλμα !"
  helpTitle: string = "Βοήθεια !"
  successTitle: string = "Επιτυχία !"
  constructor(public alertCtrl: AlertController) {
    console.log('Hello AlertProvider Provider');
  }

  showError(msg: string, cb) {
    let alert = this.alertCtrl.create({
      title: this.errorTitle,
      subTitle: msg,
      buttons: [{
        text: 'Ok',
        handler: () => {
          return cb('ok')
        }
      }]
    });
    alert.present();
  }
  showHelp(msg: string, cb) {
    let alert = this.alertCtrl.create({
      title: this.helpTitle,
      subTitle: msg,
      buttons: [{
        text: 'Ok',
        handler: () => {
          return cb('ok')
        }
      }]
    });
    alert.present();
  }

  showPermision(title, msg, permision, cb) {
    let alert = this.alertCtrl.create({
      title: title,
      subTitle: msg,
      buttons: [{
        text: permision,
        handler: () => {
          return cb('ok')
        }
      }, {
        text: "Άκυρο",
        handler: () => {
          return cb('cancel')
        }
      }]
    });
    alert.present();
  }

  showSuccess(msg: string, cb) {
    let alert = this.alertCtrl.create({
      title: this.successTitle,
      subTitle: msg,
      buttons: [{
        text: 'Ok',
        handler: () => {
          return cb('ok')
        }
      }]
    });
    alert.present();
  }

  showEmailInfo(cb) {
    const prompt = this.alertCtrl.create({
      title: 'Στοιχεία Πελάτη',
      message: "Συμπληρώστε τα στοιχεία",
      inputs: [
        {
          name: "name",
          type: 'text',
          placeholder: 'Όνομα',

        }, {
          name: 'email',
          type: 'email',
          placeholder: 'E-mail',
        },

      ],
      buttons: [
        {
          text: 'Ακύρωση',
          handler: data => {
            return cb('cancel')
          }
        },
        {
          text: 'Αποστολή',
          handler: data => {

            return cb(data)
          }
        }
      ]
    });
    prompt.present();
  }
  showInterest(cb) {
    const prompt = this.alertCtrl.create({
      title: 'Στοιχεία Πελάτη',
      message: "Παρακαλώ συμπληρώστε",
      inputs: [
        {
          name: "name",
          type: 'text',
          placeholder: 'Όνομα',

        }, {
          name: 'email',
          type: 'email',
          placeholder: 'E-mail',
        }, {
          name: 'phone',
          type: 'tel',
          placeholder: 'Τηλέφωνο',
        }

      ],
      buttons: [
        {
          text: 'Ακύρωση',
          handler: data => {
            return cb('cancel')
          }
        },
        {
          text: 'Αποστολή',
          handler: data => {
            console.log('Saved clicked');
            return cb(data)
          }
        }
      ]
    });
    prompt.present();
  }

  paymentSelect(inputs, cb) {
    const prompt = this.alertCtrl.create({
      title: 'Τρόπος Εξόφλησης',
      message: "Παρακαλώ επιλέξτε τρόπο εξόφλησης",
      inputs: inputs,
      buttons: [
        {
          text: 'Ακύρωση',
          handler: data => {
            return cb('cancel')
          }
        },
        {
          text: 'Αποθήκευση',
          handler: data => {
            return cb(data)
          }
        }
      ]
    });
    prompt.present();;
  }

  filterPrompt(inputs, cb) {
    const prompt = this.alertCtrl.create({
      title: 'Ταξινόμηση',
      inputs: inputs,
      buttons: [
        {
          text: 'Ακύρωση',
          handler: data => {
            return cb('cancel')
          }
        },
        {
          text: 'Εφαρμογή',
          handler: data => {
            return cb(data)
          }
        }
      ]
    });
    prompt.present();;
  }
}
