//
//  ViewController.swift
//  Hello World
//
//  Created by Lezardvaleth on 2019/1/21.
//  Copyright © 2019 Lezardvaleth. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var lable: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }
    @IBAction func sayhello(_ sender: Any) {
        let title = ["Hello World","Play Games","Kerbal","Fly Me to the Moon"]
        self.lable.text = title.randomElement()
    }
    

}

