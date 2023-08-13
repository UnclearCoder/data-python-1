import numpy as np

def calculate(list):
    try:
        calc = np.array(list).reshape(3,3)
    except ValueError:
        raise ValueError("List must contain nine numbers.")
    
    calculation  = {
        'mean': None,
        'variance': None,
        'standard deviation': None,
        'max': None,
        'min': None,
        'sum': None
    }
    calculation['mean'] = mean(calc)
    calculation['variance'] = variance(calc)
    calculation['standard deviation'] = standard_deviation(calc)
    calculation['max'] = max(calc)
    calculation['min'] = min(calc)
    calculation['sum'] = sum(calc)
    return calculation

def mean(data):
    dt1 = data.mean(axis=0).tolist()
    dt2 = data.mean(axis=1).tolist()
    dt3 = data.mean().tolist()
    return [dt1, dt2, dt3]

def variance(data):
    dt1 = data.var(axis=0).tolist()
    dt2 = data.var(axis=1).tolist()
    dt3 = data.var().tolist()
    return [dt1, dt2, dt3]

def standard_deviation(data):
    dt1 = data.std(axis=0).tolist()
    dt2 = data.std(axis=1).tolist()
    dt3 = data.std().tolist()
    return [dt1, dt2, dt3]

def max(data):
    dt1 = data.max(axis=0).tolist()
    dt2 = data.max(axis=1).tolist()
    dt3 = data.max().tolist()
    return [dt1, dt2, dt3]

def min(data):
    dt1 = data.min(axis=0).tolist()
    dt2 = data.min(axis=1).tolist()
    dt3 = data.min().tolist()
    return [dt1, dt2, dt3]

def sum(data):
    dt1 = data.sum(axis=0).tolist()
    dt2 = data.sum(axis=1).tolist()
    dt3 = data.sum().tolist()
    return [dt1, dt2, dt3]


if __name__ == '__main__':
    result = calculate([0,1,2,3,4,5,6,7,8])
    print(result['max'])
    print(result['min'])
    print(result['sum'])