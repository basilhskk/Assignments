'use strict'

/** @type {import('@adonisjs/lucid/src/Schema')} */
const Schema = use('Schema')

class ReportSchema extends Schema {
  up () {
    this.table('reports', (table) => {
      // alter table
      table.integer('count').unsigned()

    })
  }

  down () {
    this.table('reports', (table) => {
      // reverse alternations
    })
  }
}

module.exports = ReportSchema
