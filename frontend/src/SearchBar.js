import React from 'react'

class SearchBar extends React.Component {
  handleChange = e => {
    console.log(e.target.value)
  }

  handleSubmit = e => {
    e.preventDefault()
    console.log('Form Submited');
  }

  render(){
    return(
      <form onSubmit={this.handleSubmit}>
        <input
        type="text"
        name="first-name"
        onChange={this.handleChange}
        placeholder="start typing here..."
        />
      </form>
    )
  }
}

export default SearchBar
