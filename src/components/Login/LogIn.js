import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './Login.css'
import * as firebase from 'firebase';
import classNames from 'classnames/bind';
import background from '../../../img/landing.jpg'
import Home from '../Home'
 
export default class LogIn extends React.Component {
  constructor(){
    super();
    //this.validate = this.validate.bind(this);
    //this.register = this.register.bind(this);
    this.state = {
      email: '',
      pwd: '',
      serv_err_msg : null,
      validUser: false
    }
  }


validate() {
    firebase.auth().signOut();
    console.log("Enter validate");
    const auth = firebase.auth();
    const email = this.state.email;
    const pwd = this.state.pwd;
    console.log(email)
    console.log(pwd)
    const promise = auth.signInWithEmailAndPassword(email,pwd);
    promise.catch(ex => {
      this.setState({
        serv_err_msg: ex.message
      });
      console.log(ex.message);
    });
    
    firebase.auth().onAuthStateChanged(firebaseUser => {
         if(firebaseUser){
             console.log(firebaseUser);
             this.setState({
              validUser: true
             });
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
    promise.catch(ex => {
        console.log(ex.message);
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
  //console.log("email" + e.target.value)
  this.setState({
    email: e.target.value
  });
}

setPwd(e){
  //console.log("pass" + e.target.value)
  this.setState({
    pwd: e.target.value
  });
}

  render() {
    var formError = classNames({
      'has-error form-group': this.state.serv_err_msg
    });

    if(!this.state.validUser)
          return (
            <div className="login-container">
            <div className="login-card">
              <h1>Log-in</h1><br />
              <form>
                <input className={formError} type="text" name="user" id="txtEmail" placeholder="Username" value={ this.state.email } onChange={ this.setEmail.bind(this) }/>
                {this.state.serv_err_msg!=null? <span className ="form-error">{this.state.serv_err_msg}</span> : <span></span>}
                <input className={formError} type="password" name="pass" id="txtPwd" placeholder="Password" value={ this.state.pwd } onChange={this.setPwd.bind(this)}/>
                <button type="button" className="login login-submit" onClick={this.validate.bind(this)}>Log In</button>
              </form> 
              <div className="login-help">
                <a href="#" onClick={this.register.bind(this)}>Register</a> • <a href="#">Forgot Password</a>
              </div>
            </div>
          </div>
          )
      else
        return(
          <Home />
        )
  }
}