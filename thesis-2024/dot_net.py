import networkx as nx
from pyvis.network import Network

# Create a directed graph
G = nx.DiGraph()

# Add nodes with positions and labels
nodes = {
    'Agent': {'label': 'Agent', 'pos': (0, 0), 'color': '#FFB702', 'font': {'color': '#023047', 'title': 'This is some title'}},
    'HIScenario': {'label': 'HI Scenario', 'pos': (5, 5), 'color': '#FFB702', 'font': {'color': '#023047'}},
    # 'Artificial Agent': {'label': 'Artificial Agent', 'pos': (-2, 2), 'color': '#9A130E', 'font': {'color': 'ghostwhite'}},
    # 'Human Agent': {'label': 'Human Agent', 'pos': (1, 2), 'color': '#9A130E', 'font': {'color': 'ghostwhite'}},
    # 'Ethical Consideration': {'label': 'Ethical\nConsideration', 'pos': (4, 3)},
    # 'Context': {'label': 'Context', 'pos': (6, 2)},
    # 'Domain': {'label': 'Domain', 'pos': (6, 1)},
    # 'EndGoal': {'label': 'EndGoal', 'pos': (6, 0)},
    # 'Interaction': {'label': 'Interaction', 'pos': (4, -1)},
    # 'InteractionTTask': {'label': 'Interaction Task', 'pos': (3, -2)},
    # 'InteractionType': {'label': 'Interaction Type', 'pos': (5, -2)},
    # 'Capability': {'label': 'Capability', 'pos': (-4, 0)},
    # 'Information Processing': {'label': 'Information Processing', 'pos': (-1, -2)},
    # 'Method': {'label': 'Method', 'pos': (-2, -3.5)},
    # 'Type': {'label': 'Processing Type', 'pos': (1, -3.5)}
}

# Add text nodes
text_nodes = {
    # 'AI_text': {'label': 'Recommendation System\nIntelligent System\nChatbot\nML Model\nTesting Tools\nProject Management Bots', 'pos': (-2, 3)},
    # 'Human_Text': {'label': 'Programmer / Developer\nSenior Lead\nProject Manager\nTester\nDesigners\nClient', 'pos': (1, 3)},
    # 'Ethical_Text': {'label': 'Fairness (biases)\nPrivacy in Company\nOwnership\nRoles within Team\nMoral Dilemmas (AI Decision)\nRoles/Teamwork\nLong-Term system Maintenance\nSecurity', 'pos': (4, 4.1)},
    # 'Interaction_Type_text': {'label': 'Collaboration\nApproval\nFeedback\nExpertise\nCooperation\nCommunication\nConflict\nDirective (H -> AI; AI -> H)\nEducational', 'pos': (5, -3.22)},
    # 'Interaction_Task_Text': {'label': 'Giving tasks\nReport Making\nCode Review\nTest/QA\nMonitoring and Deployment\nDocumentation Generating', 'pos': (3, -3)},
    # 'ProcessingTypeText': {'label': 'Recognition\nReasoning\nRecollection\nKnowledge Sharing\nAsking for Information\nCollaborative Learning\nDecision-making', 'pos': (1.040, -4.5)},
    # 'CapabilityText': {'label': 'Monitoring\nCollaborativeness\nCommunication\nPredicting\nRecognition\nReasoning\nMaking choices\nLearning on input\nRequirement Analysis\nMetrics Collection\nEstimation\nRisk Analysis\nDecision-making\nPredict Phase\nPlanning', 'pos': (-4, -1.5)},
    # 'MethodText': {'label': 'Hybrid\nStatistical\nSymbolic\nFuzzy Logic\nNeural networks\nExpert System\nRule-based\nMachine Learning\nNatural Language Processing', 'pos': (-2, -4.72)},
    # 'ContextText': {'label': 'Communication\nUnderstanding commits\nCompany structure\nProcess symbolic personal growth\nTeam Dynamics\nProject Management\nProject Specifics\nOrganization Structure\nTechnical Context', 'pos': (7, 3)},
    # 'DomainText': {'label': 'Software Engineering\nProject Management', 'pos': (7.2, 1)},
    # 'EndGoalText': {'label': 'Gives Instructions\nGives Time Estimation\nGives Risk Analysis\nDecision-making\nDetermine skills required\nImprove software quality\nIncrease efficiency\nIncrease team collaboration\nIncrease team communication', 'pos': (7.4, -0.7)}
}

# Add nodes to the graph
for node, attr in nodes.items():
    G.add_node(node, **attr)

for node, attr in text_nodes.items():
    G.add_node(node, **attr, shape='box', color='ghostwhite', font={'color': '#023047'})

# Add edges with labels
edges = [
    ('HIScenario', 'Agent', 'Has'),
    ('Agent', 'Capability', 'capability'),
    ('Artificial Agent', 'Agent', 'subClassOf'),
    ('Human Agent', 'Agent', 'subClassOf'),
    # ('Agent', 'Information Processing', 'processing_information'),
    # ('Interaction', 'Agent', 'interacting_agent'),
    # ('Information Processing', 'Method', 'method'),
    # ('Information Processing', 'Type', 'processing'),
    # ('HIScenario', 'Context', ''),
    # ('HIScenario', 'Ethical Consideration', ''),
    # ('HIScenario', 'Domain', ''),
    # ('HIScenario', 'EndGoal', ''),
    # ('HIScenario', 'Interaction', ''),
    # ('Interaction', 'InteractionTTask', ''),
    # ('Interaction', 'InteractionType', '')
]

for edge in edges:
    if len(edge) == 3:
        u, v, label = edge
        G.add_edge(u, v, label=label, font={'color': '#023047'})
    else:
        u, v = edge
        G.add_edge(u, v)

# Create a pyvis network
net = Network(notebook=True, directed=True)

# Add nodes and edges to the pyvis network
net.from_nx(G)

# Customize the physics layout
net.show_buttons(filter_=['physics'])
net.toggle_physics(True)

# Save the graph to an HTML file
net.show('graph.html')