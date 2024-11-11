echo "1. Deleting dist"
rm -rf dist
echo "2. Deleting egg file"
rm -rf tinq.egg-info
echo "3. Bump version"
python -m build
echo "4. Upload"
python -m twine upload dist/*
