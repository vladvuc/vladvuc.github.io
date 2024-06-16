fetch("md/home.md")
  .then((response) => response.text())
  .then((md) => {
    // Convert markdown to HTML
    const html = marked(md);

    // Insert the HTML into the page
    document.getElementById("home").innerHTML = html;
  });

// Define your data
const graphData = {
  nodes: [
    { id: "Artificial Agent", group: 1 },
    { id: "Human Agent", group: 1 },
    { id: "Agent", group: 2 },
    { id: "HI-Scenario", group: 3 },
    { id: "Capability", group: 4 },
    { id: "Information Processing", group: 4 },
    { id: "Method", group: 5 },
    { id: "Processing Type", group: 5 },
  ],
  links: [
    { source: "Artificial Agent", target: "Agent", value: 1 },
    { source: "Human Agent", target: "Agent", value: 1 },
    { source: "HI-Scenario", target: "Agent", value: 1 },
    { source: "Agent", target: "Capability", value: 1 },
    { source: "Agent", target: "Information Processing", value: 1 },
    { source: "Information Processing", target: "Method", value: 1 },
    { source: "Information Processing", target: "Processing Type", value: 1 },
  ],
};

// Set up dimensions and SVG element
const width = 960,
  height = 600;
const svg = d3
  .select("body")
  .append("svg")
  .attr("width", width)
  .attr("height", height);

// Create a simulation to handle node placement
const simulation = d3
  .forceSimulation(graphData.nodes)
  .force(
    "link",
    d3.forceLink(graphData.links).id((d) => d.id)
  )
  .force("charge", d3.forceManyBody().strength(-500))
  .force("center", d3.forceCenter(width / 2, height / 2));

// Add links (arrows) to the graph
const link = svg
  .append("g")
  .attr("class", "links")
  .selectAll("line")
  .data(graphData.links)
  .join("line")
  .attr("stroke", "#999")
  .attr("stroke-opacity", 0.6);

// Add nodes (circles) to the graph
const node = svg
  .append("g")
  .attr("class", "nodes")
  .selectAll("circle")
  .data(graphData.nodes)
  .join("circle")
  .attr("r", 15)
  .attr("fill", (d) =>
    d.group === 1 ? "blue" : d.group === 5 ? "green" : "orange"
  )
  .call(
    d3.drag().on("start", dragstarted).on("drag", dragged).on("end", dragended)
  );

// Add text labels to the nodes
node
  .append("text")
  .text((d) => d.id)
  .attr("x", 6)
  .attr("y", 3);

// Update node and link positions during simulation
simulation.on("tick", () => {
  link
    .attr("x1", (d) => d.source.x)
    .attr("y1", (d) => d.source.y)
    .attr("x2", (d) => d.target.x)
    .attr("y2", (d) => d.target.y);

  node.attr("cx", (d) => d.x).attr("cy", (d) => d.y);
});

// Drag functions
function dragstarted(event, d) {
  if (!event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}

function dragged(event, d) {
  d.fx = event.x;
  d.fy = event.y;
}

function dragended(event, d) {
  if (!event.active) simulation.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}
