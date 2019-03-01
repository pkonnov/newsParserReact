// es5
[1,2,3].filter(function(v) {
  return v % 2;
});

// es6
[1,2,3].filter(v => v % 2);


// es5
var link = function(height, color) {
  var height = height || 50;
  var color = color || 'red';

  // your code
}

// es6 (default settings)
const link = function(height = 50, color = 'red') {
  // your code
}
