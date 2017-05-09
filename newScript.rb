#!/usr/bin/env ruby

path = ARGV[0]
fail "specify filename to create" unless path

File.open(path, "w") do |f|
	f.puts "#!/usr/bin/env ruby -w"
	f.puts "\n# Only run the following code when this file is the main file being run"
	f.puts "if __FILE__ == $0"
	f.puts "end"
end

File.chmod(0755, path)
system "open", path
