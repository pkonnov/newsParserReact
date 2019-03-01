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


  constructor(props){
    super(props)
    this.state = {
      data: [],
    }
  }

  // componentDidMount(){
  //   let timerLocation = setTimeout(() => {
  //     if(window.innerWidth < 500){
  //       document.location.href = "http://127.0.0.1:3000/test/"
  //     }
  //     timerLocation = setTimeout(timerLocation, 5000)
  //   }, 5000)
  // }

  render(){

    let { data } = this.props
    if (data.loading){
      return <div>loading...</div>
    }

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
          </div>
        </div>
    )
  }
}

ListNewsUrlView = graphql(query,{
 options:{pollInterval: 60000},
})(ListNewsUrlView)


// ListNewsUrlView = graphql(query)(ListNewsUrlView)

export default ListNewsUrlView
