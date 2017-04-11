import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import logo from '../../../img/logo1.png';
import './Home.css';
import * as firebase from 'firebase';
import Landing from '../Landing';
import Button from 'react-bootstrap/lib/Button';
import Form from '../Form';
import {Link} from "react-router-dom";

export default class Home extends React.Component {
constructor(){
    super();
    //this.validate = this.validate.bind(this);
    //this.register = this.register.bind(this);
    this.state = {
      logOut: false,
      user_details: true,
      payment: false,
      account: false,
      analytics: false
    }
  }

  handle_logout(){
    firebase.auth().signOut();
        this.setState({
            logOut: true
    });
  }

  show_user_details(){
      this.setState({
          user_details: true,
          payment: false,
          account: false,
          analytics: false
    });
  }


  show_account(){
    firebase.auth().signOut();
      this.setState({
          user_details: false,
          payment: false,
          account: true,
          analytics: false
    });
  }


  show_payment(){
    firebase.auth().signOut();
      this.setState({
          user_details: false,
          payment: true,
          account: false,
          analytics: false
    });
  }

  show_analytics(){
    firebase.auth().signOut();
      this.setState({
          user_details: false,
          payment: false,
          account: false,
          analytics: true
    });
  }


  render() {
    if(!this.state.logOut)
    return(
      <div className="formPage">
        <section className="homeSection">
          <table className="tableClass">
            <tbody className="tbodyClass">
              <tr> 
                <td><img className="logo-image" width="100vh" height="103vh" alt="logo" src={logo} /></td>
                <td><h1>follower#Stack</h1></td>
              </tr>
            </tbody>
          </table>
          <nav id="main-menu">
            <ul className="nav-bar">
              <li className="nav-button-home"><a onClick={this.show_analytics.bind(this)} href="#">Analytics</a></li>
              <li className="nav-button-services"><a onClick={this.show_user_details.bind(this)} href="#">User Details</a></li>
              <li className="nav-button-products"><a onClick={this.show_account.bind(this)} href="#">Account</a></li>
              <li className="nav-button-products"><Link to={"/details"}>Payment</Link></li>
              <li className="nav-button-products"><a onClick={this.handle_logout.bind(this)} href="#">Sign Out</a></li>
            </ul>
          </nav>
          <h2>Hello!</h2>
          {this.state.user_details? <Form /> : <h2></h2>}
          {this.state.payment? <h2>Payment</h2> : <h2></h2>}
          {this.state.account? <h2>Account</h2> : <h2></h2>}
          {this.state.analytics? <h2>User Details</h2> : <h2></h2>}
          
        </section>
      </div>
    )
    else
      return(
        <Landing />
        )
  }
}
