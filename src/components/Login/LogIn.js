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
      confirmPwd:'',
      newUsr: false,
      serv_err_msg : null,
      validUser: false,
      pwd_matched: false

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
    firebase.auth().signOut();
    const email = this.state.email;
    const pwd = this.state.pwd;
    const confirmPwd = this.state.confirmPwd;
    console.log(this.state.pwd_matched);
    console.log(pwd);
    console.log(confirmPwd);
    if(pwd==confirmPwd){
        console.log("inside if");
        this.setState({
        pwd_matched: true
        });
        console.log(this.state.pwd_matched);
    } else{
        this.setState({
        serv_err_msg: "These passwords don't match. Try again?"
        });
    }
    console.log(this.state.pwd_matched);
    console.log("Enter register");

    if(this.state.pwd_matched){
        console.log("@@@@@@@@@@@@@@@@");
    const auth = firebase.auth();
    const promise = auth.createUserWithEmailAndPassword(email,pwd);
    promise.catch(ex => {
        this.setState({
        serv_err_msg: ex.message
      });
        console.log(ex.message);
    });
        
    firebase.auth().onAuthStateChanged(firebaseUser => {
       if(firebaseUser){
           console.log(this.state.validUser)
           console.log(firebaseUser);
           this.setState({
              validUser: true
             });
       } else{
           console.log("Not Logged In");
       }
    });
  }
}

newuser() {
      this.setState({
        newUsr: true
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

setConfirmPwd(e){
    this.setState({
        confirmPwd: e.target.value
    })
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
                 {this.state.newUsr ? <input className={formError} type="password" name="cpass" id="ctxtPwd" placeholder="Confirm Password" value={ this.state.confirmPwd } onChange={this.setConfirmPwd.bind(this)} />:<span></span>}
                {this.state.newUsr ? <button type="button" className="login login-submit" onClick={this.register.bind(this)}>Register</button>
              : <button type="button" className="login login-submit" onClick={this.validate.bind(this)}>Log In</button>}
              </form> 
              <div className="login-help">
                <a href="#" onClick={this.newuser.bind(this)}>Register</a> • <a href="#">Forgot Password</a>
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