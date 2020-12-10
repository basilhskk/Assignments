'use strict'

/*
|--------------------------------------------------------------------------
| Routes
|--------------------------------------------------------------------------
|
| Http routes are entry points to your web application. You can create
| routes for different URL's and bind Controller actions to them.
|
| A complete guide on routing is available here.
| http://adonisjs.com/docs/4.1/routing
|
*/

/** @type {typeof import('@adonisjs/framework/src/Route/Manager')} */
const Route = use('Route')


Route.get('logout','Auth/LoginController.logout')

Route.get('register','Auth/RegisterController.show')
Route.post('register', 'Auth/RegisterController.register')


Route.get('login','Auth/LoginController.show')
Route.post('login', 'Auth/LoginController.login')

Route.get('forgot','Auth/LoginController.showForgot')
Route.post('forgot', 'Auth/LoginController.forgot')

Route.get('recover/:key','Auth/LoginController.recover')
Route.post('recover/:key','Auth/LoginController.recoverLogin')

Route.get('/','ProductController.show')

Route.get('/products/:category', 'ProductController.show')
Route.get('/product/:id', 'ProductController.showDetails')
Route.post('/product/checkTest/:id', 'ProductController.checkTest')

Route.get('add-product','ProductController.showAdd')
Route.post('add-product','ProductController.add')

Route.get('/success',(({view})=>{
    return view.render('success')
}))

Route.get('/fail',(({view})=>{
    return view.render('fail')
}))

Route.get('/help',(({view})=>{
    return view.render('faq')
}))