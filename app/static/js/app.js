function buildMetadata(sample) {

  // @TODO: Complete the following function that builds the metadata panel

  // Use `d3.json` to fetch the metadata for a sample
    // Use d3 to select the panel with id of `#sample-metadata`

    // Use `.html("") to clear any existing metadata

    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.

    // BONUS: Build the Gauge Chart
    // buildGauge(data.WFREQ);

    var selector = d3.select("#sample-metadata");
    selector.html("") 
    d3.json("/metadata/" + sample).then((sample_metadata) => {
      for(var key in sample_metadata){
        selector
          .append("p")
          .text(key + ":" + sample_metadata[key])
      }
    })

}

function buildCharts(sample) {

  // @TODO: Use `d3.json` to fetch the sample data for the plots


  d3.json("/samples/" + sample).then((data)=>{
    
    // @TODO: Build a Bubble Chart using the sample data

    var data1 = [{
      x :  data["otu_ids"],
      y :  data["sample_values"],
      text: data["otu_labels"],
      mode: 'markers',
      marker: {
        color: data["otu_ids"],
        size: data["sample_values"]
      }
    }];

    Plotly.newPlot("bubble", data1);

    // @TODO: Build a Pie Chart
    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).
  
    var temp_list = [];
    var sample_values = [];
    var otu_ids = [];
    var otu_labels = [];

    for (var j = 0; j < data["sample_values"].length; j++){
      temp_list.push(
        {"sample_value":data["sample_values"][j],
        "otu_id": data["otu_ids"][j],
        "otu_label" : data["otu_labels"][j]})
    }
    temp_list.sort((first, second) => second.sample_value - first.sample_value);

    for (var k = 0; k < 10; k++){
      sample_values[k] = temp_list[k].sample_value;
      otu_ids[k] = temp_list[k].otu_id;
      otu_labels[k] = temp_list[k].otu_label;
    }

    var data2 = [{
      values :  sample_values,
      labels :  otu_ids,
      text: otu_labels,
      textinfo: 'percent',
      hoverinfo: 'text',
      type: "pie",
    }];

    Plotly.newPlot("pie", data2);
  })
  
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);

}

// Initialize the dashboard
init();