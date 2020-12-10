'use strict'

const Product = use('App/Models/Product')
const Category = use ('App/Models/Category')
const Coupon = use ('App/Models/Coupon')
const User = use('App/Models/User')
const { validate } = use('Validator')
const helper = use('App/Controllers/Http/Helpers/Helper')
const Helper = new helper() 

class ProductController {

    async show ({view,params}){

        let products = []
        let categories = []
        let coupons = []
        if(!this.isEmpty(params)){
            let category = params.category.replace('%20',' ')
            categories = await Category.query().where('id','=',category).fetch()
            categories = categories.toJSON()
            categories = await Category.all()
            categories = categories.toJSON()
            console.log(categories)

        }else{
            categories = await Category.all()
            categories = categories.toJSON()
            console.log(categories)
            coupons = await Coupon.all()
            coupons = coupons.toJSON()
            console.log(coupons)

        }
        
        return view.render('home',{categories:categories,products:products,coupons:coupons})
    }

    async showDetails({view,params,auth,response,request}){
        if(!this.isEmpty(params)){
            let user = ''

            try {
                user = await auth.getUser()
            } catch (error) {
                return response.redirect('/login')
            }
            
            if(user.role == 'admin' || user.role == 'user'){
    
                let id = Helper.sanitizer(params.id)
                let product = await Product.query().where('id','=',id).fetch()
                product=product.toJSON()
                if(product[0].category_id ==1){

                    let lesson = product[0].lesson.split('||')

                    return view.render('itemDetails',{product:product[0],lesson:lesson})
                }else{
                    let lesson = product[0].lesson.split('||')
                    console.log(lesson)
                    let data = [] 
                    lesson.forEach(element => {
                        console.log(element.split('='))
                        data.push(element.split('=')[0])
                        console.log(eval(element.split('=')[0]))
                    })
                    console.log(data)

                    return view.render('testDetails',{product:product[0],lesson:data})
                }

            }else{
                return response.redirect('/login')
            }
        }else{
           return response.redirect('/')

        }


    }

    async showAdd({view,auth,response,params}){
    
        let user = await auth.getUser()

        if(!this.isEmpty(params)){
        let category = params.id
        let categories = ''
        if(category!=null){
        categories = await Category.query().where('id','=',category).fetch()
        categories = categories.toJSON()
        }else{
            categories = await Category.all()
            categories = categories.toJSON()
        }
        console.log(categories)
        categories = categories.map((val)=>{
            return {"name": val.name, "id":val.id}
        })
        return view.render('addProduct',{'categories':categories})

        }else{
        
            return response.redirect('/')
        }

    }

    async add({view, request}){

        // const Helper = new helper() //.sanitizer(test)

        let data = request.all()



        let categories = await Category.all()
        categories = categories.toJSON()
        categories = categories.map((val)=>{
            return {"name": val.name, "id":val.id}
        })

        console.log(request.all())

        const validation = await validate(request.all(),{
            name: 'required',
            description: 'required',
            category : 'required',
            points:'required'

        })


        let err=""
        if(validation.fails()){
            err = "Please enter valid info"
            return view.render('addProduct',{err:err,categories:categories})
        }

        let succ = "Product Added Successfully"
        

        if(data._type == 'coupon'){
            succ =  "Coupon Added Successfully"
            const coupon = new Coupon()
            coupon.name = Helper.sanitizer(data.name)
            coupon.discount = Helper.sanitizer(data.discount)
            coupon.description = Helper.sanitizer(data.description.slice(0,189))
            coupon.points = Helper.sanitizer(data.points)
            coupon.category_id = Helper.sanitizer(data.category)
            await coupon.save()

        }else{
            
            const newproduct = new Product()
            newproduct.name = Helper.sanitizer(data.name)
            newproduct.description = Helper.sanitizer(data.description.slice(0,189))
            newproduct.category_id = Helper.sanitizer(data.category)
    
            await newproduct.save()
    
        }



        return view.render('addProduct',{succ:succ,categories:categories})

    }


    async showProfile({view}){

        return view.render('profile')
    }

    async showBuy({view, params}){
        let category = params.id
        let categories = ''
        categories = await Category.query().where('id','=',category).fetch()
        categories = categories.toJSON()

        return view.render('itemDetails',{category:categories[0]})
    }

    async showCoupon({view, params}){
        let coupon = params.id
        let coupons = ''
        coupons = await Coupon.query().where('id','=',coupon).fetch()
        coupons = coupons.toJSON()

        return view.render('itemDetails',{coupon:coupons[0]})
    }


    async addPoints({view,request}){
        let data = request.all()
        
        let categories = await Category.all()
        categories = categories.toJSON()

        const validation = await validate(request.all(),{
            usercode: 'required',
            points: 'required',
            quantity : 'required'
        })

        let err =""
        let succ = "Οι πόντοι μεταφέρθηκαν με επιτυχία! "

        if(validation.fails()){
            err = "Παρακαλώ εισάγετε όλα τα πεδία!"
            return view.render('addProduct',{err:err,categories:categories})
        }

        let uuid = data.usercode
        let user = null
        try{
            user = await User.query().where('uuid','=',uuid).fetch()
            let points = user.toJSON()[0].points
            user = user.toJSON()[0]
            console.log(user)

        if(user!= null && user.role=='supplier'){

        await User.query().where('uuid','=',uuid).update({points:parseInt(points)+parseInt(data.points)})
        return view.render('home',{succ:succ,categories:categories})

       }else{

        err = "Δεν υπάρχει χρήστης με αυτόν τον κωδικό"
        return view.render('home',{err:err,categories:categories})

       }

        }catch{
            err = "Δεν υπάρχει χρήστης με αυτόν τον κωδικό"
            return view.render('home',{err:err,categories:categories})

        }

        

    }

    isEmpty(obj) {
        for(var prop in obj) {
            if(obj.hasOwnProperty(prop))
                return false;
        }
    
        return true;
    }

}

module.exports = ProductController
