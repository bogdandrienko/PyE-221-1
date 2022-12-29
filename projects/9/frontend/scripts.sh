
# install lts node js https://nodejs.org/en/
npx create-react-app frontend --template redux-typescript






# debian
sudo apt-get install -y curl
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
export NVM_DIR="$HOME/.nvm"
source ~/.bashrc
nvm ls-remote
nvm install 18.12.1
nvm use 18.12.1
node --version
npx create-react-app frontend --template redux-typescript



cd frontend
npm start

npm run build

npm i axios