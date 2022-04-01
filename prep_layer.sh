mkdir -p python
cd python
pip3 install -t discord-webhook python-dotenv
cd ../
zip -r -q python.zip python
rm -rf python