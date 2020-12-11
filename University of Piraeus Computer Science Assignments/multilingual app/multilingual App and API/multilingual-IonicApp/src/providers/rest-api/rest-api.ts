import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Platform } from 'ionic-angular';
import { LoadingProvider } from '../../providers/loading/loading';
import { NetworkProvider } from '../../providers/network/network';
import { SettingsProvider } from '../../providers/settings/settings';
import { Injectable } from '@angular/core';
import { AlertProvider } from '../../providers/alert/alert';
@Injectable()
export class RestApiProvider {

  //TODO :change to prod url
  apiurl: string = "http://localhost:3000/api/v1/ "
  // apiurl: string = ""

  constructor(public loadingProv: LoadingProvider,public networkProv: NetworkProvider, public platform: Platform, public http: HttpClient, public alertProv: AlertProvider, public settings: SettingsProvider) {
  }

  handleError(err) {
    err = err.error
    return err
  }

  authorise(auth) {
    return new Promise((resolve, reject) => {
      if (auth) {
            this.settings.get('token').then((token: string) => {
              resolve(new HttpHeaders({ 'Authorization': 'Bearer ' + token }))
            }).catch(err => {
              reject(err)
            })

      }
      else {
        resolve(new HttpHeaders())
      }
    })

  }

  get(url, params, needAuth = true, extraHeaders = {}, needLoading = true, showErr = true) {

    let loading
    if (needLoading) {
      loading = this.loadingProv.create()
      loading.present()
    }

    return new Promise((resolve, reject) => {
      this.networkProv.networkReady(showErr).then(() => {

        this.authorise(needAuth).then((heads: HttpHeaders) => {
          if (Array.isArray(extraHeaders)) {
            extraHeaders.forEach(function (head) {
              let prop = Object.keys(head)[0]
              let val = head[prop]
              heads = heads.set(prop, val);
            });
          }

          let queryParams = new HttpParams()

          if (Array.isArray(params)) {
            params.forEach(function (param) {
              let paramName = Object.keys(param)[0]
              let paramVal = param[paramName]
              queryParams = queryParams.append(paramName, paramVal);
            });
          }
          this.http.get(url, { headers: heads, params: queryParams }).subscribe(data => {
            if (needLoading) {
              loading.dismiss();
            }
            resolve(data)
          }, err => {
            if (needLoading) {
              loading.dismiss();
            }
            console.log('api error')
            reject(err)
          })
        }).catch(err => {
          reject(err)
        })

      }).catch((err) => {
        if (needLoading) {
          loading.dismiss();
        }
        reject(err)
      })
    })

  }

  post(handleErr, url, data, needAuth = true, extraHeaders = {}, showErr = true) {

    let loading = this.loadingProv.create()
    loading.present()

    return new Promise((resolve, reject) => {

      this.networkProv.networkReady(showErr).then(() => {

        this.authorise(needAuth).then((heads: HttpHeaders) => {

          if (Array.isArray(extraHeaders)) {
            let needFormData = false
            extraHeaders.forEach(function (head) {
              let prop = Object.keys(head)[0]
              let val = head[prop]
              if (val.includes("x-www-form-urlencoded")) {
                needFormData = true
              }
              heads = heads.set(prop, val);
            });
            if (needFormData) {

              //Transform json to form data
              let form_data = ""

              for (var key in data) {
                if (data.hasOwnProperty(key)) {
                  form_data += key + "=" + data[key] + '&'
                }
              }
              form_data = form_data.slice(0, -1)
              data = form_data
            }
          }

          this.http.post(url, data, { headers: heads }).toPromise().then((resp) => {
            loading.dismiss();
            console.log('resp')
            console.log(resp)
            resolve(resp)
          }).catch((err) => {
            loading.dismiss();
            resolve(err.error.text)
          })
        })
      })
    })
  }
}