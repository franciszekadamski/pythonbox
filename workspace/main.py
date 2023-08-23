import lib


lib.hello_world()
# lib.list_pip()
# lib.show_example_plot()
lib.pm4py_minimal_example("running-example.csv")
lib.write_xes_example("running-example.csv")

filename = lib.save_graph_from_xes("running-example.xes", image_filename="nx_example.png", vis_option="nx")
lib.show_image_from_file(filename)

# filename = lib.save_graph_from_xes("running-example.xes", image_filename="petri_example.png", vis_option="petri")
# lib.show_image_from_file(filename)
