from opcua import Server

server = Server()

url = "opc.tcp://192.168.0.100:4840"
server.set_endpoint(url)

name = "OPCUA_SIMULATION_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace, "Parameters")

J1= Param.add_variable(addspace, "J1", 0.0)
J2= Param.add_variable(addspace, "J2", 0.0)
J3= Param.add_variable(addspace, "J3", 0.0)
J4= Param.add_variable(addspace, "J4", 0.0)
J5= Param.add_variable(addspace, "J5", 0.0)
J6= Param.add_variable(addspace, "J6", 0.0)
var_OUT = Param.add_variable(addspace, "var_OUT", 0)
var_IN = Param.add_variable(addspace, "var_IN", 0)

J1.set_writable()
J2.set_writable()
J3.set_writable()
J4.set_writable()
J5.set_writable()
J6.set_writable()
var_OUT.set_writable()
var_IN.set_writable()

server.start()
print("Server started at {}".format(url))

