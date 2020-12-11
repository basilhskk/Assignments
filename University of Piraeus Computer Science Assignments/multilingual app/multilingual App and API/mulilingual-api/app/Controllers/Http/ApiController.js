'use strict'
const User = use('App/Models/User');
var jwt = require('jsonwebtoken');
const Env = use('Env')

class ApiController {
  async encrypt(data) {
    let token = jwt.sign({
      data: data
    }, Env.get('APP_KEY'), {
      expiresIn: 60 * 60
    });
    return token
  }

  async decrypt(data) {
    var decoded = jwt.verify(data, Env.get('APP_KEY'));
    return decoded.data
  }

  async login({
    request,
    auth,
    response
  }) {
    //get request data
    let data = request.only(['username', 'password'])

    try {
      let u = await auth.attempt(data.username, data.password)

      let user = await User.query().where('email', '=', data.username).fetch()

      user = user.toJSON()[0]

      let token = await this.encrypt('{"username":"' + user.username + '"}')
      console.log(token)
      return '{"token":"' + token + '"}'

    } catch (e) {
      //else return error
      return '{"msg":"Λάθος Χρήστης ή Κωδικός"}'
    }
  }

  async register({
    request
  }) {
    //register new user
    let data = request.all()

    let user = new User()

    user.username = data.username

    user.email = data.email

    user.password = data.password

    try {
      await user.save()

      let token = await this.encrypt('{"username":"' + data.username + '"}')

      return '{"token":"' + token + '"}'
    } catch (error) {
      return '{"msg": "error"}'
    }

  }

  async delete({
    request
  }) {

    let data = request.all()

    console.log(data)

    let username = await this.decrypt(data.token)

    username = JSON.parse(username).username

    let user = await User.query().where('username', '=', username).fetch()

    user = user.toJSON()[0]

    console.log(user)

    let curr = await User.find(user.id)

    await curr.delete()

    return 'success'
  }

  async user({
    request
  }) {
    let data = request.all()

    let username = await this.decrypt(data.token)

    username = JSON.parse(username)

    return username.username
  }


}

module.exports = ApiController
