//
//  ContentView.swift
//  BroomApp
//
//  Created by Caner Saka on 1/11/24.
//

import SwiftUI
import SwiftData
struct ContentView: View {
    var body: some View {
        TabView {
            // Your main view content
            Text("Broom Version 0.0.1")
                .tabItem {
                    Label("Home", systemImage: "house")
                }
            
            // ActivityView as another tab
            ActivityView()
         
                .tabItem {
                    Label("Activity", systemImage: "list.bullet.rectangle.portrait")
                }
            // MessageView as another tab
            MessageView()
                .tabItem {
                    Label("Message", systemImage: "message")
                }
            // AccountView as another tab
            AccountView()
                .tabItem {
                    Label("Account", systemImage: "person.crop.circle")
                    
                }

        }
    }
    struct ContentView_Previews: PreviewProvider {
        static var previews: some View {
            ContentView()
                .modelContainer(for: Item.self, inMemory: true)
        }
    }
}
