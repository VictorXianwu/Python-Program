# -*- coding: GBK -*-
#! /usr/bin/python

a = [0.25, 0.5, 0.25] #AA��Aa��aa�ĳ�ʼ����Ϊ1:2:1
loop = 100
print "Calculate The Effect Of Removing The Recessive Gene"
print"Num\t\tAA\tAa"

for i in range ( 1, loop ) :
#ȥ�����Ը���
    a[2] = 0
    a[1] = a[1] / ( a[1] + a[0] )
    a[0] = a[0] / ( a[1] + a[0] )

#��ӡ������ֵ
    print "Num ", i, ":\t%.3f" % a[0], "\t%.3f" % a[1]

#����Ӻ���С��0.05��ֹͣ����
    if a[1] <= 0.05:
        print "Total", i ,"steps."
        break

#�Ŵ�
    a[0] = ( a[0] * a[0] ) + ( a[0] * a[1] )
    a[1] =                 ( a[0] * a[1] )
    a[2] =                               ( a[1] * a[1] )
