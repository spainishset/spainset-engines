# Small script for comiling the latest master version of Spain Set.

# Features:
# 1 - Removes previous files
# 2 - Downloads an unzips latest commit
# 3 - Installs the dependencies for compiling
# 4 - Builds the set

# Usage: schedule it at the crontab for periodic execution

# Tested on Ubuntu 20.04 - Apr-2020

#################################################################

rm master.zip
rm -r spainset-engines-master
wget https://github.com/spainishset/spainset-engines/archive/refs/heads/master.zip
unzip master.zip
cd spainset-engines-master
cd tools
pip3 install .
cd ..
./build.sh |& tee build_log.txt
echo EXECUTION FINISHED