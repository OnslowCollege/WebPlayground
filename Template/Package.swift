// swift-tools-version:4.2
import PackageDescription

let package = Package(name: "Template")

package.products = [
    .executable(name: "Template", targets: ["Template"])
]
package.dependencies = [
    .package(url: "https://github.com/rensbreur/SwiftTUI.git", Version(0,0,0)...Version(1_000_000,0,0))
]
package.targets = [
    .target(name: "Template", dependencies: [.product(name: "SwiftTUI", package: "SwiftTUI")], path: "Sources")
]
