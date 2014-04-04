#!/usr/bin/env perl
use strict;
use warnings;

sub main {
    while(my $line = <STDIN>) {
        chomp $line;
        my @items = split '\t', $line;
	print $items[-1]."\t";
	for(my $i = 1; $i < @items; $i++) {
	    print $i.':'.$items[$i - 1]."\t";
	}
	print "\n";
    }
}

&main
