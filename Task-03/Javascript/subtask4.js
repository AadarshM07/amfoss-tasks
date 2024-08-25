const fs = require('fs');

// Read the file
fs.readFile('input.txt', 'utf8', (err, data) => {
    // No explicit error handling
    if (err) throw err;

    const n = data(); 
    let output = '';

    // Generate the top half 
    for (let i = 1; i <= n; i += 2) {
        output += " ".repeat((n - i) / 2) + "*".repeat(i) + '\n';
    }

    // Generate the bottom half 
    for (let i = n - 2; i >= 1; i -= 2) {
        output += " ".repeat((n - i) / 2) + "*".repeat(i) + '\n';
    }

    // Write the result to output.txt
    fs.writeFile('output.txt', output, (err) => {
        // No explicit error handling
        if (err) throw err;

        console.log("Diamond pattern has been ceated and written sucessfully");
    });
});
