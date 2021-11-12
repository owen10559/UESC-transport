class ODMatrix:
    def __init__(self, n=3, default_flow=0.0):
        self.od_flows = []
        for i in range(n):
            self.od_flows.append([default_flow]*n)

    def flow(self, index):
        row, col = index
        return self.od_flows[row][col]

class Connector:
    def __init__(self, nodeids):
        self.nodeids = list(nodeids)

    def get_ods_and_indices(self):
        result = []
        for row, fromnode in enumerate(self.nodeids):
            for col, tonode in enumerate(self.nodeids):
                index = (row, col)
                od = (fromnode, tonode)
                result.append((index, od))

        return result


 