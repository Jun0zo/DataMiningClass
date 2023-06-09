
from collections import deque
import pandas as pd
import math
from typing import List

class Node:
    def __init__(self, data_indexes : List[pd.Index], reason : str ='', tag : str =''):
        self.data_indexes = data_indexes
        self.pointers = []
        self.reason = reason
        self.tag = tag
    
    def add_tag(self, tag : str) -> None:
        self.tag = tag
        
    def append_nodes(self, child_nodes : List['Node']) -> None:
        self.pointers = child_nodes
        
    def get_childnodes(self) -> List['Node']:
        return self.pointers
    
    def get_tag(self) -> str:
        return self.tag
        
    def filter(self, df) -> pd.DataFrame:
        return df.loc[self.data_indexes.tolist()]
    
class Tree:
    def __init__(self):
        self.root_node = None
        
    def dfs_print(self, node : Node = None):
        if node == None:
            node = self.root_node
        
        
        children = node.get_childnodes()
        tag = node.get_tag()
        
        if tag:
            print('node :', tag)
            print('child node : ', [child.get_tag() for child in children])
            print('child node idx : ', [child.data_indexes for child in children])
            print('child node idx : ', [child.reason for child in children])
            print()
        
        for child in children:
            self.dfs_print(child)
        

class DecisionTree(Tree):
    def __init__(self, df : pd.DataFrame):
        super()
        self.data = df
        self.features = list(df)[:-1]
        self.last_features = list(df)[:-1]
        
        self.labels = self.data.iloc[:, -1].values
        self.label_sets = set(self.labels)
        
    def check_feature(self, dst_feature):
        self.last_features = [feature for feature in self.last_features if feature != dst_feature]
        
    def split_with_feature(self, data : pd.DataFrame, feature_name : str):
        print(data)
        # print('===========')
        # print(data[feature_name])
        fact_idxs, fact_col_names = pd.factorize(data[feature_name])
        print(feature_name)
        print(fact_idxs, fact_col_names)
        
        ret = [pd.DataFrame(columns=data.columns) for _ in range(len(fact_col_names))]
        for idx, (row_idx, row) in enumerate(data.iterrows()):
            print(idx)
            fact_idx = fact_idxs[idx]
            ret[fact_idx] = ret[fact_idx].append(row)
        
        return ret
        
    def get_weight(self, subset : pd.DataFrame, feature : str):
        splited_feature = subset[feature].iloc[0]
        cnt = (self.data[feature] == splited_feature).sum()
        return cnt / len(self.data)
        
    def get_entropy(self, subset : pd.DataFrame):
        entropy = 0
        # print(subset)
        for label in self.label_sets:
            # print('~~~~~~~~~~~', label, 'entropy')
            P = (subset.iloc[:, -1] == label).sum() / len(subset)
            print('P :', P)
            if P != 0:
                # print('entrop :', (- P * math.log2(P)))
                entropy += (- P * math.log2(P))
        print('all entropy', entropy)
        return entropy
        
    def make_tree(self, node : Node):
        data = node.filter(self.data)
        parent_entropy = self.get_entropy(data)
        print('pe :', parent_entropy)
        
        max_information_gain = -1e9
        selected_splited_data = []
        selected_feature = ''
        selected_reasons = []
        
        # feature값
        for last_feature in self.last_features:
            splited_data = self.split_with_feature(data, last_feature)
            child_entropy = 0
            # feature로 한번 나누어 봄 (subset : 특정 feature만 있는 데이터)
            print('=============================== divide with', last_feature)
            
            reasons = []
            for subset in splited_data:
                reason = f'{last_feature}  = {subset[last_feature].iloc[0]}'
                reasons.append(reason)
                weighted_entropy = self.get_weight(subset, last_feature) * self.get_entropy(subset)
                print('weightd', weighted_entropy, 'from', self.get_weight(subset, last_feature))
                child_entropy += weighted_entropy
               
            information_gain = parent_entropy - child_entropy
            print('information gain : ', information_gain)
            if information_gain > max_information_gain:
                max_information_gain = information_gain
                selected_splited_data = splited_data
                selected_feature = last_feature
                selected_reasons = reasons
        
        child_nodes = [Node(data.index, reason) for data, reason in zip(selected_splited_data, selected_reasons)]
        node.append_nodes(child_nodes)
        node.add_tag(selected_feature)
        self.check_feature(selected_feature)
        
        return child_nodes
        # information gain 최솟값 찾고 트리만들고
    
    def fit(self):
        root_node = Node(pd.RangeIndex(stop=len(self.data)))
        print('bef :', root_node.filter(self.data))
        nodes = deque([root_node])
        while self.last_features:
            node = nodes.pop()
            new_child_nodes = self.make_tree(node)
            nodes.extend(new_child_nodes)
            print('++++++++++++++++++++++++++++++++++++++++++++++++')
        
        self.root_node = root_node
        
        print()
        self.dfs_print()


if __name__ == '__main__':
    # 경사	표면	속도 제한	속도
    data = [['steep','bumpy','yes','slow'], ['steep','smooth','yes','slow'], ['flat','bumpy','no','fast'], ['steep','smooth','no','fast']]
    # data = [['']]
    df = pd.DataFrame(data, columns=['grade', 'bumpiness', 'speed_limit', 'speed'])
    
    dt = DecisionTree(df)
    dt.fit()