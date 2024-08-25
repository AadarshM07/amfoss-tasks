//Write a program that reads a string from a file named input.txt and writes that string to another file named output.txt.

var fs = require("fs");

// Read the 
fs.readFile('input.txt', function (err, data) {
    var upload = data.toString();
    
    // Write the content to 'output.txt'
    fs.writeFile('output.txt', upload, function () {
        console.log("Content written to 'output.txt'");
    });
});

