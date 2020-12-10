'use strict'

/** @type {import('@adonisjs/lucid/src/Schema')} */
const Schema = use('Schema')

class CouponSchema extends Schema {
  up () {
    this.table('coupons', (table) => {
      // alter table
      table.string('points',190)

    })
  }

  down () {
    this.table('coupons', (table) => {
      // reverse alternations
    })
  }
}

module.exports = CouponSchema
