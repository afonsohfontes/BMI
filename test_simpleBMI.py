import simpleBMI

def test_calculateBMI():
    t1 = simpleBMI.BMICalc(1, 1, 1, 1)
    assert t1.calculateBMI(1,1) > 0
    assert t1.calculateBMI(1,1) is float or int
    assert t1.calculateBMI(999,999) > 0
    
def test_classifyBMI():
    t2 = simpleBMI.BMICalc(180, 180, 20, 'f')
    assert t2.classifyBMI() == 'You are severely obese.'
    
    