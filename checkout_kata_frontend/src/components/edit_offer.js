import "./edit_offer.css";
import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import axios from "axios";
import { showErrorToast, showSuccessToast } from "./toasts";
import "react-toastify/dist/ReactToastify.css";

// API endpoints — ideally should come from env vars
const API_BASE_URL = "http://127.0.0.1:8000/api";
const GET_OFFER_DETAILS = `${API_BASE_URL}/api/discounts/`;
const UPDATE_OFFER = `${API_BASE_URL}/discounts/update/`;
const DELETE_OFFER = `${API_BASE_URL}/discounts/delete/`;

const EditOffer = () => {
    const { productId } = useParams();
    const navigate = useNavigate();

    const [offer, setOffer] = useState({
        product: "",
        quantity: "",
        discount_price: ""
    });
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        if (!productId) return;

        const fetchOffer = async () => {
            try {
                const { data } = await axios.get(`${GET_OFFER_DETAILS}${productId}/`);
                setOffer({
                    product: data.product,
                    quantity: data.quantity,
                    discount_price: data.discount_price
                });
            } catch (error) {
                console.error("Error fetching offer:", error);
                showErrorToast("Failed to load offer details.");
            } finally {
                setLoading(false);
            }
        };

        fetchOffer();
    }, [productId]);

    const handleUpdate = async (e) => {
        e.preventDefault();
        try {
            await axios.patch(`${UPDATE_OFFER}${productId}/`, {
                quantity: parseInt(offer.quantity),
                discount_price: parseFloat(offer.discount_price)
            });
            showSuccessToast("Offer updated successfully!");
            navigate("/");
        } catch (error) {
            console.error("Error updating offer:", error);
            showErrorToast("Failed to update offer. Please try again.");
        }
    };

    const handleDelete = async () => {
        if (!window.confirm("Are you sure you want to delete this offer?")) return;
        try {
            await axios.delete(`${DELETE_OFFER}${productId}/`);
            showSuccessToast("Offer deleted successfully!");
            navigate("/");
        } catch (error) {
            console.error("Error deleting offer:", error);
            showErrorToast("Failed to delete the offer.");
        }
    };

    return (
        <div className="edit-offer-container">
            <h2>Edit Offer</h2>
            {loading ? (
                <p>Loading offer details...</p>
            ) : (
                <form onSubmit={handleUpdate}>
                    <label htmlFor="product">Product ID:</label>
                    <input type="text" id="product" value={offer.product} readOnly />

                    <label htmlFor="quantity">Quantity:</label>
                    <input
                        type="number"
                        id="quantity"
                        value={offer.quantity}
                        onChange={(e) => setOffer({ ...offer, quantity: e.target.value })}
                        required
                    />

                    <label htmlFor="discount_price">Discount Price:</label>
                    <input
                        type="number"
                        id="discount_price"
                        value={offer.discount_price}
                        onChange={(e) => setOffer({ ...offer, discount_price: e.target.value })}
                        required
                    />

                    <div className="button-container">
                        <button type="submit" className="update-button">Update</button>
                        <button type="button" className="delete-button" onClick={handleDelete}>Delete</button>
                    </div>
                </form>
            )}
        </div>
    );
};

export default EditOffer;
