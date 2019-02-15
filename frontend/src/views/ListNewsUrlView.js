import React from 'react'
// import { Link } from 'react-router-dom'
import { gql, graphql } from 'react-apollo'


const query = gql`{
  allNewsUrls{
    edges{
      node{
        id
        title
        url
        createdAt
      }
    }
  }
}`


class ListNewsUrlView extends React.Component {
  render(){
    let { data } = this.props
    if (data.loading){
      return <div>loading...</div>
    }

    return(
        <div>
          {data.allNewsUrls.edges.map((item, index) => (
            <div key={item.node.id}>
              <h3>{item.node.title}</h3>
              <a href={item.node.url} rel="noopener noreferrer" target="_blank">Подробнее</a>
            </div>
          ))}
        </div>
    )
  }
}

ListNewsUrlView = graphql(query)(ListNewsUrlView)

export default ListNewsUrlView
