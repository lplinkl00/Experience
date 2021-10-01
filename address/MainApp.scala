package ch.makery.address
import scalafx.application.JFXApp
import scalafx.application.JFXApp.PrimaryStage
import scalafx.scene.Scene
import scalafx.Includes._ //implicit function
import scalafxml.core.{NoDependencyResolver, FXMLView, FXMLLoader}
import javafx.{scene => jfxs} //alieas
import scalafx.collections.ObservableBuffer
import ch.makery.address.model.Person
import ch.makery.address.view.PersonEditDialogController
import scalafx.stage.{Stage, Modality}
import scalafx.scene.image.Image
import ch.makery.address.util.Database
object MainApp extends JFXApp {

  Database.setupDB()
 
  //initialize the person collection from DB
  Person.personData ++= Person.allPersons 

  // transform path of RootLayout.fxml to URI for resource location.
  val rootResource = getClass.getResourceAsStream("view/RootLayout.fxml")
  // initialize the loader object.
  val loader = new FXMLLoader(null, NoDependencyResolver)
  // Load root layout from fxml file.
  loader.load(rootResource);
  // retrieve the root component BorderPane from the FXML 
  val roots = loader.getRoot[jfxs.layout.BorderPane]
  // initialize stage
  stage = new PrimaryStage {
    title = "AddressApp"
    scene = new Scene {
      root = roots
      stylesheets += getClass.getResource("view/DarkTheme.css").toString()
    }
    icons += new Image(getClass.getResourceAsStream("/images/book.png"))
  }
  // actions for display person overview window 
  def showPersonOverview() = {
    val resource = getClass.getResourceAsStream("view/PersonOverview.fxml")
    val loader = new FXMLLoader(null, NoDependencyResolver)
    loader.load(resource);
    val roots = loader.getRoot[jfxs.layout.AnchorPane]
    MainApp.roots.setCenter(roots)
  } 
  def showWelcome() = {
    val resource = getClass.getResourceAsStream("view/Welcome.fxml")
    val loader = new FXMLLoader(null, NoDependencyResolver)
    loader.load(resource);
    val roots = loader.getRoot[jfxs.layout.AnchorPane]
    MainApp.roots.setCenter(roots)      
  }
  def showPersonEditDialog(person: Person): Boolean = {
    val resource = getClass.getResourceAsStream("view/PersonEditDialog.fxml")
    val loader = new FXMLLoader(null, NoDependencyResolver)
    loader.load(resource);
    val roots2  = loader.getRoot[jfxs.Parent]
    val control = loader.getController[PersonEditDialogController#Controller]

    val dialog = new Stage() {
      initModality(Modality.ApplicationModal)
      initOwner(stage)
      scene = new Scene {
        root = roots2
        stylesheets += getClass.getResource("view/DarkTheme.css").toString()
      }
    }
    control.dialogStage = dialog
    control.person = person
    dialog.showAndWait() //bloking
    control.okClicked
  } 

  // call to display PersonOverview when app start
  showWelcome()

  //imiplicit class
  //implicit def

  implicit val data: Int = 10 //declartion

  def playPlay(a: Int)(implicit b: Int): Unit = {
    println(a + b)
  }
  def playPlay1(a: Int)(implicit b: Int): Unit = {
    println(a - b)
  }
  def playPlay2(a: Int)(implicit b: Int): Unit = {
    println(a * b)
  } 
   def playPlay3(a: Int)(implicit b: Int): Unit = {
    println(a / b)
  }  
  playPlay(30)(10)
  playPlay(50)
  playPlay1(30)


  case class RM(value: Double)

  val money = RM(3.0)

  money match {
    case RM(y) =>
      println("the value of money is " + y)
  }

  val lists: List[Int] = List(1,2,3,4,5)
  val results: List[String] = lists.map((x) => s"=${x + 1}=")
  for (i <- results){
    println(i)
  }
}
