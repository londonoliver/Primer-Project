#!/usr/bin/perl -wT
if (length($ENV{'QUERY_STRING'}) > 0){
	$buffer = $ENV{'QUERY_STRING'};
	@pairs = split(/&/, $buffer);
	foreach $pair (@pairs){
		($name, $value) = split(/=/, $pair);
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		$in{$name} = $value;
	}
}
$adjective = $in{'adjective'};
$animal = $in{'animal'};
$verb = $in{'verb'};
$country = $in{'country'};
print "Content-type: text/html\n\n";
print "<HTML>", "\n";
print "<HEAD><link rel='stylesheet' type='text/css' href='../styles.css'></HEAD>", "\n";
print "<BODY><H1>First...</H1>", "\n";
print "<H2>Some information about this server</H2>\n";
print "<PRE>";
print "Server Name:      ", $ENV{'SERVER_NAME'}, "<BR>", "\n";
print "Running on Port:  ", $ENV{'SERVER_PORT'}, "<BR>", "\n";
print "Server Software:  ", $ENV{'SERVER_SOFTWARE'}, "<BR>", "\n";
print "Server Protocol:  ", $ENV{'SERVER_PROTOCOL'}, "<BR>", "\n";
print "CGI Revision:     ", $ENV{'GATEWAY_INTERFACE'}, "<BR>", "\n";
print "<H1>...Then</H1>";
print "<H2>The word game results!\n</H2>";
print "<H3>The <span id='word'>", $adjective, " ", $animal, " ", $verb, "</span> in <span id='word'>", $country, "</span>.</H3>";
print "</PRE>", "\n\n";
print "<img src='https://upload.wikimedia.org/wikipedia/commons/2/22/Earth_Western_Hemisphere_transparent_background.png' alt='Oops image could not be displayed'>";
print "</BODY></HTML>", "\n";
