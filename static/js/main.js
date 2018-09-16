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
    var xCenterOffset = -(svg.attr("width") - g.graph().width) / 1.5;
    inner.attr("transform", "translate(" + xCenterOffset + ", 20)");
    svg.attr("height", g.graph().height + 80); 
}    

function setNodesandEdges(parsedArray) {
    
    
    // determining length of array
    var arrayLength = parsedArray.length;
    
    // based on array length set number of nodes
    for (let i = 0; i < arrayLength; i++) { 
        g.setNode(i, {width: 2, height: 2 });
    }
    
    // set edges
    for (let i = 1; i < arrayLength; i++) {
        arrayLength1 = parsedArray[i].length;
        g.setEdge(parsedArray[i][1], parsedArray[i][0]);
        g.setEdge(parsedArray[i][arrayLength1-1], parsedArray[i][0]);
    }
     
    g.graph().nodesep = 5;
    g.graph().ranksep = 10;
    g.graph().edgesep = 7;
    g.graph().rankDir = 'LR';
    
}
    

    
//Callback from AJAX call
function processData(data){
    
    
    
    // parsing csv file into array
    var parsedList=JSON.parse(data);
   
    // calling above function to set nodes and edges
    setNodesandEdges(parsedList);
          
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
        


window.test = function(e) {
  if (e.value === 'weighted') {
    getData("weighted");
  } else if (e.value === 'unweighted') {
    getData("unweighted"); 
  } else if (e.value === 'random') {
    getData("random");
  }
}

function updateTextInput(val) {
          document.getElementById('textInput').value=val; 
}


$(document).ready(function(){
    $('#advanced1').hide();
    $('#advanced2').hide();
    $('#advanced3').hide();
    
    // First Way : 
    $('#HiddenInput').empty();
    $('#HiddenInput').val($('#dropdown').val());
    var value =  $('#HiddenInput').val();
    $('#dropdown').val(value);
    $('#div' + value).show();
 
    
    //Second Way just get dropdown value show value of the DIv: 
  //  var value2 =  $('#dropdown').val();
   // $('#div' + value2).show();
    
   $('#dropdown').change(function() {
     $('#advanced1').hide();
    $('#advanced2').hide();
    $('#advanced3').hide();
      $('#HiddenInput').val($(this).val());
      $('#advanced' + $(this).val()).show();
 });
});


