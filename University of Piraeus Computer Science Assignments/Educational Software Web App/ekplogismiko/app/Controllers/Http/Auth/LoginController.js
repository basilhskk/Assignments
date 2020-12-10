'use strict'
const User  = use('App/Models/User')
const Hash = use('Hash')
const helper = use('App/Controllers/Http/Helpers/Helper')
const Helper = new helper() //.sanitizer(test)
const { validate } = use('Validator')
const nanoid = require('nanoid/async')
const Mail = use('Mail')

class LoginController {
    async show({view,auth,response}){
        try {
            const user = await auth.getUser()
            return response.route('/')
          } catch (error) {
            return view.render('auth.login')
        }


    }

    async login({request,response,view,auth}){
        
        let err = "Wrong email/password!" 

        const validation = await validate(request.all(),{
            email: 'required|email',
            password: 'required',
        })



        if(validation.fails()){
                err = "Please enter valid email"
            return view.render('auth.login',{err:err})
        }
        
        //check user input
            let user =null
        
        try {
             user = await User.findBy('email',Helper.sanitizer(request.input('email')))
        } catch (error) {
            console.log('test')
            return view.render('auth.login',{err:err})
        }
       
        if(!user){
            return view.render('auth.login',{err:err})
        }
        const math_password = await Hash.verify(Helper.sanitizer(request.input('password')), user.password)
                
        if (!math_password) {
            return view.render('auth.login',{err:err})
        }
    
        try {
          await auth.login(user)
          return response.route('/')
        } catch (e) {
            return view.render('auth.login',{err:err})
        }
             
    }

    async showForgot({view,auth,response}){


        try {
            const user = await auth.getUser()
            return response.route('/')
          } catch (error) {
            return view.render('auth.forgot')
        } 

    }

    async forgot({request,view}){

        let err = "Wrong email/password!" 

        const validation = await validate(request.all(),{
            email: 'required|email',
        })



        if(validation.fails()){
                err = "Please enter valid email"
            return view.render('auth.forgot',{err:err})
        }
        
        //check user input
        let user =null
        
        try {
             user = await User.findBy('email',Helper.sanitizer(request.input('email')))
        } catch (error) {}

        const secret = await nanoid()

        if(user!=null){
        
        user.otp = secret
    
        await user.save()

        let key = Helper.sanitizer(request.input('email')).toString() +","+ secret
        key = Buffer.from(key).toString('base64')

        await Mail.connection('gmail').send('emails.forgot', {secret:key}, (message) => {
            
            message.to('basilhskoutsokostas@gmail.com')
          })
        
        }
        
        let succ= "An email will be send to you shortly!"
        
       return view.render('auth.forgot',{succ:succ})
          
    }


    async recover({view,params,response}){

        if(!this.isEmpty(params)){
            let data = Buffer.from(decodeURIComponent(params.key), 'base64').toString('ascii').split(',')
           
            let user = null
            try {
                user = await User.findBy('email',Helper.sanitizer(data[0]))
           } catch (error) {
            response.redirect('/')  
        }
           if(user!=null && user.otp==data[1]&&user.otp.length>3){
               return view.render('auth.recover',{key:decodeURIComponent(params.key)})
           }else{
               return response.redirect('/')
           }
    
        }else{
            response.redirect('/')
        }
       
    }

    async recoverLogin({view,auth,response,params,request}){
        if(!this.isEmpty(params)){
            let data = Buffer.from(decodeURIComponent(params.key), 'base64').toString('ascii').split(',')
            let user = null
            let err = ""
            
            const validation = await validate(request.all(),{
                password: 'required',
                rpassword: 'required',
            })

            if(Helper.sanitizer(request.input('password')) != Helper.sanitizer(request.input('rpassword'))){
                err = "Passwords do not match"
                return view.render('auth.recover',{err:err,key:decodeURIComponent(params.key)})
            }

            if(validation.fails()){
                err = "Pleast fill the inputs "
                return view.render('auth.recover',{err:err,key:decodeURIComponent(params.key)})
            }
    
            try {
                user = await User.findBy('email',Helper.sanitizer(data[0]))
           } catch (error) {
            response.redirect('/')
           }
           
           if(user!=null && user.otp==data[1] && user.otp.length>3){
               user.password = Helper.sanitizer(request.input('password'))
               user.otp = null

           }else{
               
               return response.redirect('/')
           }

           await user.save()

           try {
            await auth.login(user)
            return response.route('/')
          } catch (e) {
              return view.render('auth.forgot',{err:err})
          }
              
    
        }else{
            response.redirect('/')
        }
    }


    async logout({auth,response}){
        auth.logout()
        return response.redirect('/')
    }
    
    isEmpty(obj) {
        for(var prop in obj) {
            if(obj.hasOwnProperty(prop))
                return false;
        }
    
        return true;
    }
}

module.exports = LoginController
