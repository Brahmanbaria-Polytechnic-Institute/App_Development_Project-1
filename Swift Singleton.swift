/**
In this tutorial, we will learn about Swift Singleton with the help of examples.

In Swift, Singleton is a design pattern that ensures a class can have only one object. Such a class is called singleton class.

To create a singleton class, we need to follow some rule
1. Create a private initializer

An initializer allows us to instantiate an object of a class. And, making the initializer of a class restricts the object creation of the class from outside of the class.
**/


class FileManager {
 
  ... 
  // create a private initializer
  private init() {
  }
}

// Error Code
let obj = FileManager()


/**
Here, the initializer of the FileManager class is private. So, when we try to create an object of FileManager outside of the class, we get an error.

2. Create static type Singleton Object

In Singleton class, we create a single static type object of the class. Making the object static allows us to access the object using the class name.
**/
class FileManager {
  
  // static property to create singleton
  static let fileObj = FileManager()
  ... 
}

// access the singleton 
let data = FileManger.fileObj
