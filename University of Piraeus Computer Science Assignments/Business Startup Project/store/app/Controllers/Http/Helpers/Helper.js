'use strict'
const validator = require("validator")
var xssFilters = require('xss-filters');

class Helper {

    sanitizer(value){

        let safe_value = xssFilters.inHTMLData(value)
        safe_value = validator.escape(safe_value)
        safe_value = validator.trim(safe_value)

        return safe_value
    }

}

module.exports = Helper
