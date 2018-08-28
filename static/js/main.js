var g = new dagreD3.graphlib.Graph().setGraph({});

// Set an object for the graph label
g.setGraph({});

// Default to assigning a new object as a label for each new edge.
g.setDefaultEdgeLabel(function() { return {}; });


   
 
// rendering function
function renderGraph() {
    
    var svg = d3.select("svg"),
    inner = svg.select("g");      
        
    // Create the renderer
    var render = new dagreD3.render();

    // Run the renderer
    render(inner, g);

    // Centering graph
    var xCenterOffset = (svg.attr("width") - g.graph().width) / 2;
    inner.attr("transform", "translate(" + xCenterOffset + ", 20)");
    svg.attr("height", g.graph().height + 80); 
}    
    

    
//Callback from AJAX call
function processData(data){
    

    
    // parsing csv file into array
    //var parsedArray=parse(data);
    var parsedArray=JSON.parse(data);
    // console.log(parsedArray);
    
    var arrayLength = parsedArray.length;
    
    for (let i = 0; i < arrayLength; i++) { 
        g.setNode(i, {width: 3, height: 3 });
    }
    
    for (var i = 1; i < arrayLength; i++) {
        //console.log(parsedArray[i]);
        arrayLength1 = parsedArray[i].length;
        g.setEdge(0,1);
        g.setEdge(0,1);
        g.setEdge(parsedArray[i][1], parsedArray[i][0]);
        g.setEdge(parsedArray[i][arrayLength1-1], parsedArray[i][0]);
        console.log(parsedArray[i][1]);
    }
    
    

      
   //call rendering function
    renderGraph();

}


        
// AJAX call to fetch CSV file of DAG information with callback to processData      
function getData(method) {
    $.ajax({
        url: '/data?method='+method,
        type: 'GET',
        success : processData
    });
    
}
        
getData("weighted");

