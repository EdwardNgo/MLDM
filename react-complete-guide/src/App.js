import React, { Component } from 'react';
import { BrowserRouter, Redirect, Route, Switch } from 'react-router-dom';
import About from './components/About/About'
import TextClassification from './containers/TextClassification/TextClassification'
import NavBar from './components/NavBar/NavBar'
import Ner from './containers/NerExtractor/Ner'

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <NavBar></NavBar>
        <Switch>
          <Route path='/about' exact component={About}></Route>
          <Route path="/ner" exact component={Ner}></Route>
          <Route path='/textclassify' exact component={TextClassification}></Route>
        </Switch>

      </BrowserRouter>
    );
  }
}

export default App;
