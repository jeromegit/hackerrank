#!/usr/bin/perl
use strict;
use warnings;
use Test::More "no_plan";

# Complete the designerPdfViewer function below.
sub designerPdfViewer {
   my($h, $word) = @_;

   my $max = 0;
   my $aOrd = ord('a');
   foreach my $letter(split '', $word) {
      my $height = $h->[ord($letter) - $aOrd];
      $max = $height if $height > $max;
   }

   return $max * (length $word);
}

# Test cases
is(designerPdfViewer([qw(1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5)], "abc"),  9,  "test 1");
is(designerPdfViewer([qw(1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7)], "zaba"), 28, "test 2");
