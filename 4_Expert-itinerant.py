#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# @Author: Adrien Chardon
# @Date: 2014-11-16 14:29:10
# @Last Modified by: Adrien Chardon
# @Last Modified time: 2014-11-16 16:31:32

import time as t

################################################################################
# Usefull functions
################################################################################

# big number
infinity = 1000


# wrapper
def getObjectInList(nodes, id):
    return nodes[id-1]


# Return all childs nodes that can be directly accessed from the node
def getChildOfNode(data, node):
    ret = []
    for dic in data:
        if dic['start'] == node:
            ret.append(dic['end'])
    return ret


# return the time for traveling directly from node1 to node 2
def getDist(data, node1, node2):
    for dic in data:
        if (dic['start'] == node1) and (dic['end'] == node2):
            return dic['time']
    return infinity


################################################################################
# main
################################################################################
 
# get the time for one request
def expert_itinerant_one(nb_node, nb_link, nb_request, data, start, end):
    nodes = []
    for _ in range(nb_node):
        tmp = {
            'distanceFromStart': infinity,
            'origin': -1,
        }
        nodes.append(tmp)

    getObjectInList(nodes, start)['distanceFromStart'] = 0
    getObjectInList(nodes, start)['origin'] = 0
    
    notVisited = [start]
    
    while notVisited != []:
        cur_id = notVisited.pop()
        cur = getObjectInList(nodes, cur_id)
        
        for child_id in getChildOfNode(data, cur_id):
            child = getObjectInList(nodes, child_id)
            if (child['origin'] == -1) or (cur['distanceFromStart'] + getDist(data, cur_id, child_id) < child['distanceFromStart']):
                child['distanceFromStart'] = cur['distanceFromStart'] + getDist(data, cur_id, child_id)
                child['origin'] = cur_id
                if child_id not in notVisited:
                    notVisited.append(child_id)
    
    return getObjectInList(nodes, end)['distanceFromStart']
    

def expert_itinerant(nb_node, nb_link, nb_request, data, request):
    for dic in request:
        print expert_itinerant_one(nb_node, nb_link, nb_request, data, dic['start'], dic['end'])


if __name__ == '__main__':
    nb_node, nb_link, nb_request = (int(i) for i in raw_input().split())
    
    data = []
    for _ in range(nb_link):
        start, end, time = (int(i) for i in raw_input().split())
        tmp = {
            'start': start,
            'end': end,
            'time': time,
        }
        data.append(tmp)
    data.sort(key=lambda tup: tup['start'])
        
    request = []
    for _ in range(nb_request):
        start, end = (int(i) for i in raw_input().split())
        tmp = {
            'start': start,
            'end': end,
        }
        request.append(tmp)
    
    expert_itinerant(nb_node, nb_link, nb_request, data, request)
