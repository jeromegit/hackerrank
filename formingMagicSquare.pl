#!/usr/bin/perl
use strict;
use warnings;

use Test::More "no_plan";
use POSIX;

# Vector version of all 3x3 magic squares
# Source: http://www.dr-mikes-math-games-for-kids.com/3x3-magic-square.html
my @allMagicSquares = (
                       [qw(2 7 6 9 5 1 4 3 8)],
                       [qw(2 9 4 7 5 3 6 1 8)],
                       [qw(4 3 8 9 5 1 2 7 6)],
                       [qw(4 9 2 3 5 7 8 1 6)],
                       [qw(6 1 8 7 5 3 2 9 4)],
                       [qw(6 7 2 1 5 9 8 3 4)],
                       [qw(8 1 6 3 5 7 4 9 2)],
                       [qw(8 3 4 1 5 9 6 7 2)],
                      );

# Complete the formingMagicSquare function below.
sub formingMagicSquare {
   my($s) = @_;

   my @values = (map{@{$s->[$_]}} 0..2);  # turn 2D matrix into vector

   my $minDiff = POSIX::UINT_MAX;
   foreach my $ms (@allMagicSquares) {
      my $diff = 0;
      foreach my $i (0..8) {
         $diff += abs($ms->[$i] - $values[$i]);
      }
      $minDiff = $diff if $diff < $minDiff;
   }

   return $minDiff;
}

# Used to express the test cases below in a more succinct way
sub vectorToSquare {
   my($size, @vector) = @_;

   my @square;
   foreach my $i (0..$#vector) {
      $square[$i / $size][$i % $size] = $vector[$i];
   }

   return \@square;
}

# Test cases
is(formingMagicSquare(vectorToSquare(3, qw(4 9 2 3 5 7 8 1 5))), 1, "First  test");
is(formingMagicSquare(vectorToSquare(3, qw(4 8 2 4 5 7 6 1 6))), 4, "Second test");

