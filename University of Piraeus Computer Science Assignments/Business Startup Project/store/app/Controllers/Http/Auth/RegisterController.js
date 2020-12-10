'use strict'
const { validate } = use('Validator')
const User  = use('App/Models/User')
const helper = use('App/Controllers/Http/Helpers/Helper')
const nanoid = require('nanoid/async')
const Helper = new helper() //.sanitizer(test)

class RegisterController {

    async show({view,auth,response}){
        try {
            const user = await auth.getUser()
            return response.route('/')
          } catch (error) {
            return view.render('auth.register')
        }
    }

    async register({request, session, response,view}){
        const validation = await validate(request.all(),{
            username: 'required|unique:users,username',
            email: 'required|email|unique:users,email',
            password: 'required',
        })
        let err= "Sorry, user or email is already in use!"

        if(validation.fails() || (request.input('role') !='farm' && request.input('role') !='supplier'  && request.input('role') !='hotspot') ){
                
            return view.render('auth.register',{err:err})
        }

        const newuser = new User()


            newuser.username= Helper.sanitizer(request.input('username'))
            newuser.email= Helper.sanitizer(request.input('email'))
            newuser.role =  Helper.sanitizer(request.input('role'))
            newuser.password= Helper.sanitizer(request.input('password'))
            const secret = await nanoid()
            newuser.uuid= secret


        await newuser.save()
        
        response.redirect('/login')

  

    }

}

module.exports = RegisterController
