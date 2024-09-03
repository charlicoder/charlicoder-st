environment=dev
date=$(date '+%Y-%m-%d-%H-%M')

### Pull branch
echo "Please enter branch name to pull:"
read branch
echo you have entered branch : $branch
sleep 1
git stash; git branch -f origin/$branch; git checkout $branch; git pull;

echo "creating docker image"
docker build -t charlicoder-st -f Dockerfile .

### Complete Deployment
echo "killing the running docker"
docker ps -a | egrep 'charlicoder-st' | awk '{print $1}'| xargs docker kill
docker ps -a | egrep 'charlicoder-st' | awk '{print $1}'| xargs docker rm

echo "running the charlicoder using docker"
docker run -d --restart=unless-stopped --name charlicoder-st -p 8501:8501 charlicoder-st

echo "We are done !"