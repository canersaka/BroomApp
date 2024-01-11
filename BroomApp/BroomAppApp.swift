//
//  BroomAppApp.swift
//  BroomApp
//
//  Created by Caner Saka on 1/11/24.
//

import SwiftUI
import SwiftData

@main
struct BroomAppApp: App {
    var sharedModelContainer: ModelContainer = {
        let schema = Schema([
            Item.self,
        ])
        let modelConfiguration = ModelConfiguration(schema: schema, isStoredInMemoryOnly: false)

        do {
            return try ModelContainer(for: schema, configurations: [modelConfiguration])
        } catch {
            fatalError("Could not create ModelContainer: \(error)")
        }
    }()

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(sharedModelContainer)
    }
}



struct ActivityView: View {

    var body: some View {
        VStack {
            Text("This is the Activity View")
        }
    }
}
struct MessageView: View {
    var body: some View {
        VStack {
            Text("This is the message View")
        }
    }
}
struct AccountView: View {
        let items = ["Manage Account", "Bookmarked Cleaners", "Become a paid Cleaner", "Refer friends to get deals", "Legal"]

        var body: some View {
        VStack {
                Spacer()
                Text("This is the account View")
                Spacer()

                NavigationView {
                    List(items, id: \.self) { item in
                        NavigationLink(destination: ActivityView()) {
                            Text(item)
                        }
                    }
                    
                    .navigationTitle("Account")
                    Text("This app was designed by Caner Saka")
                        .font(.system(size: 9))
                        .padding()
                }
            }
    }
}
