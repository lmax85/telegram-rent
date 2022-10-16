<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});

Route::get('/', function () {
    return 'Hello World';
});

Route::prefix('estate')->group(function () {
    Route::get('/messages', \App\Http\Controllers\Estate\MessageController::class.'@index');

    Route::prefix('authors')->group(function () {
        Route::get('/{author_id}/messages/{id}', \App\Http\Controllers\Estate\MessageController::class.'@show');
    });
});
