/**
In this tutorial, we will learn about Swift equatable with the help of examples.

In Swift, an Equatable is a protocol that allows two objects to be compared using the == operator. The hashValue is used to compare two instances.

To use the hashValue, we first have to conform (associate) the type (struct, class, etc) to Hashable property. For example,
**/
struct Employee: Hashable {
  ...
}  

/**
Here, we have conformed the Employee struct to the Hashable protocol.

Now when we create instances of Employee, the protocol will provide hash values to the instances.
**/

// Example: Swift Equatable Protocol

struct Employee: Hashable {
  var name: String
}

let obj1 = Employee(name: "Sabby")
let obj2 = Employee(name: "Smith")

// compare obj1 and obj2
if obj1 == obj2 {
    print("obj1 and obj2 are equal")
}
else {
    print("obj1 and obj2 are not equal")
}


/**
Here, the code obj1 == obj2 evaluates to false because obj1 and obj2 have different values for the name property. Hence, the else block is executed.

Note: A hash value is a long integer that varies based on the system you are using, so you might get different values for the same code.
**/


Compare Instances using Hashable Protocol
// conform Employee to Equatable
struct Employee: Equatable {
    
    var name: String
    var salary: Int
}

// initialize two objects with different property values 
let obj1 = Employee(name: "Sabby", salary: 40000)
let obj2 = Employee(name: "Sabby", salary: 40000)
let obj3 = Employee(name: "Cathy", salary: 30000)

// compare obj1 and obj2
if obj1 == obj2 {
    print("obj1 and obj2 are equal")
}
else {
    print("obj1 and obj2 are not equal")
}

// compare obj1 and obj3
if obj1 == obj3 {
    print("obj1 and obj3 are equal")
}
else {
    print("obj1 and obj3 are not equal")
}

// MARK: Output

// obj1 and obj2 are equal
// obj1 and obj3 are not equal
