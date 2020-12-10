'use strict'
/** @typedef {import('@adonisjs/framework/src/Request')} Request */
/** @typedef {import('@adonisjs/framework/src/Response')} Response */
/** @typedef {import('@adonisjs/framework/src/View')} View */

class Cauth {
  /**
   * @param {object} ctx
   * @param {Request} ctx.request
   * @param {Function} next
   */
  async handle ({ response,auth }, next) {
    // call next to advance the request
    let user = null
    try {
       user = await auth.getUser()

    } catch (error) {
      return response.redirect('/login')
    }
    
    if(user == null){
      return response.redirect('/login')
    }else{
     await next()

    }

  }

  /**
   * @param {object} ctx
   * @param {Request} ctx.request
   * @param {Function} next
   */
  async wsHandle ({ request }, next) {
    // call next to advance the request
    await next()
  }
}

module.exports = Cauth
