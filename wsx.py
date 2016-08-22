# -*- coding: utf-8 -*-
# !/usr/bin/env python3
'''多态'''
__auhtor__ = 'wushengxuan'
class Animal:
	def run(self):
		print('animal is running')

class Dog(Animal):
	def run(self):
	    print('dog is running')
		

class Cat(Animal):
	aa = 2
	__haha = 1
	__xixi = 'wsx'
	def get(self):
		return self.__haha
	def run(self):
		print('cat is runing')

def run_tow(Animal):
	Animal.run()
	Animal.run()


class Student(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def addbirth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
s = Student()
s.addbirth = 1
print(s.birth)