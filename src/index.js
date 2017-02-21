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

ReactDOM.render(
    <App />, document.getElementById('root')
);