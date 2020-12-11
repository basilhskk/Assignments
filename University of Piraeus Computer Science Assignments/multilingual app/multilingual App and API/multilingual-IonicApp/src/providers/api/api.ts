import { Injectable } from '@angular/core';
import { RestApiProvider } from '../../providers/rest-api/rest-api'
import { AlertProvider } from '../../providers/alert/alert'

@Injectable()
export class ApiProvider {

  baseUrl: string = 'http://192.168.1.7:4445/'

  constructor(public restApi: RestApiProvider, public alert: AlertProvider) {
    console.log('Hello ApiProvider Provider');
  }

  handleError(err) {
    err = err.text
    return err
  }

  login(name, pass) {
    let params = {
      username: name,
      password: pass
    }
    return this.restApi.post(this.handleError, this.baseUrl + 'login', params)
  }

  delete(token) {
    let params = {
      token: token
    }
    return this.restApi.post(this.handleError, this.baseUrl + 'delete', params)
  }

  getUser(token) {
    let params = {
      token: token
    }
    return this.restApi.post(this.handleError, this.baseUrl + 'user', params)
  }

  register(form) {
    let params = {
      username: form.username,
      email: form.email,
      password: form.password
    }
    return this.restApi.post(this.handleError, this.baseUrl + 'register', params)

  }

}
