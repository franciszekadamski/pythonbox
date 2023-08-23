from pm4py.objects.conversion.log import converter as log_converter 
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.visualization.petri_net import visualizer
import pm4py
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import os
import networkx as nx

def list_pip():
  os.system("pip list")

def hello_world():
  print("Hello world!")

def show_example_plot():
  x = np.linspace(0, 100, 100)
  y = np.random.randint(0, 100, 100)

  fig, ax = plt.subplots()
  ax.plot(x, y)
  plt.show()

def pm4py_minimal_example(file_path):
    event_log = pd.read_csv(file_path, sep=';')
    event_log = pm4py.format_dataframe(event_log, case_id='case_id', activity_key='activity', timestamp_key='timestamp')

    start_activities = pm4py.get_start_activities(event_log)
    end_activities = pm4py.get_end_activities(event_log)
    
    print("Start activities: {}\nEnd activities: {}".format(start_activities, end_activities))

def write_xes_example(file_path):
    event_log = pm4py.format_dataframe(pd.read_csv(file_path, sep=';'), case_id='case_id',
                                           activity_key='activity', timestamp_key='timestamp')
    pm4py.write_xes(event_log, file_path.replace('csv', 'xes'))

def save_graph_from_xes(file_path, image_filename="resulting_graph.png", vis_option="model"):
    log = pm4py.read_xes(file_path)

    process_tree = pm4py.discover_bpmn_inductive(log)
    bpmn_model = pm4py.convert_to_bpmn(process_tree)

    nx_graph = bpmn_model.get_graph()
    
    if vis_option == "model":
      pm4py.save_vis_bpmn(bpmn_model, image_filename)
    elif vis_option == "petri":
      net, initial_marking, final_marking = pm4py.convert_to_petri_net(bpmn_model)
      gviz = visualizer.apply(net)
      visualizer.save(gviz, image_filename)
      # pm4py.visualization.common.visualizer.save(gviz, "resulting_graph.png")
    elif vis_option == "nx":
       pos = nx.kamada_kawai_layout(nx_graph) 
       # pos = nx.spring_layout(nx_graph) # alternatively
      #  G = nx.Graph()
      #  # Add nodes and set their positions
      #  for node in nx_graph.nodes:
      #      G.add_node(node.id)
      #      G.nodes[node.id]['pos'] = (0, 0) # (node.graphics.x, node.graphics.y)

       fig, ax = plt.subplots(dpi=800) # (figsize=(4, 4), dpi=500)
       nx.draw(nx_graph, pos, node_size=100, node_color='lightblue') # with_labels=True
       plt.savefig(image_filename)
    else:
       print("Incorrect vis_option parameter")

    return image_filename

def show_image_from_file(image_filename="resulting_graph.png"):    
    img = plt.imread(image_filename)
    plt.imshow(img)
    plt.axis('off')  # Hide axes
    plt.show()

