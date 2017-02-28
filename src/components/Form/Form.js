import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import logo from '../../../img/logo1.png';
import './Form.css';

export default class Form extends React.Component {

  render() {
    return(
      <div className="formPage">
        <section className="formSection">
          <table>
            <tr>
              <td><img className="logo-image" width="100vh" height="103vh" alt="logo" src={logo} /></td>
              <td><h1>follower#Stack</h1></td>
            </tr>
          </table>

          <h2>Hi, ___.</h2>
          <div className="smallFormSection">
            <h3>Account Settings</h3>
            <form id="accForm" method="post">
              <table>
                <tr>
                  <td><label for="Name">Name</label></td>
                  <td><input type="text" name="Name"/></td>
                </tr>
                <tr>
                  <td><label for="Email">Email</label></td>
                  <td><input type="text" name="Email"/></td>
                </tr>
                <tr>
                  <td><label for="Phone">Phone</label></td>
                  <td><input type="text" name="Phone"/></td>
                </tr>
                <tr>
                  <td><label for="Company">Company</label></td>
                  <td><input type="text" name="Company"/></td>
                </tr>
                <tr>
                  <td></td>
                  <td><input type="submit" value="Apply Changes"/></td>
                </tr>
              </table>
            </form>
          </div>
          <div className="smallFormSection">
            <h3>Instagram Account</h3>
            <form id="instaForm" method="post">
              <table>
                <tr>
                  <td><label for="IUsername">Username</label></td>
                  <td><input type="text" name="IUsername"/></td>
                </tr>
                <tr>
                  <td><label for="IPassword">Password</label></td>
                  <td><input type="password" name="IPassword"/></td>
                </tr>
                <tr>
                  <td></td>
                  <td><input type="submit" value="Apply Changes"/></td>
                </tr>
              </table>
            </form>
          </div>
          <div className="smallFormSection">
            <h3>Twitter Account</h3>
            <form id="twitterForm" method="post">
              <table>
                <tr>
                  <td><label for="TUsername">Username</label></td>
                  <td><input type="text" name="TUsername"/></td>
                </tr>
                <tr>
                  <td><label for="TPassword">Password</label></td>
                  <td><input type="password" name="TPassword"/></td>
                </tr>
                <tr>
                  <td></td>
                  <td><input type="submit" value="Apply Changes"/></td>
                </tr>
              </table>
            </form>
          </div>
          <div className="smallFormSection">
            <h3>Facebook Account</h3>
            <form id="facebookForm" method="post">
              <table>
                <tr>
                  <td><label for="FUsername">Username</label></td>
                  <td><input type="text" name="FUsername"/></td>
                </tr>
                <tr>
                  <td><label for="FPassword">Password</label></td>
                  <td><input type="password" name="FPassword"/></td>
                </tr>
                <tr>
                  <td></td>
                  <td><input type="submit" value="Apply Changes"/></td>
                </tr>
              </table>
            </form>
          </div>
        </section>
      </div>
    )
  }
}
