import React from 'react';
import ReactDOM from 'react-dom';
//import LogIn from './components/Login'
import Home from './components/Home'
import * as firebase from 'firebase';
import Landing from './components/Landing';
import Form from './components/Form';
import {BrowserRouter, Route} from 'react-router-dom';

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
        <BrowserRouter>
            <Route path="/" component={Landing} >
            <Route path={"details"} component={Form} />
            </Route>
        </BrowserRouter>
        </div>
        
      )


  }
}