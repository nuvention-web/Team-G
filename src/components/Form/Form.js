import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import logo from '../../../img/logo1.png';
import './Form.css';
import SMForm from './SMForm.js';

export default class Form extends React.Component {

  render() {
    return(
      <div>
        <section className="formSection">
          <div className="smallFormSection">
            <h3>Account Settings</h3>
            <form id="accForm" method="post">
              <table>
                <tr>
                  <td><label >Name</label></td>
                  <td><input type="text" name="Name"/></td>
                </tr>
                <tr>
                  <td><label >Email</label></td>
                  <td><input type="text" name="Email"/></td>
                </tr>
                <tr>
                  <td><label >Phone</label></td>
                  <td><input type="text" name="Phone"/></td>
                </tr>
                <tr>
                  <td><label >Company</label></td>
                  <td><input type="text" name="Company"/></td>
                </tr>
                <tr>
                  <td></td>
                  <td><input type="submit" value="Apply Changes"/></td>
                </tr>
              </table>
            </form>
          </div>
          <SMForm type="I"/>
          <SMForm type="T"/>
          <SMForm type="F"/>
        </section>
      </div>
    )
  }
}
