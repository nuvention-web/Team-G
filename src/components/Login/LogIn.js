import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import Home from '../Home'
 
export default class LogIn extends React.Component {

  constructor(){
    super();
    this.state = {
      validUser : false
    }
  }

  loginClicked(e){
    this.setState({validUser: true });
    e.preventDefault();
  }

  render() {
        if (!this.state.validUser) 
          return (
           <div className="wrapper">
              <div className="container">
                <h1>Welcome</h1>
                <form className="form">
                  <input type="text" placeholder="Username" />
                  <input type="password" placeholder="Password" />
                  <button type="submit" id="login-button" onClick={this.loginClicked.bind(this)}>Login</button>
                </form>
              </div>
              <ul className="bg-bubbles">
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
              </ul>
            </div>
            )

         return <Home />
  }
}