#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Pickle Cache, Tasks 4-10"""


import os
import pickle


class PickleCache(object):
    '''Pickles are delicious with sandwiches'''
    # __file_path = self.file_path
    _PickleCache__file_object = None
    _PickleCache__data = {}

    def __init__(self, file_path='datastore.pkl'):
        self._PickleCache__file_path = file_path

    def set(self, key, value):
        '''Adds pairs to the data dict'''
        self._PickleCache__data[key] = value

    def get(self, key):
        '''Gets key pair from data dict, or returns an error'''
        if key in self._PickleCache__data:
            return self._PickleCache__data[key]
        else:
            print "Error: No value found for key '{}'".format(key)

    def delete(self, key):
        '''Deletes a key from the data dict'''
        if key in self._PickleCache__data:
            del self._PickleCache__data[key]

    def open(self):
        '''Opens file path if it is not empty'''
        if os.path.exists(self._PickleCache__file_path):
            if os.path.getsize(self._PickleCache__file_path) > 0:
                self._PickleCache__data = pickle.load(
                    open(self._PickleCache__file_path))
                self._PickleCache__file_path.close()
        open(self._PickleCache__file_path, 'wb')

    def flush(self, reopen=True):
        '''save stored data'''
        # pickle.dump(data, file)
        pickle.dump(self._PickleCache__data, self._PickleCache__file_object)
        self._PickleCache__file_object.close()
        if reopen:
            self.open()

    def close(self):
        '''closes files'''
        self.flush(reopen=False)