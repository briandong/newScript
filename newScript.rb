#!/usr/bin/env ruby

path = ARGV[0]
fail "specify filename to create" unless path

path_list = path.split('/')
dir = path_list[0..-2].join('/')

# sample script
File.open(path, "w") do |f|
	f.puts "#!/usr/bin/env ruby -w"
	f.puts "\n# Definition of a sample user class"
	f.puts "class User"
	f.puts "\n    # Name of user"
	f.puts "    attr_accessor :name"
	f.puts "\n    # What does the user say"
	f.puts "    def speak"
	f.puts "        reture 'HelloWorld!'"
	f.puts "    end"
	f.puts "\nend #class User"
	f.puts "\n# Only run the following code when this file is the main file being run"
	f.puts "if __FILE__ == $0"
	f.puts "end #if"
end

File.chmod(0755, path)
system "open", path

# unit test script
test_dir = dir+"/test"
Dir.mkdir test_dir

test_path = test_dir+"/tc_"+path_list[-1]
File.open(test_path, "w") do |f|
	f.puts "#!/usr/bin/env ruby -w"
end

# Rakefile
