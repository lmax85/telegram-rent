<?php

use App\Models\City;
use App\Models\Author;
use App\Models\Country;
use App\Models\Message;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
    // dump(Author::all());
    // dump(City::all());
    // dump(Country::with('cities')->get());
    // dump(Message::with(['group', 'author', 'photos'])->get());
    // dd($data);
});
