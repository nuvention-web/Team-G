import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './Login.css'
import * as firebase from 'firebase';
 
export default class LogIn extends React.Component {

  loginClicked(e){
    e.preventDefault();
    console.log("HERE")
    this.props.authFunc();
  }
validate() {
    console.log("hello");
    const auth = firebase.auth();
    var id = document.getElementById("txtEmail");
    var pass = document.getElementById("txtPwd");
    var email = "";
    var pwd = "";
     if(id!=null){
         email = id.value;
     }
    if(pass!=null){     
         pwd = pass.value;
    }
    console.log(email);
    console.log(pwd);
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
    console.log("hello");
    const auth = firebase.auth();
    var id = document.getElementById("txtEmail");
    var pass = document.getElementById("txtPwd");
    var email = "";
    var pwd = "";
     if(id!=null){
         email = id.value;
     }
    if(pass!=null){     
         pwd = pass.value;
    }
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

  render() {
          return (
            <div className="login-card">
              <h1>Log-in</h1><br />
              <form onSubmit={this.loginClicked.bind(this)}>
                <input type="text" name="user" id="txtEmail" placeholder="Username" />
                <input type="password" name="pass" id="txtPwd" placeholder="Password" />
                <button type="button" className="login login-submit" onClick={this.validate}>Log In</button>

              </form> 
              <div className="login-help">
                <a href="#" onClick={this.register}>Register</a> • <a href="#">Forgot Password</a>
              </div>
            </div>
          )
  }
}