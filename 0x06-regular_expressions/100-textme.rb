#!/usr/bin/env ruby
puts ARGV[0].scan(/((?<=\bfrom:|to:|flags:)[+-:\w]*)/).join(',')
