import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';  
import * as firebase from 'firebase';

var config = {
    apiKey: "AIzaSyCkXV_EXsijnUO4WSHWq_J10CilS0ctnVc",
    authDomain: "followerstack-4f91d.firebaseapp.com",
    databaseURL: "https://followerstack-4f91d.firebaseio.com",
    storageBucket: "followerstack-4f91d.appspot.com",
    messagingSenderId: "515328014825"
};
firebase.initializeApp(config);


// const fb = firebase  
//   .initializeApp(config)
//   .database()
//   .ref();

// const App = (props) => {  
//   console.log('snapshot', props);
//   return (
//     <div>
//       <h1>My Prototype</h1>
//       <p>{JSON.stringify(props)}</p>
//     </div>
//   );
// }

// fb.on('value', snapshot => {  
//   const store = snapshot.val();
//   ReactDOM.render(
//     <App {...store} />,
//     document.getElementById('root')
//   );
// });



ReactDOM.render(
    <App />, document.getElementById('root')
);