'use strict'

const Product = use('App/Models/Product')
const Category = use ('App/Models/Category')
const Report = use ('App/Models/Report')
const { validate } = use('Validator')
const helper = use('App/Controllers/Http/Helpers/Helper')
const Helper = new helper() 

class ProductController {

    async show ({view,params,response,auth}){
        let user = ''
        try {
            user = await auth.getUser()
            user = user.toJSON() 
        } catch (e) {
            return response.redirect('/login')
        }


        let products = []
        let categories = []
        let reports = ''
        reports = await Report.query().where('user_id','=',user.id).where('count','>=',3).fetch()
        reports = reports.toJSON()

        if(!this.isEmpty(params)){
            let category = params.category.replace('%20',' ')
            categories = await Category.query().where('id','=',category).fetch()
            categories = categories.toJSON()
            categories = categories.map((val)=>{
                return {"name": val.name, "id":val.id}
            })
            products = await Product.query().where('category_id','=',categories[0].id).fetch()
            products=products.toJSON()
            categories = await Category.all()
            categories = categories.toJSON()

        }else{
            categories = await Category.all()
            categories = categories.toJSON()
            categories = categories.map((val)=>{
                return {"name": val.name, "id":val.id}
            })
            products = await Product.all()
            products=products.toJSON()

        }
        
        return view.render('home',{categories:categories,products:products,reports:reports,valid:reports.length})
    }

    async showDetails({view,params,auth,response}){
        if(!this.isEmpty(params)){
            let user = ''

            try {
                user = await auth.getUser()
            } catch (error) {
                return response.redirect('/login')
            }
            
            if(user.role == 'admin' || user.role == 'user'){
    
                let id =   Helper.sanitizer(params.id)
                let product = await Product.query().where('id','=',id).fetch()
                product=product.toJSON()
                if(product[0].category_id == 1 && product.id !=21){

                    let lesson = product[0].lesson.split('||')

                    return view.render('itemDetails',{product:product[0],lesson:lesson})
                }
                else  if(product[0].id == 21){
                    
                    let lesson = product[0].lesson.split('||')
                    let data = [] 
                    let specificQuestion = 0
                    let reports = ''
                    reports = await Report.query().where('user_id','=',user.id).where('count','>=',3).fetch()
                    
                    reports = reports.toJSON()
                    
                    if (reports.length<5){
                        if(reports.length==1){
                            specificQuestion=6
                        }else if(reports.length==2){
                            specificQuestion=3
                        }else{
                            specificQuestion=1
                        }
                    }

                    lesson.forEach(element => {
                        data.push(element.split('=')[0])
                    })

                    let test = []
                    console.log(reports.length)
                    console.log('a')

                    for(let j=0;reports.length>j;j=j+1){
                        console.log('aasdasd')
                        
                        if(specificQuestion>1){

                            for (let k=0;specificQuestion>k;k=k+1){
                                test.push(this.getSpecialQuestion(data,reports[j].lesson))
                            }   
                        }else{
                            test.push(this.getSpecialQuestion(data,reports[j].lesson))
                        }
                        console.log(test)
                    }


                    while(test.length< 10){

                        let randomElement = data[Math.floor(Math.random() * data.length)];
                        
                        if(!test.includes(randomElement)){
                            test.push(randomElement);
                        }
                    }
                    return view.render('testDetails',{product:product[0],lesson:test})

                        
                }
                else{
                    let lesson = product[0].lesson.split('||')
                    let data = [] 
                    lesson.forEach(element => {
                        data.push(element.split('=')[0])
                    })

                    return view.render('testDetails',{product:product[0],lesson:data})
                }

            }else{
                return response.redirect('/login')
            }
        }else{
           return response.redirect('/')

        }


    }

    async showAdd({view,auth,response}){
    
        let user = await auth.getUser()
        if(user.role == 'admin'){

        let categories = await Category.all()
        categories = categories.toJSON()
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

        const validation = await validate(request.all(),{
            name: 'required',
            description: 'required',
            category : 'required'
        })


        let err=""
        if(validation.fails()){
            err = "Please enter valid info"
            return view.render('addProduct',{err:err,categories:categories})
        }

        const succ = "Product Added Successfully"
        
        const newproduct = new Product()
        newproduct.name = Helper.sanitizer(data.name)
        newproduct.description = Helper.sanitizer(data.description.slice(0,189))
        newproduct.category_id = Helper.sanitizer(data.category)

        await newproduct.save()

        return view.render('addProduct',{succ:succ,categories:categories})

    }


    async checkTest({ request,response,params,auth}){

        let user = await auth.getUser()
        user = user.toJSON()
        let reports = ''
        let data = request.all()
        let counter = 0
        let count = ''
        let newrep = ''
        if(!this.isEmpty(params)){

            let id = params.id

            if(id == 21 ){
                for(var prop in data) {
                    if(prop != '_csrf'){
                        if(eval(prop) == eval(data[prop])){
                            counter = counter +1 
                            reports = await Report.query().where('user_id','=',user.id).where('lesson','=',prop.split('*')[1].trim()).fetch()
                            if(reports.toJSON()[0]>0){
                                count = reports.toJSON()[0].count - 1
                                await Report.query().where('user_id','=',user.id).where('lesson','=',prop.split('*')[1].trim()).update({ count: count })
                            }

                        }else{
                            reports = await Report.query().where('user_id','=',user.id).where('lesson','=',prop.split('*')[1].trim()).fetch()
                            count = reports.toJSON()[0].count + 1
                            await Report.query().where('user_id','=',user.id).where('lesson','=',prop.split('*')[1].trim()).update({ count: count })
                       
                        }
                    }
                        
                }
            }else{           
                for(var prop in data) {
                    if(prop != '_csrf'){
                        if(eval(prop) == eval(data[prop])){
                            counter = counter +1 
                        }
                    }
                        
                }
        }

        if (counter == 10 ){
            return response.redirect('/success')
        }
        else{
            return response.redirect('/fail')
        }

    }else{
        return response.redirect('/')
    }

    }

    getSpecialQuestion(data,lesson){
        let question = ''
        let lessons = []

        for (let i = 0; data.length>i; i=i+1){
            if(data[i].split('*')[1].trim()==lesson){
                lessons.push(data[i])
            }
        }
        question = lessons[Math.floor(Math.random() * lessons.length)];

        return question
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
