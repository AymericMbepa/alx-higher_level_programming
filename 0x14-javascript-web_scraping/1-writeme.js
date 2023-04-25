#!/usr/bin/node

'use strict';

const fs = require('fs');

const filePath = process.argv[2];

const stringtowrite = process.argv[3];

fs.writeFile(filePath, stringtowrite, 'utf-8', function (err) {
    if (err) {
	console.log(err);
    }
});
