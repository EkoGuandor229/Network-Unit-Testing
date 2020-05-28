# Network-Unit-Testing - NUTS2.0

## Description

Student project to automatically test settings in a network similar to unit-tests in software development.
NUTS leverages the nornir automation framework to create and execute tests defined in a testdescription.yaml
against a arbitrary network installation.

## Table of Contents

Installation

| - Requirements

| - Installation

| - Configuration

Usage

| - Inventory

| - Devices

| - DeviceConnection

| - TestDefinitions

| - Commands

| - Execute NUTS

Add New Tests

Credits

Licence

## Installation

### Requirements
NUTS needs a Python installation on the system executing the tests.
Python 3.6 or newer is required.
If You dont have Pyhon installed, visit the [Python Website](https://www.python.org/) and install Python according
to their documentation.

### Installation
To install NUTS, simply clone or download this repository.
The modules used in the project can be installed using the
```
pip install -r requirements.txt
```

### Configuration
You can change the location of the inventory, the testdefinitions and the testreport in the config.txt located
in the root folder of the project.
It is also possible to specify, that the GUI is skipped during execution

## Usage
### Inventory
Before you can use the Program, you have to create an inventory with the network devices and the connections between them.
Per default, you can find the inventory in the YourDirectory/NUTS2.0/nuts/resources/inventory/ folder.
### Devices
The devices.yaml specifies each device in your network.
```
router01: #device name
  - router01 #device_id used to identify each device
  - cisco_ios #operating system running on your device
  - user #username used to log in to the device
  - password #password used to log in to the device
  - 192.168.0.1 #IP-address of the device
  - 172.16.0.1 #Loopback-address of the device
```
### Connecctions
The deviceconnections.yaml specifies the connection between two devices.
Per default it is found in the YourDirectory/NUTS2.0/nuts/resources/DeviceConnections
```
connection01: #connection name
  - router01 #name of the first device
  - router42 #name of the second device
  - 100Mbit #bandwith of the connection
```
### Testdefinitions
The testdefinitions.yaml can be found in the YourDirectory/NUTS2.0/nuts/resources/TestDefinitions folder.
You can create multiple YAML files for testdefinitions to sort tests according to your own specifications
```
test01: #id of the test
  - TestRouter01 #name of the test
  - Ping #command. This refers to the type of tests that exist in the context of the program
  - router01 #device on which the test is executed
  - 192.168.0.42 #target of the test. This is optional and depends on the test executed
  - Success #the expected result of a test. A ping test as implemented can either succeed or fail
  - connectivity #test_group. You can specify any test group. In the GUI, the groups are sortet by this group name
```

### Commands
These commands are implemented in the actual version of the program.

Ping

Show Interfaces

Traceroute

Arp Table

OSPF Neighbors

### Execute NUTS
To run the program, in the command line navigate to the YourDirectory/NUTS2.0 folder.
You can start the program using 
```
python -m nuts
```
If you want to skip the UI and execute all tests in the order they are specified, use
```
python -m nuts -r
```
NUTS should now run and execute the tests specified in the testdefinitions.yaml
The testresults are shown in the command line and safed in the testresults.txt
located in the YourDirectory/NUTS2.0/nuts/resources/inventory/TestResults

Passed tests are annotated with their name and a "PASSED" notification.
Failed tests are printed with the name, expected value and actual value.


## Add New Tests
To add a new test, you can add it to the nuts/testcreation/concretetest folder
The test schould inherit from the NetworkTestStrategyInterface.
In the NetworkTestStrategyFactory class, add your test to the test_map dictionary

## Credits

Authors: Janik Schlatter, Mike Schmid

## Licence

Licenced under the Apache Licence 2.0
