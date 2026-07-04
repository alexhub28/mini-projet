// bill_length_mm => x
// flipper_length_mm => y
// species => color
// body_mass_g => radius



let data = [];
let species = [];  

let colors = ["pink", "red", "lightblue"];  

let colorsScale;

let xScale;


let bill_lengthExtent;

function setup() {
  createCanvas(800, 800);

  d3.csv("penguins_cleaned.csv", d3.autoType).then(csv =>{
    data = csv;
   console.log(data);


    species = data.map(d => d.species);
    console.log(species);

    species = [...new Set(species)];
    console.log(species);

    colorsScale = d3.scaleOrdinal().domain(species).range(colors);
    console.log(colorsScale);

    let bill_lengthExtent = d3.extent(data, d => d.bill_length_mm);
    xScale = d3.scaleLinear().domain(bill_lengthExtent).range([0, width]);


  })
}

function draw() {
  background(220);

  for (let i = 0; i < data.length; i++) {
    let x = xScale(data[i].bill_length_mm);
    let col = colorsScale(data[i].species);

    noStroke();
    fill(col);

   ellipse(x, 400, 10, 10);
  
}}
