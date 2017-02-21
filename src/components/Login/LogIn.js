import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './Login.css'
import * as firebase from 'firebase';
 
export default class LogIn extends React.Component {
  constructor(){
    super();
    this.validate = this.validate.bind(this);
    this.register = this.register.bind(this);
    this.state = {
      email: '',
      pwd: ''
    }
  }

  loginClicked(e){
    e.preventDefault();
    console.log("HERE")
    this.props.authFunc();
  }

validate() {
    console.log("Enter validate");
    const auth = firebase.auth();
    
    const email = this.state.email;
    const pwd = this.state.pwd;

    const promise = auth.signInWithEmailAndPassword(email,pwd);
   
    promise
        .catch(ex => {
        console.log(ex.message);
        alert(ex.message);
    });
    
    firebase.auth().onAuthStateChanged(firebaseUser => {
       if(firebaseUser){
           console.log(firebaseUser);
       } else{
           console.log("Not Logged In");
       }
    });
}

    register() {
    console.log("Enter register");
    const auth = firebase.auth();

    const email = this.state.email;
    const pwd = this.state.pwd;
    
    const promise = auth.createUserWithEmailAndPassword(email,pwd);
    promise
        promise
        .catch(ex => {
        console.log(ex.message);
        alert(ex.message);
    });
        
    firebase.auth().onAuthStateChanged(firebaseUser => {
       if(firebaseUser){
           console.log(firebaseUser);
       } else{
           console.log("Not Logged In");
       }
    });
}


setEmail(e){
  //console.log("emaol" + e.target.value)
  this.setState({
    email: e.target.value
  });
}

setPwd(e){
  //console.log("poss" + e.target.value)
  this.setState({
    pwd: e.target.value
  });
}

  render() {
          return (
            <div className="login-card">
              <h1>Log-in</h1><br />
              <form onSubmit={this.loginClicked.bind(this)}>
                <input type="text" name="user" id="txtEmail" placeholder="Username" value={ this.state.email } onChange={ this.setEmail.bind(this) }/>
                <input type="password" name="pass" id="txtPwd" placeholder="Password" value={ this.state.pwd } onChange={this.setPwd.bind(this)}/>
                <button type="button" className="login login-submit" onClick={this.validate}>Log In</button>
              </form> 
              <div className="login-help">
                <a href="#" onClick={this.register}>Register</a> • <a href="#">Forgot Password</a>
              </div>
            </div>
          )
  }
}