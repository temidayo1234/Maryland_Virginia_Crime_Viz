function makeResponsive() {
    // Define SVG area dimensions
    var svgWidth = 1000;
    var svgHeight = 800;
    // Define the chart's margins as an object
    var chartMargin = {
        top: 20,
        right: 40,
        bottom: 30,
        left: 100
    };
    // Define dimensions of the chart area
    var chartWidth = svgWidth - chartMargin.left - chartMargin.right;
    var chartHeight = svgHeight - chartMargin.top - chartMargin.bottom;

    // Select body, append SVG area to it, and set the dimensions
    var svg = d3
        .select("body")
        .append("svg")
        .classed("svg-clear", true)
        .attr("height", svgHeight)
        .attr("width", svgWidth);
    var xLabels = [];
    var yValues = [];
    location_data.forEach(function (data) {
        Object.entries(data).forEach(([key, value]) => { xLabels.push(key); yValues.push(value) })
    });
    document.querySelectorAll('.x-chart, .y-chart,.bar').forEach(function (a) {
        a.remove();
    });

    //d3.event.preventDefault();
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
    var chartGroup = svg.append("g")
        .classed("chart-here", true)
        .attr("transform", `translate(${chartMargin.left}, ${chartMargin.top})`);

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
        .classed('bar', true)
        .attr("width", xScale.bandwidth())
        .attr("height", d => chartHeight - yScale(d))
        .attr("x", (d, i) => xScale(xLabels[i]))
        .attr("y", d => yScale(d));
    yValues.length = 0;
   

    // Step 1: Append a div to the body to create tooltips, assign it a class
    // =======================================================
    var toolTip = d3.select("body").append("div")
        .attr("class", "tooltip");

    // Step 2: Add an onmouseover event to display a tooltip
    // ========================================================
    chartGroup.on("mouseover", function (d, i) {
        toolTip.style("display", "block");
        toolTip.html(`<strong>${yValues[i]}</strong>`)
            .style("left", d3.event.pageX + "px")
            .style("top", d3.event.pageY + "px");
    })
        // Step 3: Add an onmouseout event to make the tooltip invisible
        .on("mouseout", function () {
            toolTip.style("display", "none");
        });
}

// When the browser loads, makeResponsive() is called.
makeResponsive();

// When the browser window is resized, responsify() is called.
d3.select(window).on("resize", makeResponsive);
