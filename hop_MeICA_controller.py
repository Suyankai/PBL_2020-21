from numpy.lib.function_base import append
from hop_MeICA_newton_iteration import hop_MeICA_newton_iteration
from pyfastbss_core import PyFastbss, pyfbss,MultiLevelExtractionICA
from pyfastbss_testbed import pyfbss_tb
from hop_B_Manager import hop_B_Manager
from hop_Source_controller import hop_Source_controller
import numpy as np
import os
import math
import progressbar
import time
class hop_MeICA_controller:
    def __init__(self, max_iter, tol, break_coef, ext_multi_ica, source_controller:hop_Source_controller, b_manager:hop_B_Manager) -> None:
        super().__init__()
        self.max_iter=max_iter
        self.tol=tol
        self.break_coef=break_coef
        self.ext_multi_ica=ext_multi_ica
        self.source_controller=source_controller
        self.b_manager=b_manager
        self.X=source_controller.get_X()
        # 用于获取每个节点的运行时间
        self.runtime_list=[]
        # 用于获取每个节点的迭代次数
        self.iter_list=[]
        # 用于获取迭代节点的个数
        self.grad=0


    def get_hat_S(self):
        
        n, m = self.X.shape
        _grad = int(math.log(m//n, self.ext_multi_ica))
        _prop_series = self.ext_multi_ica**np.arange(_grad, -1, -1)
        for i in range(1, _grad+1):
            time_before=time.time()
            B_temp=self.b_manager.get_B()
            _X = self.X[:, ::_prop_series[i]]
            _X, V, V_inv = pyfbss.whiten_with_inv_V(_X)
            B_temp = pyfbss.decorrelation(np.dot(B_temp, V_inv))
            self.MeICA_newton_itertion=hop_MeICA_newton_iteration(self.max_iter,self.tol,self.break_coef,self.ext_multi_ica,_X,B_temp)
            B_temp,lim,iter_num=self.MeICA_newton_itertion.meica_newton_iteration_autobreak()
            B_temp = np.dot(B_temp, V)
            self.b_manager.update_B(B_temp,None)
            time_after=time.time()
            # 用于统计的赋值不应该算在时间里
            self.iter_list.append(iter_num)
            # 计算本次的时间，并加入到list中
            self.runtime_list.append(time_after-time_before)
            # 赋值grad
            self.grad=_grad

        self.hat_S = np.dot(self.b_manager.get_B(), self.X)
        return self.hat_S 

    def get_runtime_list(self):
        return self.runtime_list
    
    def get_iter_list(self):
        return self.iter_list

    def get_grad(self):
        return self.grad

