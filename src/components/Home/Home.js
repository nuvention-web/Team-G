import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import logo from '../../../img/logo1.png';
import './Home.css';
import * as firebase from 'firebase';
import Landing from '../Landing';
import Button from 'react-bootstrap/lib/Button';

export default class Home extends React.Component {
constructor(){
    super();
    //this.validate = this.validate.bind(this);
    //this.register = this.register.bind(this);
    this.state = {
      logOut: false
    }
  }

  handle_logout(){
    firebase.auth().signOut();
          this.setState({
        logOut: true
    });
  }

  render() {
    if(!this.state.logOut)
    return(
      <div className="formPage">
        <section className="formSection">
          <table className="tableClass">
            <tbody className="tbodyClass">
              <tr> 
                <td><img className="logo-image" width="100vh" height="103vh" alt="logo" src={logo} /></td>
                <td><h1>follower#Stack</h1></td>
                <td style={{"textAlign":"right"}}><a onClick={this.handle_logout.bind(this)} className="btn-landing-top anchor-tag" href="#">Sign Out</a></td>
              </tr>
            </tbody>
          </table>
          <h2>Hello!</h2>  
        </section>
      </div>
    )
    else
      return(
        <Landing />
        )
  }
}
