import { Injectable } from '@angular/core';
import { AlertProvider } from '../../providers/alert/alert';

var validate = require("validate-js/validate.js");

@Injectable()
export class ValidateProvider {

  params = {}
  errors = {}
  constraints = {}

  constructor(public alertProvider: AlertProvider) {
    console.log('Hello ValidateProvider Provider');
  }

  clearError(prop) {
    this.errors[prop] = false;
  }

  hasError(prop) {
    if (this.errors[prop]) {
      return true
    }
    else {
      return false
    }
  }

  validateData() {

    return new Promise((resolve, reject) => {

      //clear errors
      this.errors = {}

      let validationResult = validate(this.params, this.constraints, {
        fullMessages: false
      })


      if (validationResult) {

        let firstKey = Object.keys(validationResult)[0]

        let firstVal = validationResult[firstKey][0]

        this.errors[firstKey] = firstVal;

        this.alertProvider.showError(firstVal, () => {

        })
        reject()

      }
      else {
        resolve()
      }

    })

  }

}
