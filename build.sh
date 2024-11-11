echo "1. Deleting dist"
rm -rf dist
echo "2. Deleting egg file"
rm -rf socketbee.egg-info
echo "3. Bump version"
sh bump.sh
echo "4. Build"
python3 -m build
echo "5. Upload"
python3 -m twine upload dist/*
