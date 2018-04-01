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
	f.puts "        return 'HelloWorld!'"
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
Dir.mkdir test_dir unless Dir.exist? test_dir

test_path = test_dir+"/tc_"+path_list[-1]
File.open(test_path, "w") do |f|
	f.puts "require 'test/unit'"
	f.puts "require_relative \'../#{path_list[-1]}\'"
	f.puts "\nclass UserTest < Test::Unit::TestCase"
	f.puts "    def test_speak"
	f.puts "        u = User.new"
	f.puts "        assert_equal 'HelloWorld!', u.speak"
	f.puts "    end #test_speak"
	f.puts "end #class"
end

# Rakefile
rake_path = dir+"/Rakefile"
File.open(rake_path, "w") do |f|
	f.puts "require 'rdoc/task'"
	f.puts "require 'rake/testtask'"
	f.puts "\nRake::RDocTask.new do |t|"
	f.puts "    t.rdoc_files.include '*.rb'"
	f.puts "    t.options << '--diagram'"
	f.puts "end"
	f.puts "\nRake::TestTask.new do |t|"
	f.puts "    t.test_files = FileList['test/tc_*.rb']"
	f.puts "end"
end

