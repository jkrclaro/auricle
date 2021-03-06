import React, { Component } from 'react';
import { connect } from 'react-redux';

import Layout from '../components/Layout';
import Sidebar from './Sidebar';


class NotFound extends Component {

    render() {
        return (
            <div>
                {!this.props.auth.isAuthenticated ? (
                    <Layout>
                        {this.props.children}
                    </Layout>
                ) : (
                    <Sidebar>
                        <div className='mt-5'>
                            {this.props.children}
                        </div>
                    </Sidebar>
                )}
            </div>
        )
    }
}

const mapStateToProps = state => {
    return {
        auth: state.auth
    }
}

export default connect(
    mapStateToProps
)(NotFound);