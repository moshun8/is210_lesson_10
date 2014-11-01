#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Pickle Cache, Tasks 4-10"""


import os
import pickle


class PickleCache(object):
    '''Pickles are delicious with sandwiches'''
    # __file_path = self.file_path
    __file_object = None
    __data = {}

    def __init__(self, file_path='datastore.pkl'):
        self.file_path = file_path


    def set(self, key, value):
        '''Adds pairs to the data dict'''
        __data[key] = value


    def get(self, key):
        '''Gets key pair from data dict, or returns an error'''
        if key in self.__data:
            return key
        else:
            print "Error: No value found for key '{}'".format(key)


    def delete(self, key):
        '''Deletes a key from the data dict'''
        if key in self.__data:
            del self.__data[key]


    def open(self):
        '''Opens file path if it is not empty'''
        if os.path.exists(self.__file_path):
            if os.path.getsize(self.__file_path) > 0:
                self.__data = pickle.load(self.__file_path)
                self.__file_path.close()
        open(self.__file_path, 'w')


    def flush(self, reopen=True):
        '''save stored data'''
        pickle.dump(reopen, self.__file_object)
        self.__file_object.close()
        if reopen == True:
            self.open()


    def close(self):
        '''closes files'''
        self.flush(reopen=False)