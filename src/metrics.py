def sharpe_ratio(returns):
    import numpy as np
    return (returns.mean() / returns.std()) * (252**0.5)