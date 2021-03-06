'use strict'

/** @type {import('@adonisjs/lucid/src/Schema')} */
const Schema = use('Schema')

class CategoriesSchema extends Schema {
  up () {
    this.create('categories', (table) => {
      table.increments()
      table.timestamps()
      table.string('name',190).unique()
    })
  }

  down () {
    this.drop('categories')
  }
}

module.exports = CategoriesSchema
