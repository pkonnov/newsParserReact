import React from 'react'
// import { Link } from 'react-router-dom'
import { gql, graphql } from 'react-apollo'
import classes from './ListNewsUrlView.css'


const query = gql`{
  allNewsUrls{
    edges{
      node{
        id
        title
        url
        siteUrl
      }
    }
  }
}`


class ListNewsUrlView extends React.Component {

  // getDataQuery(){
  //   const data = this.props
  //   const url = data.data.allNewsUrls.edges[0].node.url
  //   var changedUrl = setTimeout(function t(){
  //     return url
  //     changedUrl = setTimeout(t,5000)
  //   }, 5000)
  // }


  render(){
    let { data } = this.props
    if (data.loading){
      return <div>loading...</div>
    }

    let socket = new WebSocket('ws://0.0.0.0:8000/')

    const parserNews = data.allNewsUrls.edges.map((item, index) => (
      <div key={item.node.id} className="col-md-6 offset-md-3">
        <h3 className={classes.Title}>{item.node.title}</h3>
        <h5 className={classes.SiteUrl}>{item.node.siteUrl}</h5>
        <a className={classes.MoreButton} href={item.node.siteUrl + item.node.url} rel="noopener noreferrer" target="_blank">Подробнее</a>
      </div>
    ))

    return(
        <div className="container">
          <div className="row d-flex">
            {parserNews}
            {this.socket}
          </div>
        </div>
    )
  }
}

// ListNewsUrlView = graphql(query,{
//  options:{pollInterval: 5000},
// })(ListNewsUrlView)


ListNewsUrlView = graphql(query)(ListNewsUrlView)

export default ListNewsUrlView
