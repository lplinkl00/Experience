package ch.makery.address.view

import ch.makery.address.model.Person
import ch.makery.address.MainApp
import scalafx.scene.control.{TextField, TableColumn, Label, Alert}
import scalafxml.core.macros.sfxml
import scalafx.stage.Stage
import scalafx.Includes._
import ch.makery.address.util.DateUtil._
import scalafx.event.ActionEvent

@sfxml
class PersonEditDialogController (
    private val  firstNameField : TextField,
    private val   lastNameField : TextField,
    private val     streetField : TextField,
    private val postalCodeField : TextField,
    private val       cityField : TextField,
    private val   birthdayField : TextField
){
  var         dialogStage : Stage  = null //window reference
  private var _person     : Person = null //data model
  var         okClicked            = false //store user choice

  def person = _person
  def person_=(x : Person) {
        _person = x //update the private data field
        //update the person value to all textfield
        firstNameField.text = person.firstName.value
        lastNameField.text  = person.lastName.value
        streetField.text    = person.street.value
        postalCodeField.text= person.postalCode.value.toString
        cityField.text      = person.city.value
        birthdayField.text  = person.date.value.asString
        birthdayField.setPromptText("dd.mm.yyyy");
  }

  def handleOk(action :ActionEvent){

     if (isInputValid()) {
        _person.firstName.value = firstNameField.text()
        _person.lastName.value  = lastNameField.text()
        _person.street.value    = streetField.text()
        _person.city.value      = cityField.text()
        _person.postalCode.value = postalCodeField.getText().toInt
        _person.date.value       = birthdayField.text.value.parseLocalDate;

        okClicked = true;
        dialogStage.close()
    }
  }

  def handleCancel(action :ActionEvent) {
        dialogStage.close();
  }
  def nullChecking (x : String) = x == null || x.length == 0

  def isInputValid() : Boolean = {
    var errorMessage = ""

    if (nullChecking(firstNameField.text.value))
      errorMessage += "No valid first name!\n"
    if (nullChecking(lastNameField.text.value))
      errorMessage += "No valid last name!\n"
    if (nullChecking(streetField.text.value))
      errorMessage += "No valid street!\n"
    if (nullChecking(postalCodeField.text.value))
      errorMessage += "No valid postal code!\n"
    else {
      try {
        postalCodeField.text.value.toInt
        //Integer.parseInt(postalCodeField.getText());
      } catch {
          case e : NumberFormatException =>
            errorMessage += "No valid postal code (must be an integer)!\n"
      }
    }
    if (nullChecking(cityField.text.value))
      errorMessage += "No valid city!\n"
    if (nullChecking(birthdayField.text.value))
      errorMessage += "No valid birtday!\n"
    else {
      if (!birthdayField.text.value.isValid) {
          errorMessage += "No valid birthday. Use the format dd.mm.yyyy!\n";
      }
    }

    if (errorMessage.length() == 0) {
         true;
    } else {
        // Show the error message.
        val alert = new Alert(Alert.AlertType.Error){
          initOwner(dialogStage)
          title = "Invalid Fields"
          headerText = "Please correct invalid fields"
          contentText = errorMessage
        }.showAndWait()

         false;
    }
   }
} 
