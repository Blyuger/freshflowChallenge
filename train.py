{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.preprocessing import OneHotEncoder\n",
    "from sklearn.model_selection import TimeSeriesSplit\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "from sklearn.tree import DecisionTreeRegressor\n",
    "from sklearn.ensemble import AdaBoostRegressor\n",
    "from sklearn.svm import SVR\n",
    "from sklearn.pipeline import make_pipeline\n",
    "from sklearn.model_selection import GridSearchCV\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "\n",
    "from sklearn import metrics\n",
    "from sklearn import preprocessing\n",
    "from sklearn.preprocessing import scale\n",
    "from sklearn.metrics import *\n",
    "from itertools import product\n",
    "import seaborn as sns\n",
    "import statsmodels.api as sm\n",
    "import warnings\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import matplotlib as mpl\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import os\n",
    "import pandas as pd\n",
    "import pickle\n",
    "\n",
    "warnings.filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "run_control": {
     "marked": false
    }
   },
   "outputs": [],
   "source": [
    "def train_arima (x, y, p, q, d):\n",
    "    \n",
    "    arima = sm.tsa.statespace.SARIMAX(x.values,order=(p, q, d)).fit()\n",
    "    pred = pd.DataFrame(arima.forecast(steps=y.shape[0])[0:])\n",
    "    \n",
    "    return arima"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "run_control": {
     "marked": true
    }
   },
   "outputs": [],
   "source": [
    "model = train_arima(x, y, p, q, d)\n",
    "\n",
    "with open('model_pkl', 'wb') as files:\n",
    "    pickle.dump(model, files)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
