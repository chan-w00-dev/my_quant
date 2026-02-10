import pandas as pd
import numpy as np

a = np.random.randint(0,10,24).reshape(4,6)
df = pd.DataFrame(a, index=list("가나다라"), columns=list("ABCDEF"))

print(df)