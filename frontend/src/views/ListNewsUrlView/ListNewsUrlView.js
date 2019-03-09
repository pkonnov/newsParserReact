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

  componentDidMount(){
    window.addEventListener("scroll", this.handleOnScroll)
  }

  handleOnScroll = () => {
    let scrollTop =
      (document.documentElement && document.documentElement.scrollTop) ||
      document.body.scrollTop;
    let scrollHeight =
      (document.documentElement && document.documentElement.scrollHeight) ||
      document.body.scrollHeight;
    let clientHeight =
      document.documentElement.clientHeight || window.innerHeight;
    let scrolledToBottom = Math.ceil(scrollTop + clientHeight) >= scrollHeight;
    if (scrolledToBottom) {
      this.props.loadMoreEntries();
    }
  }

  render(){

    let { data } = this.props
    if (this.props.loading){
      return <div>loading...</div>
    }

    // const parserNews = data.allNewsUrls.edges.map((item, index) => (
    //   <div key={item.node.id} className="col-md-6 offset-md-3">
    //     <h3 className={classes.Title}>{item.node.title}</h3>
    //     <h5 className={classes.SiteUrl}>{item.node.siteUrl}</h5>
    //     <a className={classes.MoreButton} href={item.node.siteUrl + item.node.url}
    //       rel="noopener noreferrer" target="_blank">Подробнее</a>
    //   </div>
    // ))

    return(
          <div className="container">
            <div className="row d-flex">
              {console.log(this.props)}
            </div>
          </div>
    )
  }
}

const MoreNewsUrls = gql`query AllNewsUrls($cursor:String!){
  allNewsUrls(cursor:$cursor){
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


ListNewsUrlView = graphql(query,
{options:
  {pollInterval: 60000},
  props({ data: {cursor, allNewsUrls, loading, fetchMore} }) {
    return {
      loadMoreEntries: () => {
        return fetchMore({
          query: MoreNewsUrls,
          variables:{cursor:cursor},
          updateQuery: (previousResult, { fetchMoreResult }) => {
            console.log(previousResult);
            console.log(fetchMoreResult);
          },
        });
      },
    };
  }
})(ListNewsUrlView)


// ListNewsUrlView = graphql(query)(ListNewsUrlView)

export default ListNewsUrlView
