struct Item {
    var name = ""
    var price = 0
    var amount = 0
    func getName() -> String {
        return self.name
    }
    func getPrice() -> Int {
        return self.price
    }
    func getAmount() -> Int {
        return self.amount
    }
}

struct Factory {
    var single_circle = 0 // in seconds
    var product:Item
    var resource1:Item?
    var resource2:Item?
    var resource3:Item?
    func getItem(item_name:String) -> Item? {
        switch item_name {
        case product.getName():
            return product
        case resource1?.getName():
            return resource1
        case resource2?.getName():
            return resource2
        case resource3?.getName():
            return resource3
        default:
            print("No name macthed")
            return nil
        }
    }
    func getPerHourAmount(item:Item?) -> Int? {
        let times = 3600/self.single_circle
        return (item?.getAmount() ?? 0)*times
    }
    func getTotalPrice(item:Item?) -> Int? {
        return (item?.getPrice() ?? 0)*(self.getPerHourAmount(item:item) ?? 0)
    }
    func getProfit() -> Int? {
        let result = (self.getTotalPrice(item: product) ?? 0) - (self.getTotalPrice(item: resource1) ?? 0) - (self.getTotalPrice(item: resource2) ?? 0) - (self.getTotalPrice(item: resource3) ?? 0)
        return result
    }
    func getChangeAmount() -> [String:Int] {
        var result = [String:Int]()
        let times = 3600/self.single_circle
        result[self.product.getName()] = (self.product.getAmount() ?? 0) * times
        result[(self.resource1?.getName() ?? "")] = -(self.resource1?.getAmount() ?? 0) * times
        result[(self.resource2?.getName() ?? "")] = -(self.resource2?.getAmount() ?? 0) * times
        result[(self.resource3?.getName() ?? "")] = -(self.resource3?.getAmount() ?? 0) * times
        return result
    }
}

struct Complex {
    var factories = [Factory]()
    func getFactories() -> [Factory] {
        return self.factories
    }
    func getTotalAmount() -> [String:Int]{
        var result = [String:Int]()
        for fac in self.getFactories() {
            for (item,amount) in fac.getChangeAmount() {
                if result[item] == nil {
                    result[item] = amount
                }else{
                    result[item] = (result[item] ?? 0) + amount
                }
            }
        }
        return result
    }
}
let wheat = Item(name: "wheat", price: 36, amount: 20)
let energy = Item(name: "energy cell", price: 16, amount: 30)
let fac1 = Factory(single_circle: 60, product: wheat, resource1: energy, resource2: nil, resource3: nil)
let fac2 = Factory(single_circle: 60, product: wheat, resource1: energy, resource2: nil, resource3: nil)
//let itemtest = fac1.getItem(item_name: "energy cell")
//itemtest?.getAmount()
//fac1.getPerHourAmount(item: energy)
//fac1.getProfit()
let test = fac1.getChangeAmount()
let complex_list = [fac1,fac2]
let comp = Complex(factories: complex_list)
comp.getTotalAmount()

