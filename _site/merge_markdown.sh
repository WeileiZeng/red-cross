echo "this script merge all parts of readme into one file"
cat head.md > README.md
cat data.md >> README.md
cat tail.md >> README.md
less README.md
