'use strict'

/** @type {import('@adonisjs/lucid/src/Schema')} */
const Schema = use('Schema')

class ProductsSchema extends Schema {
  up () {
    this.create('products', (table) => {
      table.increments()
      table.timestamps()
      table.string('name', 80)
      table.string('description', 190)
      table.integer('category_id').unsigned().references('id').inTable('categories')
    })
  }

  down () {
    this.drop('products')
  }
}

module.exports = ProductsSchema
