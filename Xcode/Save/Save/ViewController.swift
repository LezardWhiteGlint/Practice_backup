//
//  ViewController.swift
//  Save
//
//  Created by Lezardvaleth on 2019/2/17.
//  Copyright © 2019 Lezardvaleth. All rights reserved.
//

import UIKit
import CoreData

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        let appDelegate = UIApplication.shared.delegate as! AppDelegate
        let context = appDelegate.persistentContainer.viewContext
        let entity = NSEntityDescription.entity(forEntityName: "User", in: context)
        let newUser = NSManagedObject(entity: entity!, insertInto: context)
        newUser.setValue("Shashikant", forKey: "username")
        newUser.setValue("1234", forKey: "password")
        newUser.setValue("1", forKey: "age")
        
    }


}

