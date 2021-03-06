import React, { Component } from 'react'
import {
  ApolloClient,
  ApolloProvider,
  createBatchingNetworkInterface,
} from 'react-apollo'
import {SubscriptionClient} from 'subscriptions-transport-ws'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'
import { InMemoryCache } from 'apollo-cache-inmemory'
import SearchBar from './SearchBar'
import ListNewsUrlView from './views/ListNewsUrlView/ListNewsUrlView'

const networkInterface = createBatchingNetworkInterface({
  uri: 'http://localhost:8000/gql/',
  batchInterval: 10,
  opts: {
    credentials: 'same-origin',
  },
})

// const WSClient = new SubscriptionClient(`ws://127.0.0.1:8000/gql/`, {
//   reconnect: true,
//   connectionParams: {
//     // Connection parameters to pass some validations
//     // on server side during first handshake
//   }
// })

const client = new ApolloClient({
  networkInterface: networkInterface,
  // link: WSClient,
  // cache: new InMemoryCache()
})

class App extends Component {
  render() {
    return (
      <ApolloProvider client={client}>
        <Router>
          <div className="bootstrap-wrapper">
            <Route exact path="/" component={ListNewsUrlView} />
            <Switch>
              <Route exact path="/test" component={SearchBar} />
            </Switch>
          </div>
        </Router>
      </ApolloProvider>
    )
  }
}

export default App
