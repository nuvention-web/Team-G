import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './Form.css';

export default class SMForm extends React.Component {

  handle_form_param(param){
    if (this.props.type == "I") {
      if (param == "type") return "Instagram";
      else if (param == "formid") return "instaForm";
      else if (param == "username") return "IUsername";
      else if (param == "password") return "IPassword";
    }
    else if (this.props.type == "T") {
      if (param == "type") return "Twitter";
      else if (param == "formid") return "twitterForm";
      else if (param == "username") return "TUsername";
      else if (param == "password") return "TPassword";
    }
    else if (this.props.type == "F") {
      if (param == "type") return "Facebook";
      else if (param == "formid") return "FacebookForm";
      else if (param == "username") return "FUsername";
      else if (param == "password") return "FPassword";
    }
  }

  render() {
    return(
      <div className="smallFormSection">
        <h3>{this.handle_form_param("type")} Account</h3>
        <form id={this.handle_form_param("formid")} method="post">
          <table>
            <tr>
              <td><label for={this.handle_form_param("username")}>Username</label></td>
              <td><input type="text" name={this.handle_form_param("username")}/></td>
            </tr>
            <tr>
              <td><label for={this.handle_form_param("password")}>Password</label></td>
              <td><input type="password" name={this.handle_form_param("password")}/></td>
            </tr>
            <tr>
              <td></td>
              <td><input type="submit" value="Apply Changes"/></td>
            </tr>
          </table>
        </form>
      </div>
    )
  }
}
