from montecarlo import MonteCarlo

seed = 42
samples = 1000000

def target_function_L(random_vector):

    L = 1
    
    x = random_vector[0]
    y = random_vector[1]
    
    x2 = x * x
    y2 = y * y
    L2 = L * L
    xL2 = (x - L) * (x - L)
    yL2 = (y - L) * (y - L)
    
    c1 = x2  + y2  <= L2
    c2 = xL2 + y2  <= L2
    c3 = x2  + yL2 <= L2
    c4 = xL2 + yL2 <= L2

    tc = c1 and c2 and c3 and c4
    
    return 1 if tc else 0


mc = MonteCarlo(seed,samples,target_function_L,2)
print(mc.run())


def target_function(random_vector):
    '''
    Function receives a uniform random vector in [0]
    '''
    x = random_vector[0]
    y = random_vector[1]
    c1 = x + y < 1
    return 1 if c1 else 0

samples = 10000    
mc = MonteCarlo(seed,samples,target_function,2)
print(mc.run())
