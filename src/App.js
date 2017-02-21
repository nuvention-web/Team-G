import React from 'react';
import ReactDOM from 'react-dom';
import LogIn from './components/Login'
import Home from './components/Home'
import * as firebase from 'firebase';

export default class App extends React.Component {
  constructor(){
    super();
    this.state = {
      validUser: false    
    };
    this.handleLogIn = this.handleLogIn.bind(this);
  }

  // componentDidMount(){
  //   const rootRef = firebase.database().ref().child('react');
  //   const speedRef = rootRef.child('speed');
  //   speedRef.on('value',snap => {
  //     this.setState({
  //       speed: snap.val()
  //     })
  //   });
  // }
handleLogIn(){
  this.setState({
    validUser : true
  });
}

  render() {
    console.log(this.state.validUser)
    if(!this.state.validUser)
      return(
        <div className="App">
          <LogIn authFunc={this.handleLogIn}/>
      	</div>
      )
    else
      return(
        <div className="App">
          <Home />
        </div>
      )
  }
}