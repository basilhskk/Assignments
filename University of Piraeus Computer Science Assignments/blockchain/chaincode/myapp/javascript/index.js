/*
 * Copyright IBM Corp. All Rights Reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

'use strict';

const myapp = require('./lib/myapp');

module.exports.myapp = myapp;
module.exports.contracts = [ myapp ];
