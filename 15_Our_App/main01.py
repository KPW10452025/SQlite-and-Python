import package

package.module.show_all()
# (1, 'Louis', 'Turner', 'Louis@gmail.com', 1, 238000)
# (2, 'Pete', 'Lyn Strong', 'Pete@gmail.com', 1, 305000)
# (3, 'Lizzie', 'Bowles', 'Lizzie@gmail.com', 0, 345000)
# (4, 'Kayla', 'Bowen', 'Kayla@gmail.com', 0, 465000)
# (5, 'Judy', 'Arnold\t', 'Judy@gmail.com', 0, 382000)
# (6, 'Marcus', 'Harper', 'Marcus@gmail.com', 1, 338000)
# (7, 'Brian', 'Williams', 'Brian@gmail.com', 1, 200000)

# Add a record to the database
package.module.add_one('Tim', 'Smith', 'Tim@gmail.com', '1', 360000)
package.module.show_all()
# (1, 'Louis', 'Turner', 'Louis@gmail.com', 1, 238000)
# (2, 'Pete', 'Lyn Strong', 'Pete@gmail.com', 1, 305000)
# (3, 'Lizzie', 'Bowles', 'Lizzie@gmail.com', 0, 345000)
# (4, 'Kayla', 'Bowen', 'Kayla@gmail.com', 0, 465000)
# (5, 'Judy', 'Arnold\t', 'Judy@gmail.com', 0, 382000)
# (6, 'Marcus', 'Harper', 'Marcus@gmail.com', 1, 338000)
# (7, 'Brian', 'Williams', 'Brian@gmail.com', 1, 200000)
# (8, 'Tim', 'Smith', 'Tim@gmail.com', 1, 360000)              <------- the new record

# Delete record use rowid as string 
package.module.delete_one('8')
package.module.show_all()
# (1, 'Louis', 'Turner', 'Louis@gmail.com', 1, 238000)
# (2, 'Pete', 'Lyn Strong', 'Pete@gmail.com', 1, 305000)
# (3, 'Lizzie', 'Bowles', 'Lizzie@gmail.com', 0, 345000)
# (4, 'Kayla', 'Bowen', 'Kayla@gmail.com', 0, 465000)
# (5, 'Judy', 'Arnold\t', 'Judy@gmail.com', 0, 382000)
# (6, 'Marcus', 'Harper', 'Marcus@gmail.com', 1, 338000)
# (7, 'Brian', 'Williams', 'Brian@gmail.com', 1, 200000)
#                                                              <------- has been deleted   
