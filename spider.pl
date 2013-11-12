#!/usr/bin/env perl
use strict;
use warnings;

use LWP::UserAgent;
use DateTime;

our $ADDR = 'http://www.icbc.com.cn/ICBCDynamicSite/Charts/GoldTendencyPicture.aspx';

sub httpget {
    # print "\$_ : @_";
    my $user_agent = new LWP::UserAgent;
    my $request = new HTTP::Request('GET', @_);
    my $response = $user_agent->request($request);
    $response->content;
}

sub now {
    use DateTime;
    my $dt = DateTime->now( time_zone => 'Asia/Shanghai',);
    # '%04d-%02d-%02d %02d:%02d:%02d', $dt->year, $dt->month, $dt->day, $dt->hour, $dt->minute, $dt->second;
    $dt->ymd." ".$dt->hms;
}

sub epoch {
    my $dt = DateTime->from_epoch(epoch => time);
    $dt->epoch;
}

sub d {
    print STDERR $_;
}

# 人民币账户黄金  251.43  252.23  251.83  252.42  251.44  
# 人民币账户白银  4.18    4.22    4.20    4.21    4.17    
# 人民币账户铂金  281.48  283.88  282.68  282.97  282.09  
# 人民币账户钯金  147.24  149.64  148.44  148.73  148.14  
# 美元账户黄金    1284.50 1287.50 1286.00 1288.98 1283.95 
# 美元账户白银    21.36   21.51   21.44   21.51   21.30   
# 美元账户铂金    1437.50 1449.50 1443.50 1445.00 1440.50 
# 美元账户钯金    752.00  764.00  758.00  759.50  756.50  
# Ag(T+D) 4298.00 -1.19%  1731702 4364.00 4364.00 4392.00 4280.00 2013-11-09 02:30:00     
# Au(T+D) 253.38  -1.50%  19210   257.45  257.34  258.10  253.00  2013-11-09 02:29:55     
# Au100g  255.00  -1.16%  416     258.00  258.01  258.00  253.60  2013-11-09 02:29:59     
# Au99.95 180.77  0.00%   0       0.00    257.42  0.00    0.00    2013-11-09 02:29:59     
# Au99.99 253.90  -1.40%  13570   257.00  257.52  257.94  252.10  2013-11-09 02:29:55

my $paper_records = 8;
my $paper_length = 6;
my $agau_length = 9;
sub persist_paper {
    open PAPER, '>>', 'paper.dat';
    # &d("\@_: @_");
    my $len = @_;
    my @data = @_[0..$len-2];
    my $appendix = $_[-1];
    # print "\@data: @data, \$appendix: $appendix\n";
    for (my $i = 0; $i < ($#data + 1) / $paper_length; $i++) {
    	my $line = join("\t", @data[($i * $paper_length)..(($i + 1) * $paper_length - 1)]);
        $line .= "\t".$appendix;
        print PAPER $line."\n";
    }
    close PAPER;
}

sub persist_agau {
    my @data = @_;
#    print "\n\@data: @data";
    open AGAU, '>>', 'agau.dat';
    for (my $i = 0; $i < @data / $agau_length; $i++) {
        my $line = join("\t", @data[($i * $agau_length)..(($i + 1) * $agau_length - 1)]);
        chomp $line;
        print AGAU $line."\n";
    }
    close AGAU;
}

sub print_usage {
    print "Usage:\n";
    print "\t./$0 (all|paper|agau)\n";
    return -1;
}

sub main {
    my $content = &httpget($ADDR);
    # print "\$content------------------------------------------------------\n$content";
    my @matched = ($content =~ m{<td style=\"[^>]+\">\s+(?<item>[^>]*?)\s+</td>}sig);
    my $timestamp = &now();
    print join("\t", @matched), "\n";
    use 5.010001;
    given ( $ARGV[0] ) {
    	# when('all') {&persist_all(@matched, $timestamp);}
    	when(/(paper|all)/) {&persist_paper(@matched[0..$paper_length * $paper_records -1], $timestamp);continue}
    	when(/(agau|all)/) {&persist_agau(@matched[$paper_length * $paper_records..(@matched-1)]);}
    	default {return &print_usage;}
    }
}

&main;

