#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'mercury'

'object oriented programming'


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def printScore(self):
        print('%s:%s' % (self.name, self.score))

    def getGrade(self):
        if self.score >= 90:
            print('A')
            return
        elif self.score >= 80 and self.score < 90:
            print('B')
            return
        else:
            print('bad')
            return



# 注意这里不需要进行new Student实例化类
jackMa = Student('jackMa', 0)
ponyMa = Student('ponyMa', 80)

jackMa.printScore()
jackMa.getGrade()
ponyMa.printScore()
ponyMa.getGrade()
