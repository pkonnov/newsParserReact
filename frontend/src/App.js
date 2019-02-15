import React, { Component } from 'react'
import {
  ApolloClient,
  ApolloProvider,
  createBatchingNetworkInterface,
} from 'react-apollo'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'
import HomeView from './views/HomeView'
import CreateView from './views/CreateView'
import DetailView from './views/DetailView'
import ListNewsUrlView from './views/ListNewsUrlView'

const networkInterface = createBatchingNetworkInterface({
  uri: 'http://0.0.0.0:8000/gql/',
  batchInterval: 10,
  opts: {
    credentials: 'same-origin',
  },
})

const client = new ApolloClient({
  networkInterface: networkInterface,
})

class App extends Component {
  render() {
    return (
      <ApolloProvider client={client}>
        <Router>
          <div>
            <Route exact path="/" component={HomeView} />
            <Route exact path="/news" component={ListNewsUrlView} />
            <Switch>
              <Route exact path="/messages/create/" component={CreateView} />
              <Route exact path="/messages/:id/" component={DetailView} />
            </Switch>
          </div>
        </Router>
      </ApolloProvider>
    )
  }
}

export default App
