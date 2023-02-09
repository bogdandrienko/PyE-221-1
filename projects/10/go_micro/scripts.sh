# update repositories
sudo apt-get update -y
sudo apt update -y
sudo apt-get upgrade -y
sudo apt upgrade -y

# install LANGUAGE
sudo apt install -y golang-go
# install IDE
sudo snap install goland --classic
#
mkdir go-rest-api && cd go-rest-api
# create custom package (module)
go mod init go-rest-api
# check all packages and install it
go get
# download
go get -u github.com/lib/pq
go get -u github.com/xuri/excelize/v2
go get -u github.com/gin-gonic/gin
# run
go run main.go
# compile
go build main.go