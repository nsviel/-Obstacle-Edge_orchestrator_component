# [Obstacle] Edge Orchestrator Component

Installed on the Edge server, it receives the data sent by the Data acquisition module. It is also reponsible of info and data transmission amongst the other components and the Control interface module.

![edge](https://user-images.githubusercontent.com/80487132/220367354-7539ae2f-3be6-4d10-97af-6defc2d1c21e.png)

## Installation and execution

<details><summary>Installation</summary>

Simply run the script file 
```
./install.sh
```
in the program directory.

</details>
<details><summary>Execution</summary>

Simply run by the command
```
./run.sh
```

</details>
<details><summary>Docker</summary>

You can use a docker image with:

```
cd docker
./build.sh
./run.sh
```

</details>

## Documentation

<details><summary>General</summary>

- The more important parameters could be changed in the ```config``` JSON file.

</details>

## System

Full system repository ( [link](https://github.com/nsviel/Obstacle_System) )
- [ ] Data acquisition module ( [link](https://github.com/nsviel/Obstacle-Data_Acquisition_Module) )
- [x] Edge server module
  - [x] Edge orchestrator component
  - [ ] Data processing component ( [link](https://github.com/nsviel/Velodium) )
- [ ] Control Interface module ( [link](https://github.com/nsviel/Obstacle-Control_Interface_Module) )
