#!/usr/bin/env perl
use strict;
use warnings;

#"$DAY_OF_WEEK"."DateTime->now(time_zone => 'Asia/Shanghai')->hms('')"
my %agau_durations = (
    '1085000' => '1113000',
    '1130000' => '1153000',
    '1205000' => '2023000',
    '2085000' => '2113000',
    '2130000' => '2153000',
    '2205000' => '3023000',
    '3085000' => '3113000',
    '3130000' => '3153000',
    '3205000' => '4023000',
    '4085000' => '4113000',
    '4130000' => '4153000',
    '4205000' => '5023000',
    '5085000' => '5113000',
    '5130000' => '5153000',
    '5205000' => '6023000',
);
my %all_durations = (
    '1085000' => '6235900',
);

sub formated_now {
    use DateTime;
    my $dt = DateTime->now( time_zone => 'Asia/Shanghai',);
    $dt->day_of_week().$dt->hms('')
}

sub valid_time {
    my $now = $_[0];
    my $len = @_;
    my %durations = @_[1..($len - 1)];
    print "\@_: @_, \$now: $now, \%durations: %durations\n";
    for my $k (keys %durations) {
        if (($now ge $k) or ($now le $durations{$k})) {
	    return 1;
	}
    }
    return 0;
}

sub main {
    my $now = &formated_now();
    use 5.010001;
    given ($now) {
        when(&valid_time($now, %agau_durations)) {system("perl spider.pl all;");}
	when(&valid_time($now, %all_durations)) {system("perl spider.pl paper;")}
	default {print "Not a valid time for working.";}
    }
} 

&main;

