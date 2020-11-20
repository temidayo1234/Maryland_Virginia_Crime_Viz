// Define SVG area dimensions
var svgWidth = 560;
var svgHeight = 360;
// Define the chart's margins as an object
var chartMargin = {
    top: 10,
    right: 30,
    bottom: 30,
    left: 60
};
// Define dimensions of the chart area
var chartWidth = svgWidth - chartMargin.left - chartMargin.right;
var chartHeight = svgHeight - chartMargin.top - chartMargin.bottom;

// Select body, append SVG area to it, and set the dimensions
var svg = d3
    .select("body")
    .append("svg")
    .attr("height", svgHeight)
    .attr("width", svgWidth);

//Define variables for x labels and y values
var xLabels = [];
var yValues = [];

// Append a group to the SVG area and shift ('translate') it to the right and down to adhere
// to the margins set in the "chartMargin" object.
var chartGroup = svg.append("g")
    .classed("chart-here", true)
    .attr("transform", `translate(${chartMargin.left}, ${chartMargin.top})`);

//clear the chart when new entry is inserted
function clearChart(name) {
    document.getElementsByClassName(name) = "";
};
// Load data
d3.csv("educationcrime.csv").then(function (Data) {
    var Data = Data;
    //Loop through the data to store the y values
    for (i = 0; i < Data.length; i++) { xLabels.push(Data[i]['Education']) };
    // Select the button
    var button = d3.select("#button");
    // Select the form
    var form = d3.select("#form");
    // Create event handlers 
    button.on("click", runEnter);
    form.on("submit", runEnter);
    
    //Funtion for when button is clicked
    function runEnter() {
         document.querySelectorAll('g.x-chart,g.y-chart,rect.bar').forEach(function(a){
            console.log(a); 
            a.remove();
            console.log(a)
             });
        document.getElementsByTagName("rect").innerHTML='';
        //d3.event.preventDefault();
        var inputElement = d3.select("#state-form-input");
        // Get the value property of the input element
        var inputValue = inputElement.property("value");
        Data.forEach(function (data) {
            Object.entries(data).forEach(([key, value]) => {
                // Log the key and value
                search = key;
                if (search === inputValue) {
                    data[inputValue] = +data[inputValue]
                    yValues.push(data[inputValue])
                };
            });
        });

        // scale y to chart height
        var yScale = d3.scaleLinear()
            .domain([0, d3.max(yValues)])
            .range([chartHeight, 0]);

        // scale x to chart width
        var xScale = d3.scaleBand()
            .domain(xLabels)
            .range([0, chartWidth])
            .padding(0.05);

        // create axes
        var yAxis = d3.axisLeft(yScale);
        var xAxis = d3.axisBottom(xScale);

        
        // set x and y to the bottom of the chart
        chartGroup.append("g")
            .classed('x-chart', true)
            .attr("transform", `translate(0, ${chartHeight})`)
            .call(xAxis);
        chartGroup.append("g")
            .classed('y-chart', true)
            .call(yAxis);

        // Build the bar chart
        chartGroup.selectAll(".bar")
            .data(yValues)
            .enter()
            .append("rect")
            .classed("bar", true)
            .attr("width", xScale.bandwidth())
            .attr("height", d => chartHeight - yScale(d))
            .attr("x", (d, i) => xScale(xLabels[i]))
            .attr("y", d => yScale(d));
    }
}).catch(function (error) { console.log(error); });