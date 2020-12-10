'use strict'

/** @type {import('@adonisjs/lucid/src/Schema')} */
const Schema = use('Schema')

class ProductSchema extends Schema {
  up () {
    this.table('products', (table) => {
      // alter table
      table.string('url', 249)

    })
  }

  down () {
    this.table('products', (table) => {
      // reverse alternations
    })
  }
}

module.exports = ProductSchema
