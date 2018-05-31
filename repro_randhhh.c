#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include "ulossycount.h"
#include <math.h>

#define COUNTERSIZE k
#define COUNTERS items
#define COUNT parentg->count


#include "hashtable.h"
#include "linked_list.h"
#include "randhhh1D.h"


#ifndef VMULT
#define VMULT 1
#endif

#if VMULT>1
#define PROB
#endif

#ifndef L
#define L NUM_MASKS
#endif

LCU_type * HH[L];

int calcPred(uint32_t prefix, int level, LL **hh_hash_set);
void remove_hh_suffixes(LL **hh_hash_set, uint32_t prefix, int level);

double max(double a, double b) {return (a >= b ? a : b);}

double twototheminus(int k) {
	double ans = 1;
	while (k > 0) {ans /= 2; k--;}
	return ans;
}

void init(double SSepsilon, double prob) {
    //srand(time(NULL));
    srand(3421);
    for (int d = 0; d < L; d++) {
	HH[d] = LCU_Init(max(twototheminus(leveleps[d]), SSepsilon));
    }
}


void deinit() {
    for (int d = 0; d < L; d++) {
	LCU_Destroy(HH[d]);
    }
}

void update(LCLitem_t item, int count) {
    unsigned int d  = (rand() % L);
    LCU_Update(HH[d], (item & masks[d]));
}

HeavyHitter * output(int threshold, int * numhitters, int streamLen) {
    // int hash_table_size = (int) ((double) streamLen/(double) threshold);
    linked_list_t *heavy_hitters_list = ll_create();
    int num_hh = 0;
    int hash_table_size = 1;
    float adj_threshold = threshold/((float) L);
    LL **hh_hash_set = HT_Init(hash_table_size);
    for (int level = 0; level < L; level++) {
	for (int i = 0; i < HH[level]->k; i++) {
	    LCLitem_t item = HH[level]->items[i].item;
	    uint32_t prefix = (item & masks[level]);
	    int upper_estimate = LCU_PointEstUpp(HH[level], item);
	    int conditional_freq = upper_estimate + calcPred(prefix, level, hh_hash_set);
	    conditional_freq += 2*4*sqrt(2*upper_estimate);
	    if (conditional_freq >= adj_threshold) {
		num_hh++;
		HeavyHitter *hh = malloc(sizeof(HeavyHitter));	
		hh->item = item;
		hh->mask = level;
		hh->upper = upper_estimate;
		hh->lower = hh->upper - HH[level]->items[i].delta;
		ll_add(heavy_hitters_list, hh);
		remove_hh_suffixes(hh_hash_set, prefix, level);
		
		HT_Insert(hh_hash_set, prefix, LCU_PointEstLow(HH[level], item), hash_table_size);
	    }
	}
    }
    
    HeavyHitter *output = (HeavyHitter *) calloc(sizeof(HeavyHitter), num_hh);
    ll_node_t *ll_node = ll_front(heavy_hitters_list);
    assert(num_hh == ll_length(heavy_hitters_list));
    for (int i = 0; i < ll_length(heavy_hitters_list); i++) {
	memcpy(output + i, ll_node->object, sizeof(HeavyHitter));
	free(ll_node->object);
	ll_node = ll_node->next;
    }
    ll_destroy(heavy_hitters_list);
    HT_Clear(hh_hash_set, hash_table_size);
    *numhitters = num_hh;
    return output;
}

int calcPred(uint32_t prefix, int level, LL **hh_hash_set) {
    int r = 0;	
    LL *list = hh_hash_set[0];
    while(list != NULL) {
	uint32_t item = (uint32_t) list->item;
	if ((item & masks[level]) == (prefix & masks[level])) {
	    r -= list->val;
	}
	list = list->next;
    }
    return r;
}

void remove_hh_suffixes(LL **hh_hash_set, uint32_t prefix, int level) {
    LL *list_node = hh_hash_set[0];
    while(list_node != NULL) {
	uint32_t item = (uint32_t) list_node->item;
	if ((item & masks[level]) == (prefix & masks[level])) {
	    if (list_node->prev != NULL) {
		list_node->prev->next = list_node->next;
	    } else {
		hh_hash_set[0] = list_node->next;
	    }
	    if (list_node->next != NULL)
		list_node->next->prev = list_node->prev;
	    LL *trash = list_node;
	    list_node = list_node->next;
	    free(trash);
	}
	else {
	    list_node = list_node->next;
	}
    }
}
