//
//  Item.swift
//  BroomApp
//
//  Created by Caner Saka on 1/11/24.
//

import Foundation
import SwiftData

@Model
final class Item {
    var timestamp: Date
    
    init(timestamp: Date) {
        self.timestamp = timestamp
    }
}
