struct Item {
    var name = ""
    var price = 0.0
    var amount = 0.0
    func getName() -> String {
        return self.name
    }
    func getPrice() -> Double {
        return self.price
    }
    func getAmount() -> Double {
        return self.amount
    }
}

struct Factory {
    var single_circle = 0.0 // in seconds
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
    func getPerHourAmount(item:Item?) -> Double? {
        let times = 3600/self.single_circle
        return (item?.getAmount() ?? 0)*times
    }
    func getTotalPrice(item:Item?) -> Double? {
        return (item?.getPrice() ?? 0)*(self.getPerHourAmount(item:item) ?? 0)
    }
    func getProfit() -> Double? {
        let prod = self.getTotalPrice(item: product) ?? 0
        let res1 = self.getTotalPrice(item: resource1) ?? 0
        let res2 = self.getTotalPrice(item: resource2) ?? 0
        let res3 = self.getTotalPrice(item: resource3) ?? 0
        let result = prod - res1 - res2 - res3
        return result
    }
    func getChangeAmount() -> [String:Double] {
        var result = [String:Double]()
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
    func getTotalAmount() -> [String:Double]{
        var result = [String:Double]()
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
    func getTotalProfit(item_price:[String:Double]) -> Double {
        var result = 0.0
        let output = self.getTotalAmount()
        for (item,amount) in output {
            result += (item_price[item] ?? 0) * amount
        }
        return result
    }
}
// set the parameters of factories and thier product + resources
let wheat_wheatFacM = Item(name: "wheat", price: 36, amount: 20)
let energy_wheatFacM = Item(name: "energy cell", price: 16, amount: 30)
// wheat fac M
let wheatFacM = Factory(single_circle: 60, product: wheat_wheatFacM, resource1: energy_wheatFacM, resource2: nil, resource3: nil)
let wheat_wheatFacL = Item(name: "wheat", price: 36, amount: 50)
let energy_wheatFacL = Item(name: "energy cell", price: 16, amount: 75)
// wheat fac L
let wheatFacL = Factory(single_circle: 60, product: wheat_wheatFacL, resource1: energy_wheatFacL, resource2: nil, resource3: nil)
//crystal fab M
let energy_crystalFabM = Item(name: "energy cell", price: 16, amount: 240)
let silicon_crystalFabM = Item(name: "silicon", price: 504, amount: 10)
let meatsteak_crystalFabM = Item(name: "meatsteak", price: 72, amount: 160)
let crystal_crystalFabM = Item(name: "crystal", price: 3368, amount: 16)
let crystalFabM = Factory(single_circle: 480, product: crystal_crystalFabM, resource1: energy_crystalFabM, resource2: silicon_crystalFabM, resource3: meatsteak_crystalFabM)
//crystal fab L
let energy_crystalFabL = Item(name: "energy cell", price: 16, amount: 600)
let silicon_crystalFabL = Item(name: "silicon", price: 504, amount: 25)
let meatsteak_crystalFabL = Item(name: "meatsteak", price: 72, amount: 400)
let crystal_crystalFabL = Item(name: "crystal", price: 3368, amount: 40)
let crystalFabL = Factory(single_circle: 480, product: crystal_crystalFabL, resource1: energy_crystalFabL, resource2: silicon_crystalFabL, resource3: meatsteak_crystalFabL)
// energyFacM
let energy_energyFacM = Item(name: "energy cell", price: 16, amount: 1106)
let crystal_energyFacM = Item(name: "crystal", price: 1684, amount: 8)
let energyFacM = Factory(single_circle: 3*60+35, product: energy_energyFacM, resource1: crystal_energyFacM , resource2: nil, resource3: nil)
////energyFacL
let energy_energyFacL = Item(name: "energy cell", price: 16, amount: 2765)
let crystal_energyFacL = Item(name: "crystal", price: 1684, amount: 20)
let energyFacL = Factory(single_circle: 3*60+35, product: energy_energyFacL, resource1: crystal_energyFacL, resource2: nil, resource3: nil)
////energyFacXL
let energy_energyFacXL = Item(name: "energy cell", price: 16, amount: 5530)
let crystal_energyFacXL = Item(name: "crystal", price: 1684, amount: 40)
let energyFacXL = Factory(single_circle: 3*60+35, product: energy_energyFacXL, resource1: crystal_energyFacXL, resource2: nil, resource3: nil)
let wheat_rimeFacL = Item(name: "wheat", price: 36, amount: 60)
let energy_rimeFacL = Item(name: "energy cell", price: 16, amount: 90)
let rime_rimeFacL = Item(name: "rime cloth", price: 292, amount: 15)
// rimeFacL
let rimeFacL = Factory(single_circle: 75, product: rime_rimeFacL, resource1:wheat_rimeFacL , resource2: energy_rimeFacL, resource3: nil)
// silicon mine L 110
let energy_SiliconMineL = Item(name: "energy cell", price: 16, amount: 240)
let silicon_SiliconMineL = Item(name: "silicon", price: 504, amount: 10)
let siliconMineL110 = Factory(single_circle: 110, product: silicon_SiliconMineL, resource1: energy_SiliconMineL, resource2: nil, resource3: nil)
// silicon mine L 78
let siliconMineL78 = Factory(single_circle: 78, product: silicon_SiliconMineL, resource1: energy_SiliconMineL, resource2: nil, resource3: nil)
// quantum tube fab
let energy_quantum = Item(name: "energy cell", price: 16, amount: 600)
let silicon_quantum = Item(name: "silicon", price: 504, amount: 25)
let meatsteak_quantum = Item(name: "meatsteak", price: 72, amount: 400)
let quantumTube_quantum = Item(name: "quantumtube", price: 3368, amount: 24)
let quantumTubeFab = Factory(single_circle: 2400, product: quantumTube_quantum, resource1: energy_quantum, resource2: silicon_quantum, resource3: meatsteak_quantum)
//quantumTubeFab.getProfit()
//  meatsteakFacL
let energy_cahoonaL = Item(name: "energy cell", price: 16, amount: 75)
let argonBeef_cahoonaL = Item(name: "beef", price: 104, amount: 15)
let meatsteak_cahonnaL = Item(name: "meatsteak", price: 72, amount: 50)
let meatsteakFacL = Factory(single_circle: 60, product: meatsteak_cahonnaL, resource1: energy_cahoonaL, resource2: argonBeef_cahoonaL, resource3: nil)
// cattleFacL
let energy_cattleL = Item(name: "energy cell", price: 16, amount: 75)
let argonBeef_cattleL = Item(name: "beef", price: 104, amount: 15)
let cattleFacL = Factory(single_circle: 60, product: argonBeef_cattleL, resource1: energy_cattleL, resource2: nil, resource3: nil)
// chipplant
let energy_chip = Item(name: "energy cell", price: 16, amount: 360)
let silicon_chip = Item(name: "silicon", price: 504, amount: 15)
let meatsteak_chip = Item(name: "meatsteak", price: 72, amount: 240)
let chip_chip = Item(name: "chip", price: 13476, amount: 4)
let chipFac = Factory(single_circle: 24*60, product: chip_chip, resource1: energy_chip, resource2: silicon_chip, resource3: meatsteak_chip)
// computer plant
let energy_computer = Item(name: "energy cell", price: 16, amount: 24)
let silicon_computer = Item(name: "silicon", price: 504, amount: 1)
let meatsteak_computer = Item(name: "meatsteak", price: 72, amount: 16)
let computer_computer = Item(name: "computer component", price: 1348, amount: 2)
let computerFac = Factory(single_circle: 96, product: computer_computer, resource1: energy_computer, resource2: silicon_computer, resource3: meatsteak_computer)


//let itemtest = fac1.getItem(item_name: "energy cell")
//itemtest?.getAmount()
//fac1.getPerHourAmount(item: energy)
//fac1.getProfit()
//let test = fac1.getChangeAmount()
let item_price : [String:Double] = ["wheat":36,"energy cell":16,"rime cloth":292,"silicon":504,"meatsteak":72,"chip":13476,"beef":104,"quantumtube":3368,"computer component":1348]

//first mega complex
//let current_section = [energyFacM,siliconMineL,siliconMineL,quantumTubeFab,crystalFabM]
//let energy_section = [crystalFabL,energyFacM]
//let food_section = [Factory]()
//let product_section = [quantumTubeFab,quantumTubeFab,quantumTubeFab,quantumTubeFab,quantumTubeFab,quantumTubeFab,quantumTubeFab,quantumTubeFab,quantumTubeFab,quantumTubeFab]
////print(product_section.count)
//let complex_list = current_section + energy_section + food_section + product_section
//print("when have \(complex_list.count) stations")
//let comp = Complex(factories: complex_list)
//let complex_result = comp.getTotalAmount()
//for (item,amount) in complex_result {
//    if item != "" {
//        print("The \(item) amount is \(amount)")
//    }
//}
//let total_profit = comp.getTotalProfit(item_price: item_price)
//print("The total profit is \(total_profit)")

//let mine_section = [siliconMineL78,siliconMineL78]
//let energy_section = [energyFacL,crystalFabL,crystalFabM]
//let food_section = [Factory]()
//let product_section = [Factory](repeating: chipFac, count: 17)
////print(product_section.count)
//let complex_list = mine_section + energy_section + food_section + product_section
//print("when have \(complex_list.count) stations")
//let comp = Complex(factories: complex_list)
//let complex_result = comp.getTotalAmount()
//for (item,amount) in complex_result {
//    if item != "" {
//        print("The \(item) amount is \(amount)")
//    }
//}
//let total_profit = comp.getTotalProfit(item_price: item_price)
//print("The total profit is \(total_profit)")


// silicon mine L 89
let siliconMineL89 = Factory(single_circle: 89, product: silicon_SiliconMineL, resource1: energy_SiliconMineL, resource2: nil, resource3: nil)

let mine_section = [Factory]()
let energy_section = [Factory]()
let food_section = [Factory](repeating: cattleFacL, count: 5)
let product_section = [Factory](repeating: meatsteakFacL, count: 5)
//print(product_section.count)
let complex_list = mine_section + energy_section + food_section + product_section
print("when have \(complex_list.count) stations")
let comp = Complex(factories: complex_list)
let complex_result = comp.getTotalAmount()
for (item,amount) in complex_result {
    if item != "" {
        print("The \(item) amount is \(amount)")
    }
}
let total_profit = comp.getTotalProfit(item_price: item_price)
print("The total profit is \(total_profit)")
