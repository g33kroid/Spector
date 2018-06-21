# Ubuntu 16.04 Version of Installation

echo "deb https://apache.bintray.com/couchdb-deb xenial main" \
    | sudo tee -a /etc/apt/sources.list

curl -L https://couchdb.apache.org/repo/bintray-pubkey.asc \
    | sudo apt-key add -

sudo apt-get --no-install-recommends -y install \
    build-essential pkg-config erlang \
    libicu-dev libmozjs185-dev libcurl4-openssl-dev
    
sudo apt-get update && sudo apt-get install couchdb

sudo pip install -r requirements.txt



