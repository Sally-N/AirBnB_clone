<p align="center">
  <img src="https://github.com/Sally-N/AirBnB_clone/blob/18a77c3b355a351703324d55759947288cf5c51e/assets/hbnb_logo.png" alt="hbnb logo">
</p>

<h1 align="center">AirBnB Clone Project</h1>

---

## Description

The AirbBnB clone project is a top down implementation of the AirBnB housing rental project that allows home owners to rent out their houses to people looking for accomodation in the short or long-term. The repository contains implementation of a command line interface (CLI) that provides a low-level interface to interact with the various data models used in AirBnB.

## Usage
### How to start the CLI
1. Clone the repository
```
$ git clone https://github.com/Sally-N/AirBnB_clone.git
```
2. Run the console file
```
$ ./console.py
```
### Interacting with CLI
After starting the console, you will be greeted with an info screen that shows all commands as below
```
$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
$
```
* **create**
  * Usage: `create <class>`

Creates an instance of the specified class.

```
$ ./console.py
(hbnb) create BaseModel
57964624-24e7-45de-8f11-f7aa45edf03d
(hbnb) quit
$ cat file.json ; echo ""
{"BaseModel.57964624-24e7-45de-8f11-f7aa45edf03d": {"id": "57964624-24e7-45de-8f11-f7aa45edf03d", 
  "created_at": "2023-03-12T03:59:26.842458", "updated_at": "2023-03-12T03:59:26.842462", 
  "__class__": "BaseModel"}}
```
* **show**
  * Usage: `show <class> <class.id>`

Shows a class instance based on class name and instance id
```
$ ./console.py
(hbnb) show BaseModel 57964624-24e7-45de-8f11-f7aa45edf03d
[BaseModel] (57964624-24e7-45de-8f11-f7aa45edf03d) {'id': '57964624-24e7-45de-8f11-f7aa45edf03d', 
  'created_at': datetime.datetime(2023, 3, 12, 3, 59, 26, 842458), 
  'updated_at': datetime.datetime(2023, 3, 12, 3, 59, 26, 842462)}
(hbnb) quit
```
* **all**
  * Usage: `all` or `all <class>`
  
Shows all instances saved in file based or not base on class name.
```
$ ./console.py
(hbnb) all
["[BaseModel] (360f1574-68e3-456c-a43e-46e4a3557a93) {'id': '360f1574-68e3-456c-a43e-46e4a3557a93', 
  'created_at': datetime.datetime(2023, 3, 12, 4, 13, 4, 845771), 
  'updated_at': datetime.datetime(2023, 3, 12, 4, 13, 4, 845777), 'email': 'alxafrica@airbnb.com'}", 
 "[User] (1f22a9a0-8c40-4b06-a2e5-ffda57e8220b) {'id': '1f22a9a0-8c40-4b06-a2e5-ffda57e8220b', 
  'created_at': datetime.datetime(2023, 3, 12, 4, 17, 26, 540595), 
  'updated_at': datetime.datetime(2023, 3, 12, 4, 17, 26, 540600)}"]
(hbnb) all User
["[User] (1f22a9a0-8c40-4b06-a2e5-ffda57e8220b) {'id': '1f22a9a0-8c40-4b06-a2e5-ffda57e8220b', 
  'created_at': datetime.datetime(2023, 3, 12, 4, 17, 26, 540595), 
  'updated_at': datetime.datetime(2023, 3, 12, 4, 17, 26, 540600)}"]
(hbnb) quit
```

* **destroy**
  * Usage: `destroy <class> <class.id>`
  
Deletes a class instance based on the class name and instance id.
```
$ ./console.py
(hbnb) destroy BaseModel 57964624-24e7-45de-8f11-f7aa45edf03d
(hbnb) show BaseModel 57964624-24e7-45de-8f11-f7aa45edf03d
** no instance found **
(hbnb) quit
$ cat file.json ; echo ""
{}
```
* **update**
  * Usage: `update <class> <class.id> <attribute_name> <attribute_value>`
  
Updates a class instance with an attribute and value
```
$ ./console.py
(hbnb) create BaseModel
360f1574-68e3-456c-a43e-46e4a3557a93
(hbnb) update BaseModel 360f1574-68e3-456c-a43e-46e4a3557a93 email alxafrica@airbnb.com
(hbnb) show BaseModel 360f1574-68e3-456c-a43e-46e4a3557a93
[BaseModel] (360f1574-68e3-456c-a43e-46e4a3557a93) {'id': '360f1574-68e3-456c-a43e-46e4a3557a93', 
  'created_at': datetime.datetime(2023, 3, 12, 4, 13, 4, 845771), 'updated_at': datetime.datetime(2023, 3, 12, 4, 13, 4, 845777), 
  'email': 'alxafrica@airbnb.com'}
(hbnb) quit
```
