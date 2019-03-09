import React from 'react'
// import { Link } from 'react-router-dom'
import { gql, graphql } from 'react-apollo'
import classes from './ListNewsUrlView.css'

const query = gql`{
  allNewsUrls(first: 10) {
    edges {
      node {
        id
        createdAt
        title
        url
        siteUrl
      }
      cursor
    }
    pageInfo {
      hasNextPage
      hasPreviousPage
      startCursor
      endCursor
    }
  }
}
`

class ListNewsUrlView extends React.Component {

  handleOnButtonPagination = () => {
    return this.props.loadMoreEntries();
  }

  render(){

    let { data } = this.props
    if (this.props.loading) return <div>loading...</div>;

    const parserNews = this.props.allNewsUrls.edges.map((item, index) => (
      <div key={item.node.id} className="col-md-6 offset-md-3">
        <h3 className={classes.Title}>{item.node.title}</h3>
        <h5 className={classes.SiteUrl}>{item.node.siteUrl}</h5>
        <a className={classes.MoreButton} href={item.node.siteUrl + item.node.url}
          rel="noopener noreferrer" target="_blank">Подробнее</a>
      </div>
    ))

    const buttonPagination = (
      <button className={classes.ButtonPagination} onClick={this.handleOnButtonPagination}>Что там еще</button>
    )

    return(
          <div className="container">
            <div className={"row d-flex " + classes.NewsFeed}>
              {parserNews}
              <div className={"col-md-6 offset-md-3 " + classes.NewsButtonContainer}>
                {buttonPagination}
              </div>
              {console.log(this.props)}
            </div>
          </div>
    )
  }
}

const MoreNewsUrls = gql`query AllNewsUrls($cursor: String){
  allNewsUrls(first:10, after:$cursor){
    edges{
      cursor
      node {
        id
        createdAt
        title
        url
        siteUrl
      }
    }
    pageInfo{
      hasNextPage
      hasPreviousPage
      startCursor
      endCursor
    }
  }
}`

ListNewsUrlView = graphql(MoreNewsUrls, {
  props: ({data: {loading, allNewsUrls, after, fetchMore}}) => ({
    loading,
    allNewsUrls,
    loadMoreEntries(){
      return fetchMore({
        query: MoreNewsUrls,
        variables: {
          cursor: allNewsUrls.pageInfo.endCursor,
        },
        updateQuery: (previousResult, {fetchMoreResult}) => {
          const newEdges = fetchMoreResult.allNewsUrls.edges;
          const pageInfo = fetchMoreResult.allNewsUrls.pageInfo;
          return newEdges.length
            ? {
              allNewsUrls: {
                __typename: previousResult.allNewsUrls.__typename,
                edges: [...previousResult.allNewsUrls.edges, ...newEdges],
                pageInfo
              }
            }
            : previousResult
        }
      })
    }
  })
})(ListNewsUrlView)

export default ListNewsUrlView
