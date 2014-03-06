#!/usr/bin/env python

import sys
import random
import math

def randomoptimize(domain, costf):
    best = sys.maxint
    best_resolve = None
    for i in range(1000000):
        resolve = [random.randint(domain[j][0], domain[j][1]) for j in range(len(domain))]
	cost = costf(resolve)

	if cost < best:
	    best = cost 
	    best_resolve = resolve
#        print 'round: %d, cost: %s, resolve: %s' % (i, cost, resolve)
#    print 'BEST -- cost: %s, resolve: %s' % (best, best_resolve)
    return best,best_resolve

def hill_climb(domain, costf):
    best_resolve = [random.randint(domain[j][0], domain[j][1]) for j in range(len(domain))]
    i = 0
    while(i < 1000000):
	neighbors = []
	for j in range(len(domain)):
	    if best_resolve[j] > domain[j][0]:
	        neighbors.append(best_resolve[0:j] + [best_resolve[j] - 1] + best_resolve[j + 1:])
	    if best_resolve[j] < domain[j][1]:
	        neighbors.append(best_resolve[0:j] + [best_resolve[j] + 1] + best_resolve[j + 1:])

        last_cost = costf(best_resolve)
	best_cost = last_cost
	for j in range(len(neighbors)):
	    current_cost = costf(neighbors[j])
	    if current_cost < best_cost:
	        best_cost = current_cost
		best_resolve = neighbors[j]
	if best_cost == last_cost:
	    break
	
	i += 1
	if i % 10000 == 0:
            print 'i: %s, cost: %s, resolve: %s' % (i, best_cost, best_resolve)
    return best_cost, best_resolve

def annealing(domain, costf, T=100000, cool=0.98, step=1):
    resolve = [random.randint(domain[j][0], domain[j][1]) for j in range(len(domain))]
    while(T > 0.1):
        i = random.randint(0, len(domain) - 1)
        delta = random.randint(0 - step, step)
	resolve_new = resolve[:]
        resolve_new[i] += delta
	if resolve_new[i] < domain[i][0]:
	    resolve_new[i] = domain[i][0]
	if resolve_new[i] > domain[i][1]:
	    resolve_new[i] = domain[i][1]
	
        cost_old, cost_new = costf(resolve), costf(resolve_new)
	if cost_old > cost_new or random.random() < pow(math.e, (cost_old - cost_new)/T):
	    resolve = resolve_new
	T *= cool
    return cost_old,resolve

def genetic_optimize(domain, costf, resolve_size=50,muteprob=0.2,step=1,elite=0.2,maxiter=100):
    def mutate(resolve):
        i = random.randint(0, len(resolve) - 1)
	if random.random() < 0.5 and resolve[i] > domain[i][0]:
	    resolve[i] -= 1
	elif resolve[i] < domain[i][1]:
	    resolve[i] += 1
	return resolve

    def crossover(ra, rb):
        i = random.randint(0, len(domain) - 1)
	return ra[0:i] + rb[i:]

    resolves = [[random.randint(domain[j][0], domain[j][1]) for j in range(len(domain))] for i in range(resolve_size)]
    elite_size = int(elite * resolve_size)
    for i in range(maxiter):
        scores = [(costf(r), r) for r in resolves]
	scores.sort()
        ranked = [v for (s,v) in scores]
        resolves = ranked[0:elite_size]
	while len(resolves) < resolve_size:
            if random.random() < muteprob:
	        c = random.randint(0, elite_size)
		resolves.append(mutate(ranked[c]))
	    else:
	        c1 = random.randint(0, elite_size)
	        c2 = random.randint(0, elite_size)
		resolves.append(crossover(ranked[c1], ranked[c2]))
    return scores[0][0],scores[0][1]

