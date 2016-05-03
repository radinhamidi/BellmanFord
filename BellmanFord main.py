# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 09:52:37 2015

@author: ..::/RADIN\::..

"""
import numpy as np
cnt=int(input("PLease enter number of routers : "))
x=np.full((cnt,cnt),100,int)
k=np.full((1,cnt,cnt,cnt),100,int)

def upd_routs(o):
    temp=np.full((1,cnt,cnt,cnt),100)
    for i in range(cnt):
        for j in range(cnt): 
            if i!=j :   
                if o[o.shape[0]-1,i,i,j]==100 :
                    temp[0,i,j,:]=100
                else: 
                    temp[0,i,j,:]=o[o.shape[0]-1,j,j,:]   
            else:
                for t in range(cnt):
                    if t==i :
                        temp[0,i,i,t]=0
                    else :
                        temp[0,i,i,t]=100
                        for u in range(cnt):
                            if  (o[o.shape[0]-1,i,i,u]+o[o.shape[0]-1,u,u,t])<temp[0,i,i,t]:  
                                temp[0,i,i,t]=(o[o.shape[0]-1,i,i,u]+o[o.shape[0]-1,u,u,t])
    
#    print(o[o.shape[0]-1,:,:,:])
#    print(temp[0,:,:,:])
    if np.array_equal(o[o.shape[0]-1,:,:,:],temp[0,:,:,:]) is False:
         o=np.concatenate((o,temp))
    return o
    
for i in range(cnt):  
    s=input("Fill row number %d of the matrix "%(i+1))
    x[i]=np.fromstring(s,dtype=int, sep=' ')
######### filling the 4D matrix with the raw data #############

for j in range(cnt):
    k[0,j,j,:]=x[j,:]
#print(k)   
######### implementing algorithm  ##################
while 1:
    before_matrix=k.shape[0]
    ## implementing famouse relax() function
    k=upd_routs(k)
    after_matrix=k.shape[0]
#    print (k)
    if after_matrix==before_matrix :
        break

## generating menu
itr=k.shape
itr=itr[0]
while 1:
    print("\nthere are %d iterations and %d routers\n"%(itr,cnt))
    print("-------------------------------------------------------------")
    iteration_pointer=input("Routing finished successfully...\nPlease enter iteration level you want to take a look at.\n")
    router_pointer=input("Enter router number or enter 'a' for overall view.\n")
    if router_pointer=='a' :
        print(k[int(iteration_pointer)-1,:,:,:])
    else:
        print(k[int(iteration_pointer)-1,int(router_pointer)-1,:,:])
    if input("Do you need more report ? (Y/N)").__le__('n') :
        break
