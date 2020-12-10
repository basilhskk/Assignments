'use strict'

/** @type {import('@adonisjs/lucid/src/Schema')} */
const Schema = use('Schema')

class CategorySchema extends Schema {
  up () {
    this.table('categories', (table) => {
      // alter table
      table.string('type', 100)
    })
  }

  down () {
    this.table('categories', (table) => {
      // reverse alternations
    })
  }
}

module.exports = CategorySchema
