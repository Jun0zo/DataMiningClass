
from collections import deque
import pandas as pd
import math
from typing import List
import random

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
        
    def dfs_print(self, node : Node = None) -> None:
        if node == None:
            node = self.root_node
        
        children = node.get_childnodes()
        tag = node.get_tag()
        
        if tag:
            print('node :', tag)
            print('child node : ', [child.get_tag() for child in children])
            print('child node idx : ', [child.data_indexes for child in children])
            print('child node reason : ', [child.reason for child in children])
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
        fact_idxs, fact_col_names = pd.factorize(data[feature_name])
        
        ret = [pd.DataFrame(columns=data.columns) for _ in range(len(fact_col_names))]
        for idx, (row_idx, row) in enumerate(data.iterrows()):
            print(idx)
            fact_idx = fact_idxs[idx]
            ret[fact_idx] = ret[fact_idx].append(row)
        
        return ret
        
    def get_weight(self, subset : pd.DataFrame, feature : str):
        # 전체 데이터 중에 해당 feature의 비율을 return 하는 함수
        splited_feature = subset[feature].iloc[0]
        cnt = (self.data[feature] == splited_feature).sum()
        return cnt / len(self.data)
        
    def get_entropy(self, subset : pd.DataFrame):
        # 해당 데이터셋의 엔트로피를 구하는 함수
        entropy = 0
        for label in self.label_sets:
            P = (subset.iloc[:, -1] == label).sum() / len(subset)
            print('P :', P)
            if P != 0:
                entropy += (- P * math.log2(P))
        return entropy
        
    def make_tree(self, node : Node):
        data = node.filter(self.data)
        parent_entropy = self.get_entropy(data)
        
        max_information_gain = -1e9
        selected_splited_data = []
        selected_feature = ''
        selected_reasons = []
        
        # feature값
        for last_feature in self.last_features:
            splited_data = self.split_with_feature(data, last_feature)
            child_entropy = 0
            # feature로 한번 나누어 봄 (subset : 특정 feature만 있는 데이터)
            
            reasons = []
            for subset in splited_data:
                reason = f'{last_feature}  = {subset[last_feature].iloc[0]}'
                reasons.append(reason)
                weighted_entropy = self.get_weight(subset, last_feature) * self.get_entropy(subset)
                child_entropy += weighted_entropy
               
            information_gain = parent_entropy - child_entropy
            
            # information gain의을 최솟값 찾는 과정
            if information_gain > max_information_gain:
                max_information_gain = information_gain
                selected_splited_data = splited_data
                selected_feature = last_feature
                selected_reasons = reasons
        
        # information gain이 최소인 노드를 기존 노드에 추가 
        child_nodes = [Node(data.index, reason) for data, reason in zip(selected_splited_data, selected_reasons)]
        node.append_nodes(child_nodes)
        node.add_tag(selected_feature)
        self.check_feature(selected_feature)
        
        return child_nodes
        
    
    def fit(self):
        root_node = Node(pd.RangeIndex(stop=len(self.data)))
        print('bef :', root_node.filter(self.data))
        nodes = deque([root_node])
        
        # 모든 feature로 트리를 만듬
        while self.last_features:
            node = nodes.pop()
            new_child_nodes = self.make_tree(node)
            nodes.extend(new_child_nodes)
        
        self.root_node = root_node
        
        self.dfs_print()

class RandomRorest:
    def __init__(self, df : pd.DataFrame, memory=5):
        # memory 개수만큼 의사결정트리 생성
        trees = [DecisionTree(self.data_sampling(df)) for _ in range(memory)]
        
    def data_sampling(self, df : pd.DataFrame):
        total_rows = df.shape[0]
        # 전체 데이터의 63 %를 랜덤으로 추출
        random_indices = random.sample(range(total_rows), int(total_rows * 0.63))
        random_rows = df.iloc[random_indices]
        
        sampled = pd.DataFrame(random_rows)
        return sampled
    
    def fit(self):
        # 생성된 의사결정트리 모두 학습
        for tree in self.trees:
            tree.fit()

if __name__ == '__main__':
    
    data = [
        ['steep','bumpy','yes','slow'], 
        ['steep','smooth','yes','slow'], 
        ['flat','bumpy','no','fast'], 
        ['steep','smooth','no','fast']
    ]
    
    # 경사	표면	속도 제한	속도
    df = pd.DataFrame(data, columns=['grade', 'bumpiness', 'speed_limit', 'speed'])
    
    dt = DecisionTree(df)
    dt.fit()
    