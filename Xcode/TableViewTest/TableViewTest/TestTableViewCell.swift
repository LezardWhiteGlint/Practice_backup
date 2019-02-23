//
//  TestTableViewCell.swift
//  TableViewTest
//
//  Created by Lezardvaleth on 2019/2/23.
//  Copyright © 2019 Lezardvaleth. All rights reserved.
//

import UIKit

class TestTableViewCell: UITableViewCell {
    
    @IBOutlet weak var test: UILabel!
    
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }

    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }

}
