
// this gives us age: {property: x, property: y}
//so we need each key (age, breed, etc) to set the variable for the chart
// and then read each properly.value into array, and property.key
// into arrayLabel above
datadata = {"age":{"Adult":37,"Baby":23,"Senior":6,"Young":34},"breed":{"American Bobtail":1,"Domestic Long Hair":13,"Domestic Medium Hair":6,"Domestic Short Hair":63,"Egyptian Mau":1,"Russian Blue":1,"Siamese":2,"Snowshoe":2,"Tabby":4,"Tiger":1,"Tortoiseshell":3,"Turkish Van":1,"Tuxedo":2},"color":{"Black":22,"Black & White / Tuxedo":13,"Blue Cream":2,"Buff & White":1,"Calico":3,"Cream Point":1,"Dilute Calico":1,"Dilute Tortoiseshell":1,"Flame Point":1,"Gray & White":6,"Gray / Blue / Silver":6,"Orange & White":3,"Orange / Red":2,"Tabby (Brown / Chocolate)":10,"Tabby (Buff / Tan / Fawn)":2,"Tabby (Gray / Blue / Silver)":4,"Tabby (Orange / Red)":3,"Tabby (Tiger Striped)":3,"Tortoiseshell":4,"White":2},"gender":{"Female":46,"Male":54},"size":{"Large":9,"Medium":78,"Small":13}}
d3.select("canvas")

//d3.json("/catdata", function(data) {
d3.json("/catdata", function(data) {
  console.log(data);
  Object.entries(data).forEach(([key, value]) => {
    var chartLabel = data.key;
	  console.log(chartLabel);
	  Object.keys(value).forEach(([key, value]) => {
      var dataLabels = this.map(thing => thing.key);
      var dataValues = this.map(thing => thing.value);
    });
  });
  console.log(chartLabel);
  console.log(dataLabels);
  console.log(dataValues);
});

/*
d3.json("/catdata", function(data) {
  console.log(data);
  //iterate over each object
  Object.entries(data).forEach(([key, value]) => {
    //object foramt is age: {young: 1, adult: 2, senior: 3}
    // age is the key, the {} is the value
    // assign the key to a variable for chart label
    var chartLabel = data.key;

    //assign the value's keys to dataLabels
    // dataLabels = [young, adult, senior]
    var dataLabels = data.value.[keys];

    //assign value's values to dataValues;
    // dataValues = [5, 8, 3]
    var dataValues = data.value.[values];

    //from a class exerices
    //var dataset = data.map(recipe => recipe.dish);
    //var spicesMapped = recipes.map(recipe => recipe.spice);
    //var dataset = data.map(ageLabel => data.);

});
*/

/*
var myDoughnutChart = new Chart(ctx, {
    type: 'doughnut',
    data: data,
    options: options
});
*/
