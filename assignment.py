from util import FlowBundle

def all_or_nothing_assignment(network, odmatrix, connector):
    bundle = FlowBundle()
    for index, od in connector.get_ods_and_indices():
        odflow = odmatrix.flow(index)
        route = network.shortest_route(od)
        bundle.add_flow(route, odflow)

    return bundle

def increamental_assignment(network, odmatrix, connector):
    bundle = FlowBundle()


    return bundle