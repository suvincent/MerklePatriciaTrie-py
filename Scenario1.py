
# Testcase: Root Hash = 5838ad5578f346f40d3e6b71f9a82ae6e5198dd39c52e18deec63734da512055
testcase5 = {'a711355' : '45', 'a77d337' : '1', 'a7f9365' : '2', 'a77d397' : '12'}
                                                                      #/                
from MPT import MerklePatriciaTrie

Tests = []
Tests.append(testcase5)
for Test in Tests:
    Tree = MerklePatriciaTrie()
    for item in Test:
        Tree.AddNode(item,Test[item])
    Tree.print()
