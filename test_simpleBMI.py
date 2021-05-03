import simpleBMI

def test_calculateBMI():
    assert simpleBMI.calculateBMI(1,1) > 0
    assert simpleBMI.calculateBMI(1,1) is float or int
    assert simpleBMI.calculateBMI(999,999) > 0
    
def test_classifyBMI():
    assert simpleBMI.classifyBMI(40, 20, 'f') == 'You are severely obese.'
    