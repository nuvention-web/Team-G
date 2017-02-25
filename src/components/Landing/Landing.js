import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './Landing.css'
import logo from '../../../img/logo1.png'
import arrow from '../../../img/arrow.png'
import Home from '../Home' 
import Login from '../Login' 


export default class Landing extends React.Component {
  constructor(){
    super();
    this.state = {
      loginClicked: false    
    };
  }

handle_login(){
  console.log("here")
  this.setState({
    loginClicked: true
  });
}

  render() {
    if(!this.state.loginClicked)
      return(
        <div className="landing-body">
          
          <section className="hero">
          <div className="login-float">
            <a onClick={this.handle_login.bind(this)} className="btn-landing-top anchor-tag" href="#">Login/Signup</a>
          </div>
            <div className="clear-center"></div>
            <img className="logo-image" width="380vh" height="400vh" alt="logo" src={logo} />
            <h1><span className="pos1">follower#Stack</span></h1>
            <h2>We're in the business of growing your business. Using a combination of filters and key 
              parameters, we direct target audience to your social media platforms to grow your social 
              media presence organically. You can be as broad or as specific as you want for your target audience, 
              and can utilize multiple social media platforms, all within the umbrella of followerStack.</h2>
            <div className="arrow-class">
              <p>Scroll to find out more!</p>
              <img width="50vh" height="50vh" src={arrow}></img>
            </div>
          </section>
          
          <section className="section">

            <div className="wrapper">
              <h2 className="section__title">Boost your social media growth</h2>
              <p className="section__intro">
                Look no further. We've got you covered. Here are some of our amazing features
              </p>
              
              <div className="box__grid">              
                <article className="box">
                  <a className="box__content anchor-tag" href="#"><i className="fa fa-lightbulb-o fa-3x"></i>
                    <h3 className="box__title">Tailored Followers</h3>
                    <p>Through the use of our comprehensive algorithms, our program allows you to select the kind of people you want 
                      to interact with based off of age, gender and location.</p>
                  </a>
                </article>
                <article className="box">
                  <a className="box__content anchor-tag" href="#"><i className="fa fa-code fa-3x"></i>
                    <h3 className="box__title">Human Algorithm</h3>
                    <p>Our program was built people in mind. All of the activity is done mimics how a person would normally interact 
                      with Instagram</p>
                  </a>
                </article>
                <article className="box">
                  <a className="box__content anchor-tag" href="#"><i className="fa fa-code fa-3x"></i>
                    <h3 className="box__title">Ban Proof</h3>
                    <p>We spent months testing our program over 150 accounts and only felt comfortable releasing it once 
                      we knew it was 100% safe.</p>
                  </a>
                </article>
              </div>

            </div>
          </section>

          <div className="section section--cta">
            
            <div className="wrapper">
              <h2 className="section__title">What're you waiting for?</h2>
              <p className="section__intro">Interested in signing up?</p>
                <a onClick={this.handle_login.bind(this)} className="btn-landing-bottom anchor-tag" href="#">Lets get started</a>
            </div>
          
          </div>
          
          <div className="landing-footer">
            <p>&copy; 2017 Follower Stack</p>
          </div>
        </div>  
      )
    else
      return(
        <Login />
      )
  }
}