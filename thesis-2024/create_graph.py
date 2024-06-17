import networkx as nx
from pyvis.network import Network

# Create a directed graph
G = nx.DiGraph()

# The nodes with positions, labels, and hover titles
nodes = {
    'Agent': {
        'label': 'Agent',
        'title': 'This is the class Agent. \nIt represents an entity that can \nperform actions.',
        'color': '#FFB702',
        'font': {'color': '#023047'}
    },
    'HIScenario': {
        'label': 'HI Scenario',
        'title': 'This is the HI Scenario. \nIt represents a scenario involving \nHuman-Computer Interaction',
        'color': '#FFB702',
        'font': {'color': '#023047'}
    },
    'Artificial Agent': {
        'label': 'Artificial Agent',
        'title': 'Recommendation System\nIntelligent System\nChatbot\nML Model\nTesting Tools\nProject Management Bots',
        'color': '#9A130E',
        'font': {'color': '#023047'}
    },
    'Human Agent': {
        'label': 'Human Agent',
        'title': 'Programmer / Developer\nSenior Lead\nProject Manager\nTester\nDesigners\nClient',
        'color': '#9A130E',
        'font': {'color': '#023047'}
    },
    'Ethical Consideration': {
        'label': 'Ethical\nConsideration',
        'title': 'Fairness (biases)\nPrivacy in Company\nOwnership\nRoles within Team\nMoral Dilemmas (AI Decision)\nRoles/Teamwork\nLong-Term system Maintenance\nSecurity',
        'color': '#219EBC',
        'font': {'color': '#023047'}
    },
    'Context': {
        'label': 'Context',
        'title': 'Communication\nUnderstanding commits\nCompany structure\nProcess symbolic personal growth\nTeam Dynamics\nProject Management\nProject Specifics\nOrganization Structure\nTechnical Context',
        'color': '#219EBC',
        'font': {'color': '#023047'}
    },
    'Domain': {
        'label': 'Domain',
        'title': 'Software Engineering\nProject Management',
        'color': '#219EBC',
        'font': {'color': '#023047'}
    },
    'EndGoal': {
        'label': 'EndGoal',
        'title': 'Gives Instructions\nGives Time Estimation\nGives Risk Analysis\nDecision-making\nDetermine skills required\nImprove software quality\nIncrease efficiency\nIncrease team collaboration\nIncrease team communication',
        'color': '#219EBC',
        'font': {'color': '#023047'}
    },
    'Interaction': {
        'label': 'Interaction',
        'title': 'This is the Interaction class. \nIt represents the interaction \npossible between an Agent \nand HI-Scenario.',
        'color': '#219EBC',
        'font': {'color': '#023047'}
    },
    'InteractionTask': {
        'label': 'Interaction Task',
        'title': 'Giving tasks\nReport Making\nCode Review\nTest/QA\nMonitoring and Deployment\nDocumentation Generating',
        'color': '#219EBC',
        'font': {'color': '#023047'}
    },
    'InteractionType': {
        'label': 'Interaction Type',
        'title': 'Collaboration\nApproval\nFeedback\nExpertise\nCooperation\nCommunication\nConflict\nDirective (H -> AI; AI -> H)\nEducational',
        'color': '#219EBC',
        'font': {'color': '#023047'}
    },
    'Capability': {
        'label': 'Capability',
        'title': 'Monitoring\nCollaborativeness\nCommunication\nPredicting\nRecognition\nReasoning\nMaking choices\nLearning on input\nRequirement Analysis\nMetrics Collection\nEstimation\nRisk Analysis\nDecision-making\nPredict Phase\nPlanning',
        'color': '#219EBC',
        'font': {'color': '#023047'}
    },
    'Information Processing': {
        'label': 'Information Processing',
        'title': 'This is the class which defines \nhow the information is being \nprocessed by the agent \nand what is method used',
        'color': '#219EBC',
        'font': {'color': '#023047'}
    },
    'Method': {
        'label': 'Method',
        'title': 'Hybrid\nStatistical\nSymbolic\nFuzzy Logic\nNeural networks\nExpert System\nRule-based\nMachine Learning\nNatural Language Processing',
        'color': '#219EBC',
        'font': {'color': '#023047'}
    },
    'Processing Type': {
        'label': 'Processing Type',
        'title': 'Recognition\nReasoning\nRecollection\nKnowledge Sharing\nAsking for Information\nCollaborative Learning\nDecision-making',
        'color': '#219EBC',
        'font': {'color': '#023047'}
    },
}

# Add nodes to the graph
for node, attr in nodes.items():
    G.add_node(node, **attr)

# Add an edge in the graph
G.add_edge('Agent', 'HIScenario', label='Has', font={'color': '#023047'})
G.add_edge('Artificial Agent', 'Agent', label='subClassOf', font={'color': '#023047'})
G.add_edge('Human Agent', 'Agent', label='subClassOf', font={'color': '#023047'})
G.add_edge('HIScenario', 'Context', label='', font={'color': '#023047'})
G.add_edge('HIScenario', 'Ethical Consideration', label='', font={'color': '#023047'})
G.add_edge('HIScenario', 'Domain', label='', font={'color': '#023047'})
G.add_edge('HIScenario', 'EndGoal', label='', font={'color': '#023047'})
G.add_edge('HIScenario', 'Interaction', label='', font={'color': '#023047'})
G.add_edge('Interaction', 'InteractionTask', label='', font={'color': '#023047'})
G.add_edge('Interaction', 'InteractionType', label='', font={'color': '#023047'})
G.add_edge('Interaction', 'Agent', label='interacting_agent', font={'color': '#023047'})
G.add_edge('Agent', 'Capability', label='capability', font={'color': '#023047'})
G.add_edge('Agent', 'Information Processing', label='processing_information', font={'color': '#023047'})
G.add_edge('Information Processing', 'Method', label='method', font={'color': '#023047'})
G.add_edge('Information Processing', 'Processing Type', label='processing', font={'color': '#023047'})

# Create a pyvis network
net = Network(notebook=True, directed=True, width="100%")

# Add nodes and edges to the pyvis network
net.from_nx(G)

# Disable buttons by customizing options
options = """
var options = {
  "physics": {
    "enabled": true,
    "stabilization": {
      "enabled": false
    },
    "forceAtlas2Based": {
      "gravitationalConstant": -22,
      "centralGravity": 0.002,
      "springLength": 100,
      "springConstant": 0.18,
      "avoidOverlap": 0.5
    },
    "solver": "forceAtlas2Based",
    "timestep": 0.35,
    "adaptiveTimestep": true
  },
  "nodes": {
    "shape": "dot",
    "size": 25,
    "font": {
      "size": 16,
      "color": "#023047"
    },
    "borderWidth": 2
  },
  "edges": {
    "color": {
      "inherit": true
    },
    "width": 2,
    "font": {
      "size": 14,
      "color": "#023047",
      "background": "white",
      "strokeWidth": 0,
      "strokeColor": "#ffffff"
    },
    "smooth": {
      "enabled": true,
      "type": "dynamic",
      "roundness": 0.5
    },
    "arrows": {
      "to": {
        "enabled": true,
        "type": "arrow"
      }
    }
  },
  "interaction": {
    "navigationButtons": true,
    "keyboard": true
  }
}
"""
net.set_options(options)

# Generate the HTML content
html_content = net.generate_html()

# Save HTML file
with open('graph.html', 'w') as f:
    f.write(html_content)
    