from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from database import (
    add_book,
    delete_book,
    retrieve_book,
    retrieve_books,
    update_book
)
from schemas import (
    ErrorResponseModel,
    ResponseModel,
    LibrarySchema,
    UpdateLibraryModel
)

router = APIRouter()

@router.post("/", response_description="Book data added into the database")
async def add_book_data(book: LibrarySchema = Body(...)):
    book= jsonable_encoder(book)
    new_book = await add_book(book)
    return ResponseModel(new_book, "Book added successfully.")

@router.get("/", response_description="Books retrieved")
async def get_books():
    books = await retrieve_books()
    if books:
        return ResponseModel(books, "books data retrieved successfully")
    return ResponseModel(books, "Empty list returned")


@router.get("/{id}", response_description="Book data retrieved")
async def get_book_data(id):
    book = await retrieve_book(id)
    if book:
        return ResponseModel(book, "book data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "book doesn't exist.")

@router.put("/{id}")
async def update_book_data(id: str, req: UpdateLibraryModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_book = await update_book(id, req)
    if updated_book:
        return ResponseModel(
            "Book with ID: {} data updation is successful".format(id),
            "info updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the book data.",
    )

@router.delete("/{id}", response_description="book data deleted from the database")
async def delete_book_data(id: str):
    deleted_book = await delete_book(id)
    if deleted_book:
        return ResponseModel(
            "book with ID: {} removed".format(id), "book deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "book with id {0} doesn't exist".format(id)
    )

