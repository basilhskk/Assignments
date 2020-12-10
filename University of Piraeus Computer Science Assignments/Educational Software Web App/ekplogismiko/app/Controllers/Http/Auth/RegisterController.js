'use strict'
const { validate } = use('Validator')
const User  = use('App/Models/User')
const helper = use('App/Controllers/Http/Helpers/Helper')
const Helper = new helper() //.sanitizer(test)
const Database = use('Database')
const Report = use ('App/Models/Report')

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


        if(validation.fails()){
                
            return view.render('auth.register',{err:err})
        }
        
        const newuser = new User()

        
            newuser.username= Helper.sanitizer(request.input('username')),
            newuser.email= Helper.sanitizer(request.input('email')),
            newuser.role = "user"
            newuser.password= Helper.sanitizer(request.input('password'))
        

        await newuser.save()

        let user = await User.query().where('email','=',Helper.sanitizer(request.input('email'))).fetch()
        user = user.toJSON()[0]
        
        const insertData = [
            {
                'user_id' : user.id,
                'lesson' : 1,
                'count' : 0
            },            {
                'user_id' : user.id,
                'lesson' : 2,
                'count' : 0
            },            {
                'user_id' : user.id,
                'lesson' : 3,
                'count' : 0
            },            {
                'user_id' : user.id,
                'lesson' : 4,
                'count' : 0
            },            {
                'user_id' : user.id,
                'lesson' : 5,
                'count' : 0
            },            {
                'user_id' : user.id,
                'lesson' : 6,
                'count' : 0
            },            {
                'user_id' : user.id,
                'lesson' : 7,
                'count' : 0
            },            {
                'user_id' : user.id,
                'lesson' : 8,
                'count' : 0
            },            {
                'user_id' : user.id,
                'lesson' : 9,
                'count' : 0
            },            {
                'user_id' : user.id,
                'lesson' : 10,
                'count' : 0
            }
        ]

        
        const dbTrx = await Database.raw('INSERT INTO reports (user_id,lesson,count) VALUES('+user.id+',1,0),('+user.id+',2,0),('+user.id+',3,0),('+user.id+',4,0),('+user.id+',5,0),('+user.id+',6,0),('+user.id+',7,0),('+user.id+',8,0),('+user.id+',9,0),('+user.id+',10,0)')

        // await Report.createMany(insertData, dbTrx)

        
        response.redirect('/login')

  

    }

}

module.exports = RegisterController
