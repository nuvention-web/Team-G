import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './Home.css'
 
export default class Home extends React.Component {

  handleSubmit(e){
    e.preventDefault();
    console.log("In home page")
  }

  render() {
    return(
        <div className="home">
          <h3>Home</h3>
          <form onSubmit={this.handleSubmit.bind(this)}>
            <label>Name</label><br />
            <input type="text" ref="data1" /><br /><br />
            <label>Email</label><br />
            <input type="text" ref="data2" /><br /><br />
            <label>Phone</label><br />
            <input type="text" ref="data2" /><br /><br />
            <label>Business Name</label><br />
            <input type="text" ref="data2" /><br /><br />
            <input type="submit" ref="submit" value="Submit" />
          </form>
      </div>
    )
  }
}