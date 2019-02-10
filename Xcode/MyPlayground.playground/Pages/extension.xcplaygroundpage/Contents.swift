struct test {
    var origin = 1
}

extension test {
    func IAMEX() {
        print("This is extension")
    }
}

let IAmTesting = test()
IAmTesting.IAMEX()

