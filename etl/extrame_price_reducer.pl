#!/usr/bin/env perl
use strict;
use warnings;

use DateTime;

&reducer();

sub get_agau_day {
    my $day_str = $_[0];   
    my $time = $_[1];
    my($year, $month, $day) = split '-',$day_str;
    my($hour, $minute, $second) = split ':',$time;
    my $dt = DateTime->new(
        year => $year,
	month => $month,
	day => $day,
	hour => $hour,
	minute => $minute,
	second => $second,
	time_zone => 'Asia/Shanghai',
    );
    if($dt->hour < 8){
        $dt = $dt->add(days => -1);	
    }
    return $dt->ymd('-');
}

sub reducer {
    my %maxs = {};
    my %mins = {};
    while(<>){
        chomp;
	my($price, $day_str, $time) = (split /\s/)[1, -2, -1];
        if($time ~= /\A(0|1)/){
	    my $day = &get_agau_day($day_str, $time);
            $maxs{$day} = $price if(not exists $maxs{$day} || $price gt $max{$day});
	    }
    }
    print sort %maxs;
}

