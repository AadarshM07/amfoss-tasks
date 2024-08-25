var n =prompt("Enter the number: ")

//TOp half
for (var i = 1; i <= n; i += 2) {
    console.log(" ".repeat((n - i) / 2) + "*".repeat(i));
}
//Bottom half
for (var i = n - 2; i >= 1; i -= 2) {
    console.log(" ".repeat((n - i) / 2) + "*".repeat(i));
}
