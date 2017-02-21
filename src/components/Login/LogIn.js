import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './Login.css'
 
export default class LogIn extends React.Component {

  loginClicked(e){
    e.preventDefault();
    console.log("HERE")
    this.props.authFunc();
  }

  render() {
          return (
            <div className="login-card">
              <h1>Log-in</h1><br />
              <form onSubmit={this.loginClicked.bind(this)}>
                <input type="text" name="user" placeholder="Username" />
                <input type="password" name="pass" placeholder="Password" />
                <input type="submit" name="login" className="login login-submit" value="login" />
              </form> 
              <div className="login-help">
                <a href="#">Register</a> • <a href="#">Forgot Password</a>
              </div>
            </div>
          )
  }
}