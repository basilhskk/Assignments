'use strict'

/** @type {import('@adonisjs/lucid/src/Schema')} */
const Schema = use('Schema')

class CouponSchema extends Schema {
  up () {
    this.create('coupons', (table) => {
      table.increments()
      table.timestamps()
      table.string('name', 80)
      table.string('description', 190)
      table.string('discount', 190)
      table.integer('category_id').unsigned().references('id').inTable('categories')
      table.string('url', 249)
    })
  }

  down () {
    this.drop('coupons')
  }
}

module.exports = CouponSchema
