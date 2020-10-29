import huffman_answer
import huffman

code_dict_answer, entropy_answer = huffman_answer.getAnswer()
code_dict, entropy = huffman.huffmancode("santaclaus.txt")

def test_huffman():
    assert code_dict_answer==code_dict
    
def test_entropy():
    assert entropy_answer==entropy
