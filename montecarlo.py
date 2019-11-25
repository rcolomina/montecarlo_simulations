
import random


class MonteCarlo(object):
    '''
    
    '''
    def __init__(self,rand_seed, num_samples, target_func, dimensions):
        
        self.rand_seed = rand_seed
        self.num_samples = num_samples
        self.target_func = target_func
        self.dimensions = dimensions

        # TODO: Assert function should admit random vector
    def run(self):

        '''
        This runs experiments onto the target functions over a number of random samples
        
        '''
        pos_cases = 0
        random.seed(self.rand_seed)
        for experiment in range(0,self.num_samples):
            random_vector = [random.random() for _ in range(0,self.dimensions)]
            pos_cases += self.target_func(random_vector)
        return pos_cases / self.num_samples
            
