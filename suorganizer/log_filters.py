# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:11:32 2017

@author: user
"""
from logging import Filter
from pprint import pprint

class ManagementFilter(Filter):
    
    def filter(self, record):
        if (hasattr(record, 'funcName')
                and record.funcName== 'execute'):
            return False
        else:
            return True
    
