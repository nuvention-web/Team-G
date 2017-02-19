import React, { Component } from 'react';
import ReactDOM from 'react-dom';
 
export default class LogIn extends React.Component {

  handleSubmit(e){
    e.preventDefault();
    console.log("HERE")
  }

  render() {
    return(
        <div className="LogIn">
          <h3>Log In</h3>
          <form onSubmit={this.handleSubmit.bind(this)}>
            <label>Username</label><br />
            <input type="text" ref="username" /><br />
            <label>Password</label><br />
            <input type="password" ref="password" /><br /><br />
            <input type="submit" ref="submit" value="Log in" />
          </form>

      </div>
    )
  }
}