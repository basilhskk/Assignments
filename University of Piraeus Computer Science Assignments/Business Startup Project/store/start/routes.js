'use strict'



/** @type {typeof import('@adonisjs/framework/src/Route/Manager')} */
const Route = use('Route')


Route.get('logout','Auth/LoginController.logout').middleware(['cauth'])

Route.get('register','Auth/RegisterController.show')
Route.post('register', 'Auth/RegisterController.register')


Route.get('login','Auth/LoginController.show')
Route.post('login', 'Auth/LoginController.login')

Route.get('forgot','Auth/LoginController.showForgot')
Route.post('forgot', 'Auth/LoginController.forgot')

Route.get('recover/:key','Auth/LoginController.recover')
Route.post('recover/:key','Auth/LoginController.recoverLogin')

Route.get('/','ProductController.show').middleware(['cauth'])

Route.get('/products/:category', 'ProductController.show').middleware(['cauth'])
Route.get('/product/:id', 'ProductController.showDetails').middleware(['cauth'])
Route.post('/product/checkTest', 'ProductController.checkTest').middleware(['cauth'])

Route.get('add-product/:id?','ProductController.showAdd').middleware(['cauth'])
Route.post('add-product','ProductController.add').middleware(['cauth'])

Route.get('/buy/:id?','ProductController.showBuy').middleware(['cauth'])

Route.get('/coupon/:id?','ProductController.showCoupon').middleware(['cauth'])

Route.post('/add-points/','ProductController.addPoints').middleware(['cauth'])

Route.get('/profile','ProductController.showProfile').middleware(['cauth'])


Route.get('/hotspots',({view})=>{
return view.render('hotspots')
})