

docker build -t pza_test .


docker run \
    -v $PWD/../..:/work \
    -it pza_test bash

