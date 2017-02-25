import React from 'react';
import ReactDOM from 'react-dom';
//import LogIn from './components/Login'
import Home from './components/Home'
import * as firebase from 'firebase';
import Landing from './components/Landing'

export default class App extends React.Component {
  constructor(){
    super();
    this.state = {
      validUser: false    
    };
    this.handleLogIn = this.handleLogIn.bind(this);
  }

handleLogIn(){
  this.setState({
    validUser : true
  });
}

  render() {
    return(
        <div className="App">
          <Landing />
        </div>
      )


  }
}