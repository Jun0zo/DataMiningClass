
import pandas as pd

def get_weight():
    return 0

def get_entropy():
    return 0

def split_with_feature(data : pd.DataFrame, feature_name : str):
    # print('===========')
    # print(data[feature_name])
    fact_idxs, fact_col_names = pd.factorize(data[feature_name])
    
    ret = [[] for _ in range(len(fact_col_names))]
    for idx, row in data.iterrows():
        fact_idx = fact_idxs[idx]
        ret[fact_idx].append(row)
    
    return ret
    

class Node:
    def __init__(self, data_indexes):
        self.data_indexes = data_indexes
        
    def filter(self, df):
        return df.loc[self.data_indexes]

class DecisionTree:
    def __init__(self, df : pd.DataFrame):
        self.data = df
        self.last_features = list(df)[:-1]
        
    
        
    def makeTree(self, node : Node):
        data = node.filter(self.data)
        parent_entropy = get_entropy(data)
        print(data)
        for last_feature in self.last_features:
            splited_data = split_with_feature(data, last_feature)
            child_entropy = 0
            for a in splited_data:
               child_entropy += get_weight(data, a) * get_entropy(a)
               
            information_gain = parent_entropy - child_entropy
        
        # information gain 최솟값 찾고 트리만들고
    
    def fit(self):
        root_node = Node(list(range(len(self.data))))
        print(root_node.filter(self.data))
        nodes = [root_node]
        while self.last_features:
            for node in nodes:
                self.makeTree(node)
            break
        


if __name__ == '__main__':
    # 경사	표면	속도 제한	속도
    data = [['steep','bumpy','yes','slow'], ['flat','bumpy','no','fast'], ['steep','smooth','no','fast']]
    df = pd.DataFrame(data, columns=['grade', 'bumpiness', 'speed_limit', 'speed'])
    
    dt = DecisionTree(df)
    dt.fit()