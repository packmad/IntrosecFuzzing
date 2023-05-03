# IntroSec -- Fuzzing


### Setting up

1. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repo or download the zip.
2. Install [docker](https://www.docker.com/). If you are under Windows, I strongly recommend that you first install [Ubuntu Linux](https://ubuntu.com/wsl) and then proceed with the installation of docker inside Ubuntu.
3. Open a [shell](https://en.wikipedia.org/wiki/Shell_(computing)), move into the IntrosecFuzzing folder, and then run the following commands

```shell
docker build -t introsecfuzz .
docker run -it -v $(pwd)/:/IntrosecFuzzing/ introsecfuzz
``` 

### Running an example
```shell
python3 sut_examples/cgi_coverage.py 
```


### Running the challenge

1. Download the executable from [here](https://www.dropbox.com/s/e3hfqbbc7a6uhgq/fuzzme.exe?dl=1). 
2. Copy `fuzzme.exe` in the `fuzzme_exe` folder.


If you are under Linux or macOS this command can do the job for you:
```shell
curl -L -o ./fuzzme_exe/fuzzme.exe https://www.dropbox.com/s/e3hfqbbc7a6uhgq/fuzzme.exe?dl=1
``` 

Remember, if you run `fuzzme.exe` with the correct arguments you get:
```shell
./fuzzme.exe ? ? ? ?
0
1
2
3
4
5
6
7
8
ISEC{flag}
```

In this way the output of the program can be used as a coverage feedback.