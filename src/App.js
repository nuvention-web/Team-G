import React from 'react';
import ReactDOM from 'react-dom';
import LogIn from './components/Login'
import * as firebase from 'firebase';

export default class App extends React.Component {
  // constructor(){
  //   super();
  //   this.state = {
  //     speed: 10    
  //   };
  // }

  // componentDidMount(){
  //   const rootRef = firebase.database().ref().child('react');
  //   const speedRef = rootRef.child('speed');
  //   speedRef.on('value',snap => {
  //     this.setState({
  //       speed: snap.val()
  //     })
  //   });
  // }


  render() {
    return(
        <div className="App">
          <LogIn />

      	</div>
    )
  }
}