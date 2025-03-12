# IntroSec -- Fuzzing

This is the code for the lecture on Fuzzing for the Introduction To Cybersecurity course at the [EURECOM](https://www.eurecom.fr/) research center. 

The slides are [here](https://docs.google.com/presentation/d/1WJDzp586N5Zchg7U6_s4VH6BnBZ6mtugzDrbSGJ1hjw/).

### Repository organization

+ [fuzzme_exe](https://github.com/packmad/IntrosecFuzzing/tree/master/fuzzme_exe): is an empty folder into which the binary executables to be tested should be put. 
+ [myfuzzer](https://github.com/packmad/IntrosecFuzzing/tree/master/myfuzzer): the fuzzer's code.
+ [slides_examples](https://github.com/packmad/IntrosecFuzzing/tree/master/slides_examples): the code snippets used in some slides.
+ [sut_examples](https://github.com/packmad/IntrosecFuzzing/tree/master/sut_examples): software under test examples, in which different ways of fuzzing are shown.

### Setting up

1. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repo or download the zip.
2. Install [docker](https://www.docker.com/). If you are under Windows, I strongly recommend that you first install [Ubuntu Linux](https://ubuntu.com/wsl) and then proceed with the installation of docker inside Ubuntu.
3. Open a [shell](https://en.wikipedia.org/wiki/Shell_(computing)), and then run the following commands:

```shell
cd IntrosecFuzzing/
docker build -t introsecfuzz .
docker run -it -v $(pwd)/:/IntrosecFuzzing/ introsecfuzz
``` 

A new `root` shell will pop up, from which you can run the code (see below).


### Running an example
```shell
python3 sut_examples/cgi_coverage.py 
```


### Solving the challenge

1. Download the `fuzzme.exe` executable from [our CTF website](https://introsec.s3.eurecom.fr/challenges#FuzzMe-3)
2. Copy `fuzzme.exe` into the `fuzzme_exe` folder
3. Implement your fuzzer, and plug it into `sut_examples/fuzzme_exe.py`
4. Create your Docker container
5. Run it: `python3 sut_examples/fuzzme_exe.py`
6. If it takes more than an hour, you should consider improving your fuzzer.
