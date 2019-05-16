import React, {Component} from 'react';

class GoFetch extends Component {
	state = {
		monsterpic: 'https://s3.amazonaws.com/derffred/outputdestination.png'
	}
	render(){
		const {count} = this.state
		const {monsterpic} = this.state
		return(
			<React.Fragment>
				//<img src={monsterpic} alt='' />
				<button>addtoy</button>
			</React.Fragment>
		);
	}
}

export default GoFetch;


//inside the render is a return