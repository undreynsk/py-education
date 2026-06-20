use strict;

use Data::Dumper;
use Text::CSV_XS qw( csv );

# Read whole file in memory
my $wage = csv( in => 'C:\\prj\\py\\2023-10-22-task-1\\wage-1-ee13a6b1-605e-44fe-83a6-85d3d7a0b3ae-2873619c-9efe-44e2-932a-f6fed7be056b.csv' );    # as array of array
my $bonus = csv( in => 'C:\\prj\\py\\2023-10-22-task-1\\bonus-1-c177edc7-6e8e-4e53-8f5d-098bd95cc4de-e6e1e463-001c-49ff-adc4-ef6500457b1e.csv' 
	, sep_char => ";");

my %people = ();

my $dup = 0;
my $dup_different_wages = 0;

for my $h ( @$wage ) {
	if ( $h->[0] eq 'person_id' ) {
		next;
	}

	if ( ! ( $h->[2] > 0 ) ) {
		print "No wage found " . Dumper( $h );
		next;
	}

	my @p = @$h;

	if ( exists $people{$p[0]} ) {
		if ( $people{$p[0]}->[2] != $p[2] ) {
			#print "Found duplicate with the different wages!\n";
			$dup_different_wages++;
		}
		else {
			#print "Found duplicate with the same wages!\n";
			$dup++;
		}
		#print Dumper( $people{$p[0]} ) . Dumper( \@p ) . "\n"; 
	}

	$people{$p[0]} = \@p;
}

print "Duplicates with different wages: $dup_different_wages\n"
	. "Duplicates with the same wages: $dup\n";

for my $h ( @$bonus ) {
	if ( $h->[0] eq 'person_id' ) {
		next;
	}

	my @p = @$h;

	if ( exists $people{$p[0]} ) {
		$people{$p[0]}->[3] = $p[1];
		$people{$p[0]}->[4] = $people{$p[0]}->[2] + $p[1];
	}
}

my %sum;
my $men; 
my $women;

for my $k ( keys %people ) {
	$people{$k}->[4] ||= $people{$k}->[2];

	if ( $people{$k}->[1] == 0 ) {
		$women++;
	}
	else {
		$men++;
	}
	$sum{$people{$k}->[1]} += $people{$k}->[4];
}

print "Men, women: $men, $women\n";
print Dumper( \%sum );
print "Average woman (was 1390227.43044448): " . ( ( $sum{0} / $women )  * 12 ) ."\n";

my @wages_man = 
	sort { $a <=> $b }
	map { $people{$_}->[4] * 12 }
	grep $people{$_}->[1] == 1
	, keys %people;

print Dumper( \@wages_man );

print int($#wages_man / 2) . "\n"; 
print "Median man: " . $wages_man[251] . "\n";	
print "Median man: " . $wages_man[int(scalar( @wages_man ) / 2)] . "\n";	
print "Median man: " . $wages_man[int(scalar( @wages_man ) / 2) + 1] . "\n";	


#print Dumper( \@wages_man );

=comment
# Write array of arrays as csv file
csv (in => $aoa, out => "file.csv", sep_char=> ";");

# Only show lines where "code" is odd
csv (in => "data.csv", filter => { code => sub { $_ % 2 }});


# Object interface
use Text::CSV_XS;

my @rows;
# Read/parse CSV
my $csv = Text::CSV_XS->new ({ binary => 1, auto_diag => 1 });
open my $fh, "<:encoding(utf8)", "test.csv" or die "test.csv: $!";
while (my $row = $csv->getline ($fh)) {
 $row->[2] =~ m/pattern/ or next; # 3rd field should match
 push @rows, $row;
 }
close $fh;

# and write as CSV
open $fh, ">:encoding(utf8)", "new.csv" or die "new.csv: $!";
$csv->say ($fh, $_) for @rows;
close $fh or die "new.csv: $!";
=cut