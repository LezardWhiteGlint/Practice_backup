struct Factory {
    var time_circle = 0.0
    var production_amount = 0
    var production_price = 0
    var resource_1_name = "resource"
    var resource_1_amount = 0
    var resource_1_price = 0
    var resource_2_name: String?
    var resource_2_amount: Int?
    var resource_2_price: Int?
    var resource_3_name: String?
    var resource_3_amount: Int?
    var resource_3_price: Int?
}

let wheat = Factory(time_circle: 60, production_amount: 20, production_price: 36, resource_1_name: "Energy Cell", resource_1_amount: 20, resource_1_price: 16, resource_2_name: nil, resource_2_amount: nil, resource_2_price: nil, resource_3_name: nil, resource_3_amount: nil, resource_3_price: nil)

let a = 1
var b:Int?
b = 2
var dictest = [String:Int]()
dictest["IamDick"] = 1
dictest["haha"] == nil
dictest["IamDick"] = (dictest["IamDick"] ?? 0) + 1
