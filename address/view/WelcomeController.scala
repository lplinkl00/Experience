package ch.makery.address.view

import scalafxml.core.macros.sfxml
import ch.makery.address.MainApp
@sfxml
class WelcomeController() {
    def handleClick(): Unit = {
        MainApp.showPersonOverview()
    }
}