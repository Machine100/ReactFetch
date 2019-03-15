import React, {Component} from 'react';

class GoFetch extends Component {
	state = {
		count: 0,
		monsterpic: 'https://sowfpbj0a4.execute-api.us-east-1.amazonaws.com/stagename1/pets/'
	}
	render(){
		const {count} = this.state
		const {monsterpic} = this.state
		return(
			<React.Fragment>
				//<img src={this.state.monsterpic} alt='' />
				//<span>{monsterpic}</span>
				<span>{count}</span>
				<button>innertext</button>
			</React.Fragment>
		);
	}
}

export default GoFetch;


//inside the render is a return